from heapq import heappop, heappush
import random
from python.config import PRIORITY_SCORE_CUTOFF_MIN
from python.matching_state import MatchingState

def summarize_dominated_choices(applicants):
    dominated_dropping = 0
    dominated_flipping = 0
    dominated_choice = 0
    for applicant in applicants.values():
        dominated_dropping += int(applicant.dominated_dropping)
        dominated_flipping += int(applicant.dominated_flipping)
        dominated_choice += int(any([applicant.dominated_dropping, applicant.dominated_flipping]))
    print(f"Share of applicants with dominated dropping: {dominated_dropping/len(applicants)}")
    print(f"Share of applicants with dominated flipping: {dominated_flipping/len(applicants)}")
    print(f"Share of applicants with dominated choices: {dominated_choice/len(applicants)}")

def STB(applicants, seed = 1000):
    """Run single tie-breaking."""
    random.seed(seed)
    random_tiebreaker = {applicant_id : random.random() for applicant_id in applicants}
    for applicant in applicants.values():
        applicant.priority_scores_sorted = [priority_score + random_tiebreaker[applicant.applicant_id] for priority_score in applicant.priority_scores_sorted]

def student_proposing_deferred_acceptance(applicants, contracts):
    """Run Student-Proposing Deferred Acceptance."""
    matching_state = MatchingState(applicants, contracts)
    temporary_allocation = matching_state.temporary_allocation
    cutoffs = matching_state.cutoffs
    proposers = matching_state.proposers
    current_index = matching_state.current_index
    while len(proposers) > 0:
        applicant_id, applicant = proposers.pop()
        contract_id = applicant.ranking_sorted[current_index[applicant_id]]
        # Rejected applicant
        while (contracts[contract_id].score_dictionary[applicant_id] < cutoffs[contract_id]) | (contracts[contract_id].score_dictionary[applicant_id] < float(PRIORITY_SCORE_CUTOFF_MIN)):
            current_index[applicant_id] += 1
            if current_index[applicant_id] == len(applicant.ranking_sorted):
                contract_id = None
                break
            contract_id = applicant.ranking_sorted[current_index[applicant_id]]
        if contract_id == None: continue
        # Update assignment
        heappush(temporary_allocation[contract_id], (contracts[contract_id].score_dictionary[applicant_id], applicant_id))
        if len(temporary_allocation[contract_id]) > contracts[contract_id].capacity:
            min_s = heappop(temporary_allocation[contract_id])
            applicant_id_out = min_s[1]
            current_index[applicant_id_out] += 1
            if current_index[applicant_id_out] < len(applicants[applicant_id_out].ranking_sorted):
                proposers.add((applicant_id_out, applicants[applicant_id_out]))
            cutoffs[contract_id] = min_s[0] + 10**(-10)  
    matching = {applicant_id : None for applicant_id in applicants}
    for contract_id in temporary_allocation:
        for sc_applicant_id in temporary_allocation[contract_id]:
            applicant_id = sc_applicant_id[1]
            matching[applicant_id] = contract_id
    return matching
