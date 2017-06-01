# Decision Theory
Implementing decision theory using Python
```
matrix format:

    N1  N2  N3  ...
S1  0   0   0
S2  0   0   0
S3  0   0   0
```
# Examples
```python
from plunger import Plunger
from wald import Wald
from laplace import Laplace
from savage import Savage
from decisionbase import DecisionBase


benefitMatrix = [[60000, 120000, 180000], [90000, 120000, 160000], [100000, 125000, 150000]]
costMatrix = [[2, 6, -3, 1], [7,4, 8, -2], [-6, -3, 5, 7]]

# Plunger Benefit Example
plungerBenefit = Plunger(benefitMatrix)
result = plungerBenefit.getResult(DecisionBase.benefit)
print(result) #{'result': 180000, 'index': [0]}

# Plunger Cost Example
plungerCost = Plunger(costMatrix)
result = plungerCost.getResult(DecisionBase.cost)
print(result) #{'result': -6, 'index': [2]}

# Wald Benefit Example
waldBenefit = Wald(benefitMatrix)
result = waldBenefit.getResult(DecisionBase.benefit)
print(result) #{'result': 100000, 'index': [2]}

# Wald Cost Example
waldCost = Wald(costMatrix)
result = waldCost.getResult(DecisionBase.cost)
print(result) #{'result': 6, 'index': [0]}

# Savage Benefit Example
savageBenefit = Savage(benefitMatrix)
result = savageBenefit.getResult(DecisionBase.benefit)
print(result) #{'index': [1], 'result': 20000}

# Savage Cost Example
savageCost = Savage(costMatrix)
result = savageCost.getResult(DecisionBase.cost)
print(result) #{'index': [0, 2], 'result': 9}

# Laplace Benefit Example
laplaceBenefit = Laplace(benefitMatrix)
result = laplaceBenefit.getResult(DecisionBase.benefit)
print(result) #{'index': [2], 'result': 125000.0}

#Laplace Cost Example
laplaceCost = Laplace(costMatrix)
result = laplaceCost.getResult(DecisionBase.cost)
print(result) #{'index': [2], 'result': 0.75}
```
