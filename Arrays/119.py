'''Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:'''
from typing import List

class Solution:
    def generate(self, rowIndex: int) -> List[List[int]]:
        result=[]
        if rowIndex == 0:
            return [1]
        first_Row=[1]
        result.append(first_Row)
        for i in range(1,rowIndex+1):
            currentRow=[1]
            prevRow=result[i-1]
            for j in range(1,i):
                currentRow.append(prevRow[j]+prevRow[j-1])
            currentRow.append(1)
            result.append(currentRow)
        return result[rowIndex]