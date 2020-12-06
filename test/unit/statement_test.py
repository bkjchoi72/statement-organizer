import os
import shutil

import pytest

from chase_statement import ChaseStatement
from citi_statement import CitiStatement
from enumeration.bank import Bank
from statement import Statement
from test.conftest import SAMPLE_CHASE_STATEMENT_PATH, TEST_DIR, SAMPLE_CITI_STATEMENT_PATH


@pytest.mark.parametrize("path,expected_bank", [
    (os.path.join(TEST_DIR, "Year to date.CSV"), Bank.CITI),
    (os.path.join(TEST_DIR, "Chase6725_Activity20200101_20201201_20201201.CSV"), Bank.CHASE),
    (os.path.join(TEST_DIR, "Since Nov 19, 2020.CSV"), Bank.CITI),
    (os.path.join(TEST_DIR, "From 11_1_2020 To 11_30_2020.CSV"), Bank.CITI),
])
def test_bank_name_is_identified_from_statement(path, expected_bank):
    assert Statement.get_bank(path) == expected_bank


def test_statement_with_no_obvious_file_name_is_identified(tmpdir):
    new_statement_path = os.path.join(str(tmpdir), "mysterious_statement.csv")
    shutil.copyfile(SAMPLE_CHASE_STATEMENT_PATH, new_statement_path)
    assert Statement.get_bank(new_statement_path) == Bank.CHASE


def test_chase_statement_is_loaded():
    chase_statement = ChaseStatement()
    chase_statement.statement_path = SAMPLE_CHASE_STATEMENT_PATH
    transactions = chase_statement.get_transactions()
    assert len(transactions) == 11
    assert int(sum([transaction.amount for transaction in transactions])) == 495


def test_citi_statement_is_loaded():
    citi_statement = CitiStatement()
    citi_statement.statement_path = SAMPLE_CITI_STATEMENT_PATH
    transactions = citi_statement.get_transactions()
    assert len(transactions) == 9
    assert int(sum([transaction.amount for transaction in transactions])) == -255
