from os import path
from pathlib import Path

from python.get_input.get_data_from_file import get_data_from_file

INPUT_FILE = file = path.join(Path(__file__).parent.resolve(), "fixtures", "input.csv")


def test__get_data_from_file__returns_content_of_csv_file() -> None:
    result = get_data_from_file(file=file)

    assert result == [
        {
            "applicant_id": "A72866",
            "rank": "3",
            "priority_score": "0",
            "contract_id": "C1",
            "capacity": "0",
            "state_funded": "0",
            "program_id": "P1",
            "admitted": "0",
        },
        {
            "applicant_id": "A94708",
            "rank": "1",
            "priority_score": "80",
            "contract_id": "C10",
            "capacity": "19",
            "state_funded": "1",
            "program_id": "P2",
            "admitted": "1",
        },
        {
            "applicant_id": "A70101",
            "rank": "1",
            "priority_score": "80",
            "contract_id": "C10",
            "capacity": "19",
            "state_funded": "1",
            "program_id": "P2",
            "admitted": "1",
        },
    ]
