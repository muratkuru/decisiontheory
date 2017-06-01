"""
Author: Murat Kuru
Description: This class is about implementing Pierre LaPlace's the Average model with Python.
Python Version: 3.5.3
"""

from decisionbase import DecisionBase

class Laplace:
    def __init__(self, matrix):
        self.matrix = matrix

    def __getRatio(self):
        length = len(self.matrix[0])
        return float(1) / length

    def __getCalculationValues(self):
        ratio = self.__getRatio()
        calc = list(map(lambda x: ratio * sum(x), self.matrix))
        return calc
    
    def getResult(self, decisionBase):
        values = self.__getCalculationValues()
        if(decisionBase == DecisionBase.cost):
            result = min(values)
        elif(decisionBase == DecisionBase.benefit):
            result = max(values)
        index = [i for i, j in enumerate(values) if j == result]
        return { 'result': result, 'index': index }
