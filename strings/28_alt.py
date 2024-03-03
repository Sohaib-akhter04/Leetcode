class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack)<len(needle):
            return -1
        
        if not needle:
            return 0 
        

        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)]==needle:
                return i
        
        
        return -1






if __name__=="__main__":
    solution=Solution()
    haystack="sadbutsad"
    needle="sad"
    ans=solution.strStr(haystack,needle)
    print(ans)