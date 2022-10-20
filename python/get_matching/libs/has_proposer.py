from python.types import ApplicantsNew


def has_proposer(applicants: ApplicantsNew) -> bool:
    return len(applicants.proposer) > 0
