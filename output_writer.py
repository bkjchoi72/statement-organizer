import csv
import itertools
from typing import List, Dict

from enumeration.category import Category
from transaction import Transaction


class OutputWriter:
    KEY_AMOUNT = "Amount"
    KEY_DATE = "Date"

    def __init__(self, category_to_transactions: Dict[Category, List[Transaction]]):
        self.category_to_transactions: Dict[Category, List[Transaction]] = category_to_transactions

    def write_to_file(self, outfile_path: str):
        fieldnames = [
            Category.FOOD_AND_DRINK.value, self.KEY_AMOUNT, self.KEY_DATE,
            "",
            Category.GROCERIES.value, self.KEY_AMOUNT, self.KEY_DATE,
            "",
            Category.SHOPPING.value, self.KEY_AMOUNT, self.KEY_DATE,
            "",
            Category.BILLS_AND_UTILITIES.value, self.KEY_AMOUNT, self.KEY_DATE,
            "",
            Category.GAS_AND_AUTO.value, self.KEY_AMOUNT, self.KEY_DATE,
            "",
            Category.TRAVEL_AND_ENTERTAINMENT.value, self.KEY_AMOUNT, self.KEY_DATE,
            "",
            Category.PERSONAL.value, self.KEY_AMOUNT, self.KEY_DATE,
            "",
            Category.UNIDENTIFIED.value, self.KEY_AMOUNT, self.KEY_DATE,
        ]
        with open(outfile_path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            writer.writerow(fieldnames)

            for food_and_drink_transaction, \
                groceries_transaction, \
                shopping_transaction, \
                bills_and_utilities_transaction, \
                gas_and_auto_transaction, \
                travel_and_entertainment, \
                personal_transaction, \
                unidentified_transaction in itertools.zip_longest(
                    self.category_to_transactions[Category.FOOD_AND_DRINK],
                    self.category_to_transactions[Category.GROCERIES],
                    self.category_to_transactions[Category.SHOPPING],
                    self.category_to_transactions[Category.BILLS_AND_UTILITIES],
                    self.category_to_transactions[Category.GAS_AND_AUTO],
                    self.category_to_transactions[Category.TRAVEL_AND_ENTERTAINMENT],
                    self.category_to_transactions[Category.PERSONAL],
                    self.category_to_transactions[Category.UNIDENTIFIED],
                    fillvalue=None,
            ):
                writer.writerow(
                    [
                        self.get_description_or_empty_str(food_and_drink_transaction),
                        self.get_amount_or_empty_str(food_and_drink_transaction),
                        self.get_date_or_empty_str(food_and_drink_transaction),
                        "",
                        self.get_description_or_empty_str(groceries_transaction),
                        self.get_amount_or_empty_str(groceries_transaction),
                        self.get_date_or_empty_str(groceries_transaction),
                        "",
                        self.get_description_or_empty_str(shopping_transaction),
                        self.get_amount_or_empty_str(shopping_transaction),
                        self.get_date_or_empty_str(shopping_transaction),
                        "",
                        self.get_description_or_empty_str(bills_and_utilities_transaction),
                        self.get_amount_or_empty_str(bills_and_utilities_transaction),
                        self.get_date_or_empty_str(bills_and_utilities_transaction),
                        "",
                        self.get_description_or_empty_str(gas_and_auto_transaction),
                        self.get_amount_or_empty_str(gas_and_auto_transaction),
                        self.get_date_or_empty_str(gas_and_auto_transaction),
                        "",
                        self.get_description_or_empty_str(travel_and_entertainment),
                        self.get_amount_or_empty_str(travel_and_entertainment),
                        self.get_date_or_empty_str(travel_and_entertainment),
                        "",
                        self.get_description_or_empty_str(personal_transaction),
                        self.get_amount_or_empty_str(personal_transaction),
                        self.get_date_or_empty_str(personal_transaction),
                        "",
                        self.get_description_or_empty_str(unidentified_transaction),
                        self.get_amount_or_empty_str(unidentified_transaction),
                        self.get_date_or_empty_str(unidentified_transaction),
                    ]
                )

    def get_description_or_empty_str(self, transaction: Transaction):
        if transaction:
            return transaction.description
        return ""

    def get_amount_or_empty_str(self, transaction: Transaction):
        if transaction:
            return "${:,.2f}".format(transaction.amount)
        return ""

    def get_date_or_empty_str(self, transaction: Transaction):
        if transaction:
            return transaction.date
        return ""
