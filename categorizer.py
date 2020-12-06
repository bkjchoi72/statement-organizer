import logging
import os
from typing import List, Dict

from enumeration.category import Category
from exceptions import ConfigFileNotFoundError
from rule import Rule
from transaction import Transaction


class Categorizer:
    def __init__(self, config_file_path: str, transactions: List[Transaction]):
        self.config_key_to_category: Dict[str: Category] = {category.value: category for category in
                                                            Category}
        self.config_key_to_rule: Dict[str: Rule] = {}
        self.transactions: List[Transaction] = transactions
        self.load_rules_from_config_file(config_file_path)

    @staticmethod
    def sort_each_category_by_date(category_to_transactions: Dict[Category, List[Transaction]]):
        for transactions in category_to_transactions.values():
            transactions.sort(key=lambda transaction: transaction.date, reverse=True)

    def load_rules_from_config_file(self, config_file_path: str):
        if not os.path.isfile(config_file_path):
            raise ConfigFileNotFoundError(
                f"Config file was not found. Given file path: {config_file_path}")
        with open(config_file_path, "r") as fin:
            lines = fin.readlines()
        for line in lines:
            split_by_equal_sign = line.strip().split("=")
            config_key = split_by_equal_sign[0]
            config_substring_value = split_by_equal_sign[1]
            if config_key in self.config_key_to_category:
                rule = self.config_key_to_rule.get(config_key,
                                                   Rule(self.config_key_to_category[config_key]))
                rule.add_rule(config_substring_value)
                self.config_key_to_rule[config_key] = rule
            else:
                logging.error(
                    f"Unrecognized category rule '{config_key}' in the config file {config_file_path}")

    def get_category(self, description: str) -> Category:
        for rule in self.config_key_to_rule.values():
            if rule.satisfies(description):
                return rule.category
        logging.warning(f"Unable to identify the category for the given description: {description}. Returning {Category.UNIDENTIFIED.value}")
        return Category.UNIDENTIFIED

    def get_all_transactions_by_category(self) -> Dict[Category, List[Transaction]]:
        category_to_transactions = {category: [] for category in Category}
        for transaction in self.transactions:
            category = self.get_category(transaction.description)
            category_to_transactions[category].append(transaction)
        return category_to_transactions
