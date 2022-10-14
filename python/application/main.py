import sys
from os import environ, path
from pathlib import Path

from python.application.validate_input import validate_input
from python.application.validate_stability import validate_stability
from python.get_contracts.get_contracts import get_contracts
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
    validate_input(input=input)
    contracts = get_contracts(applicants=input.applicants, contracts=input.contracts)
    validate_stability(contracts=contracts)
    write_output(file=output_file, data=contracts)


if __name__ == "__main__":
    main(
        input_file=path.join(INPUT_FOLDER, environ["INPUT"]),
        output_file=path.join(OUTPUT_FOLDER, f"result_{environ['INPUT']}"),
    )
