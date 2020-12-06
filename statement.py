import csv
import os
from abc import ABC, abstractmethod
from typing import List

from enumeration.bank import Bank
from exceptions import CouldNotIdentifyStatementError
from transaction import Transaction


class Statement(ABC):
    def __init__(self, statement_path: str = ""):
        self.statement_path = statement_path
        if statement_path:
            self.transactions: List[Transaction] = self.get_transactions()

    @abstractmethod
    def get_transactions(self) -> List[Transaction]:
        pass

    @staticmethod
    def get_bank(statement_path: str) -> Bank:
        file_name = os.path.basename(statement_path)
        if "chase" in file_name.lower():
            return Bank.CHASE
        elif "from" in file_name.lower() or \
                "since" in file_name.lower() or \
                "year" in file_name.lower():
            return Bank.CITI
        with open(statement_path) as fin:
            csv_reader = csv.DictReader(fin)
            if csv_reader:
                if "Transaction Date" in csv_reader.fieldnames:
                    return Bank.CHASE
                elif "Status" in csv_reader.fieldnames:
                    return Bank.CITI
        raise CouldNotIdentifyStatementError
