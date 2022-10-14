from python.types import Matching


def get_output_from_matchings(
    matchings: list[Matching],
) -> list[list[str]]:
    return [
        ["applicant_id", "contract_id", "rank"],
        *[
            [matching.applicant_id, matching.contract_id, str(matching.rank)]
            for matching in matchings
        ],
    ]
