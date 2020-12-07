import os
import logging
from datetime import datetime
from subprocess import Popen
from typing import List, Optional
from tkinter.filedialog import askopenfiles

from categorizer import Categorizer
from chase_statement import ChaseStatement
from citi_statement import CitiStatement
from enumeration.bank import Bank
from exceptions import UnknownStatementError, ConfigFileNotFoundError
from output_writer import OutputWriter
from statement import Statement

HOME_DIR = os.path.expanduser("~")
WORKING_DIR = os.path.join(HOME_DIR, "Desktop", "statement_organizer")
DEFAULT_OUTPUT_DIR = os.path.join(WORKING_DIR, "combined_statements")
DEFAULT_CONFIG_FILE_PATH = os.path.join(WORKING_DIR, "config.txt")


def main(statement_paths: Optional[List[str]] = None, output_dir: str = DEFAULT_OUTPUT_DIR,
         config_file_path: str = DEFAULT_CONFIG_FILE_PATH, open_output_file_at_the_end=True):
    if not os.path.isfile(config_file_path):
        raise ConfigFileNotFoundError

    if not statement_paths:
        selected_files = askopenfiles(title="Choose one or more bank statements in CVS format",
                                      filetypes=[("CSV file", "*.csv")])
        if not selected_files:
            return 1
        statement_paths = [selected_file.name for selected_file in selected_files]
    logging.debug(f"Statements selected: {statement_paths}")

    transactions = []

    for statement_path in statement_paths:
        bank = Statement.get_bank(statement_path)
        if bank == Bank.CHASE:
            statement = ChaseStatement(statement_path)
        elif bank == Bank.CITI:
            statement = CitiStatement(statement_path)
        else:
            raise UnknownStatementError(f"Statement file {statement_path} is not a known statement")
        transactions += statement.get_transactions()

    categorizer = Categorizer(config_file_path, transactions)
    category_to_transactions = categorizer.get_all_transactions_by_category()
    Categorizer.sort_each_category_by_date(category_to_transactions)
    output_writer = OutputWriter(category_to_transactions)
    date_time = datetime.now()
    timestamp = date_time.strftime("%Y%m%d_%H%M%S")
    output_file_path = os.path.join(output_dir, f"combined_statement_{timestamp}.csv")
    output_writer.write_to_file(output_file_path)

    print(f"Combined statement: {output_file_path}")

    if open_output_file_at_the_end:
        Popen(output_file_path, shell=True)

    return 0


if __name__ == '__main__':
    main()
