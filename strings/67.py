#Given two binary strings a and b, return their sum as a binary string.


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # a=int(a,2)
        # b=int(b,2)
        
        return bin(int(a,2)+int(b,2))[2:]

if __name__=="__main__":
    solution=Solution()
    a="11"
    b="1"
    print(solution.addBinary(a,b))