# Given an integer array nums, handle multiple queries of the following type:
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:
# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).



class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums=nums

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        result=0
        if left<0 or right>=len(self.nums) or left>right:
            return 0
        return sum(self.nums[left:right+1])
    

if __name__=="__main__":
    nums = [1, 2, 3, 4, 5]
    numArray = NumArray(nums)
    print(numArray.sumRange(1, 3))