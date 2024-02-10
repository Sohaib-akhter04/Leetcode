#Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_indices={}

        for index,num in enumerate(nums):
            if num in num_indices and index-num_indices[num]<=k:
                return True
            num_indices[num]=index
        return False
            



if __name__=="__main__":
    solution=Solution()
    nums = [1,0,1,1]
    k = 1
    print(solution.containsNearbyDuplicate(nums,k))