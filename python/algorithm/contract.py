from dataclasses import dataclass


@dataclass
class AdmittedApplicant:
    applicant_id: str
    priority_score: float


@dataclass
class Contract:
    id: str
    capacity: int
    admitted_applicants: list[AdmittedApplicant]
