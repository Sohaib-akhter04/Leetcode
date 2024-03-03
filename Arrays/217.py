# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dictionary={}
        for index,element in enumerate(nums):
            if element in dictionary:
                return True
            else:
                dictionary[element]=1
        
        return False

if __name__=="__main__":
    solution=Solution()
    nums=[1,2,3]
    print(solution.containsDuplicate(nums))