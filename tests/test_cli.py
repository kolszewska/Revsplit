import pytest
from click.testing import CliRunner

from revsplit.cli import hello


@pytest.fixture
def cli_test_runner():
    return CliRunner()


def test_hello_world(cli_test_runner):
    invoke_result = cli_test_runner.invoke(hello, ['--name', 'Karolina'])
    assert invoke_result.exit_code == 0
    assert invoke_result.output == 'Hello Karolina!\n'
