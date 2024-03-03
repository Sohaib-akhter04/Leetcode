# Given a string s consisting of words and spaces, 
#return the length of the last word in the string.A word is a maximal substring consisting of non-space characters only.
class Solution(object):
    def lengthOfLastWord(self,s):
        while s and s[-1]==' ':
            s=s[:-1]
        
        for i in range(len(s)-1,-1,-1):
            if s[i]==' ':
                return len(s)-i-1
            if i==0:
                return len(s)




if __name__=="__main__":
    solution=Solution()
    text="tool"
    print(solution.lengthOfLastWord(text))    