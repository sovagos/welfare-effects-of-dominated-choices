from python.types import Applicants, Applicant


def get_admitted_applicant(applicants: Applicants, applicant_id: str) -> Applicant:
    return applicants.admitted[applicant_id]
