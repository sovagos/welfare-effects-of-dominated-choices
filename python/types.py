from dataclasses import dataclass, field
from enum import Enum


class ApplicantStatusType(Enum):
    INIT = "init"
    ADMITTED = "admitted"
    REJECTED = "rejected"


@dataclass
class InitialApplicantStatus:
    type: ApplicantStatusType = field(default=ApplicantStatusType.INIT, init=False)


@dataclass
class AdmittedApplicantStatus:
    type: ApplicantStatusType = field(default=ApplicantStatusType.ADMITTED, init=False)
    rank: int


@dataclass
class RejectedApplicantStatus:
    type: ApplicantStatusType = field(default=ApplicantStatusType.REJECTED, init=False)
    rank: int


@dataclass
class Application:
    contract: str
    priority_score: float


@dataclass
class Applicant:
    id: str
    ranked_applications: list[Application]
    status: InitialApplicantStatus | AdmittedApplicantStatus | RejectedApplicantStatus


@dataclass
class AdmittedApplicant:
    applicant_id: str
    priority_score: float


@dataclass
class Contract:
    id: str
    capacity: int
    admitted_applicants: list[AdmittedApplicant]


Applicants = dict[str, Applicant]
Contracts = dict[str, Contract]


@dataclass
class ContractWithScore:
    id: str
    score: int

@dataclass
class Input:
    contracts: list[Contract]
    applicants: list[Applicant]
