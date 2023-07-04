import pytest

from categorizer import Categorizer
from enumeration.category import Category
from test.conftest import SAMPLE_CONFIG_FILE_PATH
from transaction import Transaction


def test_sample_statements_are_categorized():
    categorizer = Categorizer(SAMPLE_CONFIG_FILE_PATH, [])

    assert categorizer.get_category("COSTCO GAS #0569") == Category.GAS_AND_AUTO
    assert categorizer.get_category("COSTCO WHSE #0479") == Category.GROCERIES
    assert categorizer.get_category("TRADER JOE'S #119") == Category.GROCERIES
    assert categorizer.get_category("STARBUCKS STORE 49208") == Category.FOOD_AND_DRINK
    assert categorizer.get_category("KOKO CHICKEN &amp; BBQ") == Category.FOOD_AND_DRINK
    assert categorizer.get_category("Lowe's") == Category.HOUSE
    assert categorizer.get_category("SOME_UNIDENTIFIED_DESCRIPTION") == Category.UNIDENTIFIED
    assert categorizer.get_category("SOME_UNIDENTIFIED_DESCRIPTION") == Category.UNIDENTIFIED


def test_all_transactions_in_category_are_returned():
    transactions = [
        Transaction(date="_", description="COSTCO GAS #0569", amount=0.0),
        Transaction(date="_", description="COSTCO WHSE #0479", amount=0.0),
        Transaction(date="_", description="TRADER JOE'S #119", amount=0.0),
        Transaction(date="_", description="Payment Thank You - Web", amount=0.0),
        Transaction(date="_", description="Lowe's", amount=0.0),
    ]
    categorizer = Categorizer(SAMPLE_CONFIG_FILE_PATH, transactions)

    category_to_transactions = categorizer.get_all_transactions_by_category()

    assert len(category_to_transactions[Category.GROCERIES]) == 2
    assert len(category_to_transactions[Category.GAS_AND_AUTO]) == 1
    assert len(category_to_transactions[Category.UNIDENTIFIED]) == 1
    assert len(category_to_transactions[Category.HOUSE]) == 1


def test_transactions_are_sorted_by_date():
    category_to_transactions = {
        Category.GROCERIES: [
            Transaction(date="11/22/2020", description="COSTCO WHSE #0479", amount=0.0),
            Transaction(date="11/30/2020", description="TRADER JOE'S #119", amount=0.0),
        ],
        Category.GAS_AND_AUTO: [
            Transaction(date="11/15/2020", description="COSTCO GAS #0479 MAR VISTA CA", amount=0.0),
            Transaction(date="12/01/2020", description="COSTCO GAS #0411 FOUNTAIN VALLCA", amount=0.0),
            Transaction(date="11/27/2020", description="AAFES LA MAIN STORE GAS", amount=0.0),
        ]
    }

    Categorizer.sort_each_category_by_date(category_to_transactions)

    assert category_to_transactions[Category.GROCERIES][0].description == "TRADER JOE'S #119"
    assert category_to_transactions[Category.GAS_AND_AUTO][0].description == "COSTCO GAS #0411 FOUNTAIN VALLCA"
    assert category_to_transactions[Category.GAS_AND_AUTO][-1].description == "COSTCO GAS #0479 MAR VISTA CA"
