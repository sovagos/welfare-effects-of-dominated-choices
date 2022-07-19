# welfare-effects-of-dominated-choices
This repo computes the welfare effect of dominated choices in Hungarian college admission

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
