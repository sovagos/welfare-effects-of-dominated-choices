from python.types import Matching, Output


def get_output_from_matchings(
    matchings: list[Matching],
) -> Output:
    return [
        ["applicant_id", "contract_id", "rank"],
        *[
            [matching.applicant_id, matching.contract_id, str(matching.rank)]
            for matching in matchings
        ],
    ]
