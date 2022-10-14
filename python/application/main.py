import sys
from os import environ, path
from pathlib import Path

from python.get_matching.get_matching import get_matching
from python.get_input.get_input import get_input
from python.write_output.write_output import write_output

BASE_PATH = path.join(
    Path(__file__).parent.resolve(),
    "..",
    "..",
)
INPUT_FOLDER = path.join(BASE_PATH, "input")
OUTPUT_FOLDER = path.join(BASE_PATH, "output")

sys.setrecursionlimit(10**8)


def main(input_file: str, output_file: str) -> None:
    input = get_input(file=input_file)
    matchings = get_matching(applicants=input.applicants, contracts=input.contracts)
    write_output(file=output_file, data=matchings)


if __name__ == "__main__":
    input_file = environ["INPUT"]
    main(
        input_file=path.join(INPUT_FOLDER, input_file),
        output_file=path.join(OUTPUT_FOLDER, f"result_{input_file}"),
    )
