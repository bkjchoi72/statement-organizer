import os

import pytest

from main import main
from test.conftest import SAMPLE_CHASE_STATEMENT_PATH, SAMPLE_CONFIG_FILE_PATH, \
    SAMPLE_CITI_STATEMENT_PATH


@pytest.mark.parametrize("statement_paths", [
    [SAMPLE_CHASE_STATEMENT_PATH],
    [SAMPLE_CITI_STATEMENT_PATH],
])
def test_one_statement_is_processed(tmpdir, statement_paths):
    exit_code = main(statement_paths=statement_paths, output_dir=str(tmpdir), config_file_path=SAMPLE_CONFIG_FILE_PATH, open_output_file_at_the_end=False)
    assert exit_code == 0
    assert len(os.listdir(tmpdir)) > 0


def test_combined_statement_is_created(tmpdir):
    exit_code = main(statement_paths=[SAMPLE_CHASE_STATEMENT_PATH, SAMPLE_CITI_STATEMENT_PATH], output_dir=str(tmpdir),
                     config_file_path=SAMPLE_CONFIG_FILE_PATH, open_output_file_at_the_end=False)
    assert exit_code == 0
    assert len(os.listdir(tmpdir)) > 0
