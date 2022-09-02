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
    ranked_applications: list[Application]
    status: InitialApplicantStatus | AdmittedApplicantStatus | RejectedApplicantStatus








class Applicant_old:

    def _init_(self, ranked_contracts):
        self._ranked_contracts = ranked_contracts
        self._admitted = None
        self._rejected = None

    def is_proposer(self):
        pass

    def set_admitted(self):
        pass

    def set_rejected(self):
        pass

    def get_next_application(self):
        pass