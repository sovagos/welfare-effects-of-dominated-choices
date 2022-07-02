from enum import unique
from python.applicant import Applicant

import pandas as pd

d = {
        'applicant_id': [1, 1, 1, 2, 2, 2, 3, 3, 3],
        'rank': [1, 2, 3, 1, 2, 3, 1, 2, 3],
        'program_id': [1, 1, 3, 1, 3, 3, 5, 3, 1],
        'state_funded': [1, 0, 0, 1, 0, 1, 1, 1, 1],
        'priority_score': [10, 10, 10, 10, 10, 10, 10, 10, 10],
        'admitted': [1, 0, 0, 0, 1, 0, 1, 0, 0]
    }
data = pd.DataFrame(data=d)
data["contract_id"] = data["program_id"] + (1 - data["state_funded"])

applicant_ids = data['applicant_id'].unique()
applicants = {}
for a in applicant_ids:
    applicant = Applicant(a)
    applicants[a] = applicant
    
n_rows = len(data)
for d in range(n_rows):
    applicant_id = data["applicant_id"][d]
    a = applicants[applicant_id]
    a.ranking.append([int(data["rank"][d]), data["contract_id"][d]])

for applicant_id in applicants:
    applicants[applicant_id].ranking.sort()
    applicants[applicant_id].ranking_sorted = [x[1] for x in applicants[applicant_id].ranking]

# Next steps: create contracts and programs


