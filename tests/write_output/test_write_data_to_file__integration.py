from os import path
from pathlib import Path
from csv import reader

from python.write_output.write_data_to_file import write_data_to_file
from tests.helpers import get_random_string

OUTPUT_FOLDER = file = path.join(
    Path(__file__).parent.resolve(),
    "output",
)


def test__write_data_to_file__writes_the_give_data_to_the_given_file() -> None:
    data = [["first", "second", "third"], ["1", "2", "3"]]
    file = path.join(OUTPUT_FOLDER, f"{get_random_string()}.csv")

    write_data_to_file(file=file, data=data)

    result = get_data_from_file(file=file)
    assert result == data


def get_data_from_file(file: str) -> list[list[str]]:
    result = []
    with open(file) as csvfile:
        for row in reader(csvfile):
            result.append(row)
    return result
