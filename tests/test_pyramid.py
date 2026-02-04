import subprocess
import sys
from src.pyramid import build_pyramid


def test_build_pyramid_three_rows():
    expected = "  *  \n *** \n*****"
    assert build_pyramid(3) == expected


def test_build_pyramid_one_row():
    assert build_pyramid(1) == "*"


def test_cli_integration(tmp_path, capsys):
    # Run the CLI with 3 rows and capture stdout
    result = subprocess.run([sys.executable, "-m", "src.pyramid", "--rows", "3"], capture_output=True, text=True)
    assert result.returncode == 0
    # Use rstrip of trailing newline only so leading spaces are preserved
    assert result.stdout.rstrip("\n") == build_pyramid(3)
