class Applicant:
    """A class representing an applicant."""
    def __init__(self, applicant_id):
        self.applicant_id = applicant_id 
        self.ranking = []
        self.priority_scores = []
        self.realized_admitted = None
        self.dominated_dropping = None
    def add_dominated_dropping(self, dual_self_funded_program_dictionary):
        listed_dual_programs = {self_funded: state_funded for self_funded, state_funded in dual_self_funded_program_dictionary.items() if ((self_funded in [ranking[1] for ranking in self.ranking]) & (state_funded not in [ranking[1] for ranking in self.ranking]))}
        self.dominated_dropping = listed_dual_programs != {}
    def add_dominated_flipping(self, dual_program_dictionary):
        dominated_flipping = []
        for pair in dual_program_dictionary.items():
            ranking_self_funded = [ranking[0] for ranking in self.ranking if ranking[1] == pair[1]]
            if len(ranking_self_funded) == 1:
                ranking_state_funded = [ranking[0] for ranking in self.ranking if ranking[1] == pair[0]]
                if len(ranking_state_funded) == 1:
                    dominated_flipping.append(ranking_state_funded[0] < ranking_self_funded[0])
        self.dominated_flipping = any(dominated_flipping)
    def correct_dominated_dropping_lower_bound(self, ranking, dual_self_funded_program_dictionary):
        self.ranking_lower_bound = ranking
        listed_dual_programs = {self_funded: state_funded for self_funded, state_funded in dual_self_funded_program_dictionary.items() if ((self_funded in [item[1] for item in ranking]) & (state_funded not in [item[1] for item in ranking]))}
        relevant_ranking = [item[0] - 0.5 for item in ranking if item[1] in listed_dual_programs.keys()]
        self.ranking_lower_bound.extend([list(ranking) for ranking in zip(relevant_ranking, list(listed_dual_programs.values()))])
