class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        s=(n*(n+1))/2
        Sum=sum(nums)
        result=s-Sum
        return int(result)
        
if __name__ == "__main__":
    solution=Solution()
    nums=[3,0,2]
    solution.missingNumber(nums)