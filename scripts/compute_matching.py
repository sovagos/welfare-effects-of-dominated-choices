from enum import unique
from python.applicant import Applicant

import pandas as pd

d = {
        'applicant_id': [1, 1, 1, 2, 2, 2, 3, 3, 3],
        'rank': [1, 2, 3, 1, 2, 3, 1, 2, 3],
        'program_id': [1, 1, 2, 1, 2, 2, 3, 2, 1],
        'funded': [1, 0, 0, 1, 0, 1, 1, 1, 1],
        'priority_score': [10, 10, 10, 10, 10, 10, 10, 10, 10],
    }
data = pd.DataFrame(data=d)

applicant_ids = data['applicant_id'].unique()
applicants = []
for a in applicant_ids:
    applicants[a] = Applicant(a)
    applicant = applicants[a]
    applicant.ranking = data[data['applicant_id'] == applicant.applicant_id]['program_id'].tolist()



