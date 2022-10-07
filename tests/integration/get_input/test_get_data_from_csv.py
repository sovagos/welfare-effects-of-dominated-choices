from os import path
from pathlib import Path

from python.application.get_input import get_input

INPUT_FILE = file = path.join(Path(__file__).parent.resolve(), "fixtures", "input.csv")

def test__get_data_from_csv__returns_content_of_csv_file() -> None:
    result = get_input(file=file)

    assert result == [
        ["A72866", "3", "0", "C1", "0", "0", "0"],
        ["A94708", "1", "80", "C10", "80", "19", "1"],
        ["A70101", "1", "80", "C10", "80", "19", "1"],
    ]