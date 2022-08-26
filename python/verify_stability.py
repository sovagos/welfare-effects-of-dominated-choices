import math


def verify_stability(matching, applicants, priority_score_cutoffs):
    for applicant in applicants.values():
        for rank in range(_get_least_preferred_rank_to_be_verified(
                applicant=applicant,
                assigned_contract_id=matching[applicant.applicant_id])
        ):
            if _would_have_been_admitted(
                priority_score_cutoff=priority_score_cutoffs[applicant.ranking_sorted[rank]],
                priority_score=math.floor(applicant.priority_scores_sorted[rank])
            ):
                raise ValueError("The matching is not stable: an applicant could have been admitted to a more preferred contract")


def _would_have_been_admitted(priority_score_cutoff, priority_score):
    return priority_score >= priority_score_cutoff

def _get_least_preferred_rank_to_be_verified(applicant, assigned_contract_id):
    if assigned_contract_id == None:
        return len(applicant.ranking_sorted)

    return applicant.ranking_sorted.index(assigned_contract_id)
