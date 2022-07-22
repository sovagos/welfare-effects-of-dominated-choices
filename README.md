# welfare-effects-of-dominated-choices
This repo computes the welfare effect of dominated choices in Hungarian college admission

# Summary
The Hungarian college admission market is an example of a matching-with-contracts markets: college applicants can apply to study programs with state-funding or self-funding options. Applicants are assigned to contracts by a centralized clearinghouse that uses a variant of the student-proposing Deferred Acceptance mechanism. 

Key steps:
  - Document the prevalence of dominated choices
  - Replicate baseline match
  - Correct dominated choices and compute a counterfactual match
  - Compare the counterfactual match to the baseline match
    - number of applicants assigned to college (total, self-funded, state-funded)
    - number of winners and losers

# Definitions

Applicant: college applicant with the following attributes:
  - applicant_id: integer, identifies the applicant
  - ranking: list of rank and contract id
  - priority_scores: list of rank and priority score

Contract:
  - contract_id: integer, identifies the contract (e.g., Economics at Corvinus University Budapest with state-funding)
  - program_id: integer: identifies the corresponding program (e.g., Economics at Corvinus University Budapest)
  - state_funded: Boolean, indicates whether a contract is state-funded (True) or slef-funded (False)
  
Program:
  - program_id: integer, identifies the program (e.g., Economics at Corvinus University Budapest)
  
 Dominated dropping:
  - An applicant ranks a self-funded contract, but does not rank the corresponding state-funded contract
  
Domnated flipping:
  - The applicant ranks the self-funded contract higher than the corresponding state-funded contract

# Example

| Applicant id | Ranking | Contract id | Program id | Priority score | State-funded |
| ------------ | ------- | ----------- | ---------- | -------------- | ------------ |
| 1            | 1       | 1           | A          | 10             | True         |
| 2            | 1       | 2           | A          | 11             | False        |
| 3            | 1       | 2           | A          | 12             | False        |
| 3            | 2       | 2           | A          | 12             | True         |

Capacities:
 - Contract 1: 1 spot
 - Contract 2: 1 spot

Dominated choices:
 - Applicant 2: dominated dropping, as (s)he do not rank the state-funded version of Program A
 - Applicant 3: dominated flipping, as (s)he ranks the self-funded version of Program A higher than the state-funded version of Program A

Benchmark matching: {Applicant: contract} = {1:1, 2:None, 3:2}   
Counterfactual matching (with no dominated choices): {Applicant: contract} = {1:None, 2:2, 3:1}   
Counterfactual matching (with no dominated flipping): {Applicant: contract} = {1:None, 2:2, 3:1}   
Counterfactual matching (with no dominated dropping): {Applicant: contract} = {1:None, 2:1, 3:2}   

## Number of applicants assigned to college
Benchmark matching: 2
Counterfactual matching (with no dominated choices): 2
Counterfactual matching (with no dominated flipping): 2
Counterfactual matching (with no dominated dropping): 2
## Winners and losers

| Comparison | Winner | Indifferent | Loser |
| --------------------------------------------------------------------------- | ------ | ----------- | ----- |
| Counterfactual matching (with no dominated choices) vs. Benchmark matching: | 2, 3   | None        | 1     |
| Counterfactual matching (with no dominated flipping) vs. Benchmark matching:| 2, 3 | None        | 1     |
| Counterfactual matching (with no dominated dropping) vs. Benchmark matching:| 2    | 3           | 1     |
