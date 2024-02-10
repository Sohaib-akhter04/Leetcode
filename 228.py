class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        
        ranges=[]
        start=nums[0]
        end=nums[0]


        for i in range(1,len(nums)):
            if nums[i]==end+1: #7==6+1
                end=nums[i]
            else:
                if start==end:
                    ranges.append(str(end))
                else:
                    ranges.append(str(start)+"->"+str(end))
                start=nums[i] # 7
                end=nums[i] # 7
        if start==end:
            ranges.append(str(end))
        else:
            ranges.append(str(start)+"->"+str(end))
        return ranges




if __name__ == "__main__":
    solution = Solution()
    nums = [0, 1, 2, 4, 6, 7]
    print(solution.summaryRanges(nums))
