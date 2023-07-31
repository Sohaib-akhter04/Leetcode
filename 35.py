
'''Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.'''
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s=0
        e=len(nums)
        if target>nums[e-1]:
            return e
        while s<=e:
            mid=(s+e)/2
            mid=int(mid)
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                e=mid-1
            else:
                s=mid+1
        return s




if __name__=='__main__':
    nums=[1,3]
    target=2
    solution=Solution()
    result = solution.searchInsert(nums,target)
    print(result)
