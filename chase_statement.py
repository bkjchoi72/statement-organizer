import csv
from typing import List

from statement import Statement
from transaction import Transaction


class ChaseStatement(Statement):
    def get_transactions(self) -> List[Transaction]:
        transactions = []
        with open(self.statement_path) as fin:
            csv_reader = csv.DictReader(fin)
            for row in csv_reader:
                transactions.append(
                    Transaction(date=row["Transaction Date"],
                                description=row["Description"],
                                amount=float(row["Amount"]))
                )

        return transactions
