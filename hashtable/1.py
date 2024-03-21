#1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.You may assume that each input would have exactly one solution, and you may not use the same element twice.You can return the answer in any order.


class Solution(object):
    def twoSum(self,nums,target):
        map={}
        result=[]
        for index,num in enumerate(nums):
            complement=target-num
            if complement in map:
                result.append(map[complement])
                result.append(index)
                return result
            map[num]=index
        return []






if __name__=="__main__":
    solution=Solution()
    nums=[2,7,11,15]
    target=9
    print(solution.twoSum(nums,target))