import os
from csv import writer, reader
from os import path
from pathlib import Path
from subprocess import Popen

from tests.unit.helpers import get_random_string

BASE_PATH = path.join(
    Path(__file__).parent.resolve(),
    "..",
    "..",
    "..",
)
INPUT_FOLDER_NAME = "input"
OUTPUT_FOLDER_NAME = "output"


def test__main() -> None:
    input_data = [
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
        ["A1", "1", "1", "C1", "1", "0", "P1", "0"],
        ["A2", "1", "80", "C2", "19", "1", "P2", "1"],
    ]
    input_filename = create_input_file(input_data)

    run(input_filename)

    result = get_result(input_filename)
    assert result == [
        ["contract_id", "priority_score_cutoff"],
        ["C1", "1"],
        ["C2", "80"],
    ]

    clear(input_filename)


def create_input_file(data: list[list[str]]) -> str:
    filename = f"{get_random_string()}.csv"
    with open(
        get_absolut_path_of_input_file(input_filename=filename), "w+", newline=""
    ) as csvfile:
        spamwriter = writer(csvfile, delimiter=",")
        for row in data:
            spamwriter.writerow(row)
    return filename


def get_absolut_path_of_input_file(input_filename: str) -> str:
    return path.join(BASE_PATH, INPUT_FOLDER_NAME, input_filename)


def get_result(input_filename: str) -> list[list[str]]:
    result = []
    with open(
        get_absolut_path_of_output_file(input_filename=input_filename)
    ) as csvfile:
        for row in reader(csvfile):
            result.append(row)
    return result


def get_absolut_path_of_output_file(input_filename: str) -> str:
    return path.join(BASE_PATH, OUTPUT_FOLDER_NAME, f"result_{input_filename}")


def run(input_filename: str) -> None:
    Popen(
        ["python3", "-m", "python.application.main"],
        env={**os.environ.copy(), "INPUT": input_filename},
    ).wait()


def clear(input_filename):
    os.remove(get_absolut_path_of_input_file(input_filename=input_filename))
    os.remove(get_absolut_path_of_output_file(input_filename=input_filename))
