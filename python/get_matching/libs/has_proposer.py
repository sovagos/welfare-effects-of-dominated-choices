from python.get_matching.libs.is_proposer import is_proposer
from python.types import Applicants
from python.libs.find import find


def has_proposer(applicants: Applicants) -> bool:
    return find(is_proposer, list(applicants.values())) is not None
