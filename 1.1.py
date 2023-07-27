'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        no_to_dictionary = {}
        for index,num in enumerate(nums):
            temp=target-num
            if temp in no_to_dictionary:
                return [no_to_dictionary[temp],index]
            no_to_dictionary[num]=index
        return []
    
# Example usage
if __name__ == "__main__":
    nums = [3,2,4]
    target = 6
    
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result)  # Output: [0, 1]
