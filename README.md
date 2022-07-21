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
