# 168. Excel Sheet Column Title
# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        char=""
        temp=columnNumber
        while(temp>0):
            char=chr((temp-1)%26+ord('A'))+char
            temp=(temp-1)//26
        return char
        
# chr converts to char and ord converts to asci
if __name__=="__main__":
    solution=Solution()
    col_no=26
    print(solution.convertToTitle(col_no))

        



