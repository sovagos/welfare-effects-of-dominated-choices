from copy import deepcopy
class MatchingState:
    """A helper class for representing current state of SPDA."""
    def __init__(self, applicants, contracts):
        self.temporary_allocation = {}
        self.cutoffs = {}
        for contract_id in contracts:
            self.temporary_allocation[contract_id] = []
            self.cutoffs[contract_id] = 0
        self.proposers = {(applicant_id, applicants[applicant_id]) for applicant_id in applicants if len(applicants[applicant_id].ranking) > 0}
        self.current_index = {}
        for applicant_id in self.proposers: 
            self.current_index[applicant_id[0]] = 0

    def copy(self):
        matching_state = MatchingState(set(), set())
        matching_state.temporary_allocation = deepcopy(self.temporary_allocation)
        matching_state.cutoffs = self.cutoffs.copy()
        matching_state.proposers = self.proposers.copy()
        matching_state.current_index = self.current_index.copy()
        return matching_state
