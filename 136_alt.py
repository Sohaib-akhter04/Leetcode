#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num
        return result
        

if __name__ == '__main__':
    solution=Solution()
    nums = [4,1,2,2]
    key=solution.singleNumber(nums)
    print(key)