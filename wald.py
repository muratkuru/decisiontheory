"""
Author: Murat Kuru
Description: This class is about implementing Wald's maximin model with Python.
Python Version: 3.5.3
"""

from decisionbase import DecisionBase

class Wald:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def __getMaximumValues(self):
        maximumValues = list(map(lambda x: max(x), self.matrix))
        return maximumValues

    def __getMinimumValues(self):
        minimumValues = list(map(lambda x: min(x), self.matrix))
        return minimumValues
    
    def getResult(self, decisionBase):
        if decisionBase == DecisionBase.cost:
            values = self.__getMaximumValues()
            result = min(values)
        elif decisionBase == DecisionBase.benefit:
            values = self.__getMinimumValues()
            result = max(values)
        index = [i for i, j in enumerate(values) if j == result]
        return { 'result': result, 'index': index }
