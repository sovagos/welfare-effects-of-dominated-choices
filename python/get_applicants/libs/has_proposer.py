from python.get_applicants.libs.is_proposer import is_proposer
from python.get_applicants.types import Applicants
from python.libs.find import find


def has_proposer(applicants: Applicants) -> bool:
    return find(is_proposer, list(applicants.values())) is not None
