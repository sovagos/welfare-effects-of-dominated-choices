from python.algorithm.applicant import Applicant
from python.algorithm.is_proposer import is_proposer


def get_next_proposer(applicants: list[Applicant]) -> Applicant:
    for applicant in applicants:
        if is_proposer(applicant=applicant):
            return applicant
