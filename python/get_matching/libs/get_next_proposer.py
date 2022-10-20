from python.types import Applicant, ApplicantsNew


def get_next_proposer(applicants: ApplicantsNew) -> Applicant:
    return applicants.proposer[0]
