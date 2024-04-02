from typing import List

'''Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_nums=[num for num in nums if num!=val]
        nums[:]=new_nums
        return len(nums)


if __name__ == '__main__':
    solution=Solution()
    nums=[1,2,3,4,5,6,7]
    val=2
    result=solution.removeElement(nums,val)
    print(result)
