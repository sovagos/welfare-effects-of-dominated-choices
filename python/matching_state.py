from copy import deepcopy


class MatchingState:
    """A helper class for representing current state of SPDA."""
    def __init__(self, applicants, contracts):
        self.temp_mu = {}
        self.cutoffs = {}
        for contract_id in contracts:
            self.temp_mu[contract_id] = []
            self.cutoffs[contract_id] = -1000
        self.proposers = {(applicant_id, applicants[applicant_id]) for applicant_id in applicants if len(applicants[applicant_id].ranking) > 0}
        self.curr_inds = {}
        for ssid in self.proposers: self.curr_inds[ssid[0]] = 0

    def copy(self):
        ret = MatchingState(set(), set())
        ret.temp_mu = deepcopy(self.temp_mu)
        ret.cutoffs = self.cutoffs.copy()
        ret.proposers = self.proposers.copy()
        ret.curr_inds = self.curr_inds.copy()
        return ret
