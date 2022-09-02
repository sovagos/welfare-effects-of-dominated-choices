from python.algorithm.applicant import Applicant
from python.algorithm.is_proposer import is_proposer


def has_proposer(applicants: list[Applicant]) -> bool:
    return any(is_proposer(applicant) for applicant in applicants)
