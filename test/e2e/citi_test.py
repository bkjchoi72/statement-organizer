import os

from main import main
from test.conftest import SAMPLE_CITI_STATEMENT_PATH, SAMPLE_CONFIG_FILE_PATH


def test_one_statement_is_processed(tmpdir):
    exit_code = main(statement_paths=[SAMPLE_CITI_STATEMENT_PATH], output_dir=str(tmpdir), config_file_path=SAMPLE_CONFIG_FILE_PATH)
    assert exit_code == 0
    assert len(os.listdir(tmpdir)) > 0

