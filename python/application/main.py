from os import environ

from python.application.validate_input import validate_input
from python.application.validate_stability import validate_stability
from python.get_contracts.get_contracts import get_contracts
from python.application.write_output import write_output
from python.get_input.get_input import get_input


def main(input_file: str, output_file: str) -> None:
    input = get_input(file=input_file)
    validate_input(input=input)
    contracts = get_contracts(applicants=input.applicants, contracts=input.contracts)
    validate_stability(contracts=contracts)
    write_output(file=output_file, contracts=contracts)


if __name__ == "__main__":
    main(input_file=environ.get("INPUT"), output_file=environ.get("OUTPUT"))
