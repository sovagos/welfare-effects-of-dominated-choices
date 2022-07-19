from copy import deepcopy


class Applicant:
    """A class representing an applicant."""
    def __init__(self, applicant_id):
        self.applicant_id = applicant_id 
        self.ranking = []
        self.priority_scores = []
        self.realized_admitted = None
        self.dominated_dropping = None

    def add_dominated_dropping(self, dual_self_funded_program_dictionary, ranking):
        listed_dual_programs = {self_funded: state_funded for self_funded, state_funded in dual_self_funded_program_dictionary.items() if ((self_funded in [item[1] for item in ranking]) & (state_funded not in [item[1] for item in ranking]))}
        self.dominated_dropping = listed_dual_programs != {}

    def add_dominated_flipping(self, dual_self_funded_program_dictionary, ranking):
        listed_dual_programs = {self_funded: state_funded for self_funded, state_funded in dual_self_funded_program_dictionary.items() if ((self_funded in [item[1] for item in ranking]) & (state_funded in [item[1] for item in ranking]))}
        dominated_flipping = []
        for self_funded, state_funded in listed_dual_programs.items():
            ranking_state_funded = [item[0] for item in ranking if item[1] == state_funded]
            ranking_self_funded = [item[0] for item in ranking if item[1] == self_funded]
            dominated_flipping.append(ranking_self_funded < ranking_state_funded)
        self.dominated_flipping = any(dominated_flipping)

    def correct_dominated_dropping_lower_bound(self, ranking, priority_scores, dual_self_funded_program_dictionary):
        self.ranking_lower_bound = deepcopy(ranking)
        self.priority_scores_lower_bound = deepcopy(priority_scores)
        listed_dual_programs = {self_funded: state_funded for self_funded, state_funded in dual_self_funded_program_dictionary.items() if ((self_funded in [item[1] for item in ranking]) & (state_funded not in [item[1] for item in ranking]))}
        relevant_ranking = [item[0] for item in ranking if item[1] in listed_dual_programs.keys()]
        relevant_priority_scores = [[priority_score[0]- 0.5, priority_score[1]] for priority_score in priority_scores if priority_score[0] in relevant_ranking]
        self.priority_scores_lower_bound.extend(relevant_priority_scores)
        self.ranking_lower_bound.extend([list(ranking) for ranking in zip([x- 0.5 for x in relevant_ranking], list(listed_dual_programs.values()))])
        self.priority_scores_lower_bound.sort()
        self.ranking_lower_bound.sort()

    def correct_dominated_flipping_lower_bound(self, ranking, priority_scores, dual_self_funded_program_dictionary):
        listed_dual_programs = {self_funded: state_funded for self_funded, state_funded in dual_self_funded_program_dictionary.items() if ((self_funded in [item[1] for item in ranking]) & (state_funded in [item[1] for item in ranking]))}
        ranking_dict = {item[1]: item[0] for item in ranking}
        priority_scores_dict = {ps[0]: ps[1] for ps in priority_scores}
        for self_funded, state_funded in listed_dual_programs.items():
            top_rank = min(ranking_dict[self_funded], ranking_dict[state_funded])
            bottom_rank = max(ranking_dict[self_funded], ranking_dict[state_funded])
            ps_state_funded = priority_scores_dict[ranking_dict[state_funded]]
            ps_self_funded = priority_scores_dict[ranking_dict[self_funded]]
            priority_scores_dict[top_rank] = ps_state_funded
            priority_scores_dict[bottom_rank] = ps_self_funded
            ranking_dict[state_funded] = top_rank
            ranking_dict[self_funded] = bottom_rank
        self.ranking_lower_bound = [[rank, contract] for contract, rank in ranking_dict.items()]
        self.priority_scores_lower_bound = [[rank, priority_score] for rank, priority_score in priority_scores_dict.items()]
        self.ranking_lower_bound.sort()
        self.priority_scores_lower_bound.sort()
        

    def initialize_ranking(self, ranking, priority_scores):
        self.ranking_sorted = [x[1] for x in ranking]
        self.priority_scores_sorted = [x[1] for x in priority_scores]
