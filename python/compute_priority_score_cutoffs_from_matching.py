
def compute_priority_score_cutoffs_from_matching(matching, contracts):
    priority_score_cutoffs = {}
    for contract in contracts.values():
        priority_scores_of_admitted_applicants = [priority_score for applicant_id, priority_score in contract.score_dictionary.items() if matching[applicant_id] == contract.contract_id]
        priority_score_cutoffs[contract.contract_id] = 0 if priority_scores_of_admitted_applicants == [] else min(priority_scores_of_admitted_applicants)
    return priority_score_cutoffs