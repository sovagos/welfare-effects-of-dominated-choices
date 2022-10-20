from python.types import Applicants


def has_proposer(applicants: Applicants) -> bool:
    return len(applicants.proposer) > 0
