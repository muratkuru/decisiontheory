"""
Author: Murat Kuru
Description: This class is about implementing Optimistic maximax model with Python.
Python Version: 3.5.3
"""

from decisionbase import DecisionBase

class Plunger:
    def __init__(self, matrix):                 
        self.__matrix = matrix
    
    def __getMaximumValues(self):
        return list(map(lambda x: max(x), self.__matrix))

    def __getMinimumValues(self):
        return list(map(lambda x: min(x), self.__matrix))
    
    def getResult(self, decisionBase):
        if decisionBase == DecisionBase.cost:
            values = self.__getMinimumValues()
            result = min(values)
        elif decisionBase == DecisionBase.benefit:
            values = self.__getMaximumValues()
            result = max(values)
        index = [i for i, j in enumerate(values) if j == result]
        return { 'result': result, 'index': index }
