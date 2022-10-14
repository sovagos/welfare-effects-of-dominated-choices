from python.get_matching.libs.is_proposer import is_proposer
from python.types import Applicants, Applicant
from python.libs.find import find


def get_next_proposer(applicants: Applicants) -> Applicant:
    return find(is_proposer, list(applicants.values()))
