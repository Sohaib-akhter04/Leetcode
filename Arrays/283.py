# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        non_zero_index=0
        for index in range(len(nums)):
            if nums[index]!=0:
                nums[index], nums[non_zero_index] = nums[non_zero_index], nums[index]
                non_zero_index+=1
        print(nums)




if __name__=="__main__":
    solution=Solution()
    nums=[1,3,0,0,2,0]
    solution.moveZeroes(nums)