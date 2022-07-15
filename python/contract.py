from python.config import CAPACITY_MIN, PRIORITY_SCORE_CUTOFF_MIN, CAPACITY_FACTOR
class Contract:
    """A class representing a contract."""
    def __init__(self, contract_id):
        self.contract_id = contract_id
        self.program_id = None
        self.state_funded = None
        self.ranking = []
        self.score_dictionary = {}
        self.capacity = 10**8
        self.total_admitted = 0
        self.priority_score_cutoff = None
    def add_capacity(self):
        if self.priority_score_cutoff == PRIORITY_SCORE_CUTOFF_MIN:
            self.capacity = max(self.total_admitted*CAPACITY_FACTOR, CAPACITY_MIN)
        else:
            self.capacity = self.total_admitted
