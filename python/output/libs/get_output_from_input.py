from itertools import chain

from python.types import Output, Contracts, Applicant, Input


def get_output_from_input(input: Input) -> Output:
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


def _get_applications(applicant: Applicant, contracts: Contracts) -> Output:
    return [
        [
            applicant.id,
            str(rank + 1),
            str(ranked_application.priority_score),
            ranked_application.contract,
            str(contracts[ranked_application.contract].capacity),
            _get_converted_bool(
                value=contracts[ranked_application.contract].state_funded
            ),
            contracts[ranked_application.contract].program_id,
            _get_converted_bool(value=ranked_application.admitted),
        ]
        for rank, ranked_application in enumerate(applicant.ranked_applications)
    ]


def _get_converted_bool(value: bool) -> str:
    return "1" if value else "0"
