from python.types import Applicant, Applicants


def get_next_proposer(applicants: Applicants) -> Applicant:
    return applicants.proposer[0]
