class Applicant:
    """A class representing an applicant."""
    def __init__(self, applicant_id):
        self.applicant_id = applicant_id 
        self.ranking = []
        self.priority_scores = []
        self.realized_admitted = None
        self.dominated_dropping = None
    def add_dominated_dropping(self, dual_program_dictionary):
        listed_self_funded_contracts = [x for x in [ranking[1] for ranking in self.ranking] if x in dual_program_dictionary.keys()]
        self.dominated_dropping = not set([dual_program_dictionary[contract_id] for contract_id in listed_self_funded_contracts]).issubset(set([ranking[1] for ranking in self.ranking]))
