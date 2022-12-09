from itertools import chain
from os import environ, path

from python.config import INPUT_FOLDER, OUTPUT_FOLDER
from python.correct_dominated_choices.correct_dominated_choices_lower import (
    correct_dominated_choices_lower,
)
from python.get_input.get_input import get_input
from python.types import Input, Contracts, Applicant
from python.write_output.write_data_to_file import write_data_to_file


def main(input_file: str, output_file: str) -> None:
    input = correct_dominated_choices_lower(get_input(file=input_file))
    write_data_to_file(
        file=output_file,
        data=_get_output_from_input(input=input),
    )


def _get_output_from_input(input: Input) -> list[list[str]]:
    return [
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
        *list(
            chain(
                *[
                    _get_applications(applicant=applicant, contracts=input.contracts)
                    for applicant in input.applicants
                ]
            )
        ),
    ]


def _get_applications(applicant: Applicant, contracts: Contracts) -> list[list[str]]:
    return [
        [
            applicant.id,
            str(rank),
            str(ranked_application.priority_score),
            ranked_application.contract,
            str(contracts[ranked_application.contract].capacity),
            _convert_boolean(value=contracts[ranked_application.contract].state_funded),
            contracts[ranked_application.contract].program_id,
            _convert_boolean(value=ranked_application.admitted),
        ]
        for rank, ranked_application in enumerate(applicant.ranked_applications)
    ]


def _convert_boolean(value: bool) -> str:
    return "1" if value else "0"


if __name__ == "__main__":
    input_file = environ["INPUT"]
    main(
        input_file=path.join(INPUT_FOLDER, input_file),
        output_file=path.join(OUTPUT_FOLDER, f"correct_lower_input_{input_file}"),
    )
