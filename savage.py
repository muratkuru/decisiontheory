"""
Author: Murat Kuru
Description: This class is about implementing Savage Minimax Regret model with Python.
Python Version: 3.5.3
"""

from decisionbase import DecisionBase

class Savage:
    def __init__(self, matrix):
        self.__matrix = matrix

    def __getRegretMatrix(self, decisionBase):
        columnLength = len(self.__matrix[0])
        rowLength = len(self.__matrix)
        regretMatrix = [[0 for i in range(columnLength)] for j in range(rowLength)]
        for i in range(columnLength):
            columnCells = [column[i] for column in self.__matrix]
            if(decisionBase == DecisionBase.benefit):
                maxColumnValue = max(columnCells)
                result = list(map(lambda x: maxColumnValue - x, columnCells))
            elif(decisionBase == DecisionBase.cost):
                minColumnValue = min(columnCells)
                result = list(map(lambda x: x - minColumnValue, columnCells))
            for j in range(rowLength):
                regretMatrix[j][i] = result[j]
        return regretMatrix

    def getResult(self, decisionBase):
        regretMatrix = self.__getRegretMatrix(decisionBase)
        values = list(map(lambda x: max(x), regretMatrix))
        result = min(values)
        index = [i for i, j in enumerate(values) if j == result]
        return { 'result': result, 'index': index }
