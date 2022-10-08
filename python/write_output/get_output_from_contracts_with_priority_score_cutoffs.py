from python.types import ContractWithPriorityScoreCutoff


def get_output_from_contracts_with_priority_score_cutoffs(
    contracts_with_priority_score_cutoffs: list[ContractWithPriorityScoreCutoff],
) -> list[list[str]]:
    return [
        ["contract_id", "priority_score_cutoff"],
        *[
            [contract.id, str(contract.priority_score_cutoff)]
            for contract in contracts_with_priority_score_cutoffs
        ],
    ]
