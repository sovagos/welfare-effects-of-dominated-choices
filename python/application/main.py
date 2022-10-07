from os import environ

from python.get_contracts.get_contracts import get_contracts
from python.application.get_input import get_input
from python.application.write_output import write_output


def main(input_file: str, output_file: str) -> None:
    input = get_input(file=input_file)
    contracts = get_contracts(applicants=input.applicants, contracts=input.contracts)
    write_output(file=output_file, contracts=contracts)


if __name__ == "__main__":
    main(input_file=environ.get("INPUT"), output_file=environ.get("OUTPUT"))
