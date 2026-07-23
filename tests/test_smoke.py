from typer.testing import CliRunner

import webreel
from webreel.cli import app

runner = CliRunner()


def test_import_exposes_version() -> None:
    assert isinstance(webreel.__version__, str)
    assert webreel.__version__


def test_cli_help_runs() -> None:
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "webreel" in result.stdout.lower()


def test_cli_version_flag() -> None:
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert webreel.__version__ in result.stdout


def test_stub_subcommand_exits_nonzero() -> None:
    result = runner.invoke(app, ["shot", "https://example.com"])
    assert result.exit_code == 2
