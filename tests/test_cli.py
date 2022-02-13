from click.testing import CliRunner
import pytest

from revsplit.cli import hello


@pytest.fixture
def cli_test_runner():
    return CliRunner()


def test_hello_world(cli_test_runner):
    result = cli_test_runner.invoke(hello, ['Karolina'])
    assert result.exit_code == 0
    assert result.output == 'Hello Karolina!\n'
