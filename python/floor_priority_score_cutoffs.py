import math


def floor_priority_score_cutoffs(priority_score_cutoffs):
    return {
        contract_id: math.floor(priority_score_cutoff)
        for contract_id, priority_score_cutoff in priority_score_cutoffs.items()
    }
