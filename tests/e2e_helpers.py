import os
from csv import writer, reader
from os import path
from pathlib import Path
from subprocess import Popen

from tests.helpers import get_random_string

BASE_PATH = path.join(
    Path(__file__).parent.resolve(),
    "..",
)
INPUT_FOLDER_NAME = "input"
OUTPUT_FOLDER_NAME = "output"


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


def get_result(output_filename: str) -> list[list[str]]:
    result = []
    with open(
        get_absolut_path_of_output_file(output_filename=output_filename)
    ) as csvfile:
        for row in reader(csvfile):
            result.append(row)
    return result


def get_absolut_path_of_output_file(output_filename: str) -> str:
    return path.join(BASE_PATH, OUTPUT_FOLDER_NAME, output_filename)


def run(input_filename: str, application: str) -> None:
    Popen(
        ["python3", "-m", application],
        env={**os.environ.copy(), "INPUT": input_filename},
    ).wait()


def clear(input_filename: str, output_filename: str):
    os.remove(get_absolut_path_of_input_file(input_filename=input_filename))
    os.remove(get_absolut_path_of_output_file(output_filename=output_filename))
