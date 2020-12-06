import csv
import logging
from typing import List

from statement import Statement
from transaction import Transaction


class CitiStatement(Statement):
    @property
    def key_amount(self):
        return "Debit"

    def get_transactions(self) -> List[Transaction]:
        transactions = []
        with open(self.statement_path) as fin:
            csv_reader = csv.DictReader(fin)
            for row in csv_reader:
                amount = 0.0
                if row["Debit"]:
                    amount = -float(row["Debit"])
                elif float(row["Credit"]) < 0.0:
                    amount = -float(row["Credit"])
                else:
                    logging.error(
                        f"Could not determine the amount for transaction {row['Description']} on {row['Date']}")
                transactions.append(
                    Transaction(date=row["Date"],
                                description=row["Description"],
                                amount=amount)
                )

        return transactions
