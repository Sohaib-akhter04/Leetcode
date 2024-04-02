'''Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.'''


from typing import List

class Solution:
    def removeDuplicates(self,nums:List[int])->int:
    #    [1,1,2,2,3,4]=>[1,1,2,3,4]=>[1,2,2,3,4]=>[1,2,3,3,4]=>[]
        j=1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[j]=nums[i]
                j+=1
        return j

if __name__=='__main__':
    nums=[1,1,2]
    solution=Solution()
    result=solution.removeDuplicates(nums)
    count_map={}
    result2=[]
    print(result)

    # 
    count_map = {}
    num = [1, 1, 2]
    result2 = []
    
    # Initialize count_map with zeros for each unique element in num
    for element in num:
        count_map[element] = 0
    
    # Count occurrences of each element
    for element in num:
        count_map[element] += 1
    
    # Find elements with count less than 1
    for key in count_map:
        if count_map[key] == 1:
            result2.append(key)
    
    print(result2)

