# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
from typing import List

class Solution():
    def generate(self,numRows:int)->List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        prevRows=self.generate(numRows-1)
        newRows=[1]*numRows
        
        for i in range(1,numRows-1):
            newRows[i]=prevRows[-1][i]+prevRows[-1][i-1]
        
        prevRows.append(newRows)
        return prevRows

if __name__ == "__main__":
    solution=Solution()
    result=solution.generate(5)
    print(result)