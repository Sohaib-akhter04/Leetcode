'''You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.'''


from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        carry=1
        for i in range(n-1,-1,-1):
            total=carry+digits[i] #4
            digits[i]=total%10 #4
            carry=total//10
        if carry:
            digits.insert(0,carry)
        return digits
# its simple basically humne total calculate kra or uska mod save kradiya digits[i] me agr 10 ya 10 se bara hota tou waha pr ajata lkn or phir humne mod save kradiya digits[i] me or carry divide by 10 se krlia take carry bit usi lihaz se right wale pe add ho

if __name__ == '__main__':
    nums=[1,2,3]
    solution=Solution()
    result=solution.plusOne(nums)
    print(result)