class Applicant:
    """A class representing an applicant."""
    def __init__(self, applicant_id):
        self.applicant_id = applicant_id
        self.ranking = []
        self.priority_scores = []
        self.realized_admitted = None
