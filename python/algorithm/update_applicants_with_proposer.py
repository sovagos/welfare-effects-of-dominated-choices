from python.algorithm.applicant import Applicant


def update_applicants_with_proposer(
    applicants: list[Applicant], proposer: Applicant
) -> list[Applicant]:
    updated_applicants = []
    for applicant in applicants:
        if applicant.id == proposer.id:
            updated_applicants.extend([proposer])
        else:
            updated_applicants.extend([applicant])
    return updated_applicants
