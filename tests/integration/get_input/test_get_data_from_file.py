from os import path
from pathlib import Path

from python.get_input.get_data_from_file import get_data_from_file

INPUT_FILE = file = path.join(Path(__file__).parent.resolve(), "fixtures", "input.csv")


def test__get_data_from_file__returns_content_of_csv_file() -> None:
    result = get_data_from_file(file=file)

    assert result == [
        [
            "applicant_id",
            "rank",
            "priority_score",
            "contract_id",
            "capacity",
            "state_funded",
            "program_id",
            "admitted",
        ],
        ["A72866", "3", "0", "C1", "0", "0", "P1", "0"],
        ["A94708", "1", "80", "C10", "19", "1", "P2", "1"],
        ["A70101", "1", "80", "C10", "19", "1", "P2", "1"],
    ]
