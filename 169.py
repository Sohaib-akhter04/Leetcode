class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dictionary={}
        n=len(nums)
        array=[]
        for index,element in enumerate(nums):
            if element in dictionary:
                dictionary[element]+=1
            else:
                dictionary[element]=1
        for key,value in dictionary.items():
            if value>n/2:
                return key



if __name__=="__main__":
    solution=Solution()
    nums=[3,3,4]
    solution.majorityElement(nums)