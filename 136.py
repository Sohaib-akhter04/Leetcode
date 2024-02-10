#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space. optimal approach
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dictionary={}
        filtered_dict={}
        array=[]
        for i, element in enumerate(nums):
             if element in dictionary:
                dictionary[element] += 1
             else:
                dictionary[element] = 1
        for key, value in dictionary.items():
            if value == 1:
                filtered_dict[key] = value
        for key,value in filtered_dict.items():
            array.append(key)
        return key

if __name__ == '__main__':
    solution=Solution()
    nums = [4,1,2,1,2]
    key=solution.singleNumber(nums)
    print(key)