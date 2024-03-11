#171. Excel Sheet Column Number
#Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result=0
        for i in range(len(columnTitle)):
            result=result*26+(ord(columnTitle[i])-ord('A')+1)
        print(result)
        

if __name__ =="__main__":
    solution=Solution()
    char ="ZY"
    solution.titleToNumber(char)
   

