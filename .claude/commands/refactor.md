\---



description: Refactor a file with a stated goal while keeping behaviour identical

argument-hint: \[file] \[goal]

\----------------------------



Refactor $1 with this goal: $2



Constraints:



\* Behaviour must not change.

\* Public function names must stay the same.

\* Every existing test must still pass, unmodified.

\* Do not add dependencies.



First inspect the relevant code and tests.



Then show me a concise refactoring plan explaining:



1\. What you intend to change.

2\. Which functions/files will be affected.

3\. Why behaviour will remain unchanged.

4\. How you will verify the change.



Do not change anything until I approve the plan.



