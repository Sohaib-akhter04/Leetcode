# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
from typing import List
class Solution:
    def generate(self,numRows:int)->List[List[int]]:
        result=[]
        if numRows==0:
            return result
        first_row=[1]
        result.append(first_row)
        for i in range(1,numRows):#simple row wise iteration
            current_row=[1] #current row me 1 daldia pehle to then dekhege
            prev_row=result[i-1] #prev row me piche array k index k value dali
            for j in range(1,i): # catch idher aya k humne pichle wlae array k j or j-1 se access hoga
                current_row.append(prev_row[j]+prev_row[j-1])
            current_row.append(1)# last me append hona hai
            result.append(current_row)
        return result

if __name__=='__main__':
    solution=Solution()
    numRows=input('Enter num rows:')
    numRows=int(numRows)
    result=solution.generate(numRows)
    print(result)    
               

             
