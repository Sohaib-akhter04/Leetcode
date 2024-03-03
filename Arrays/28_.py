#28. Find the Index of the First Occurrence in a String

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        print(haystack.find(needle))

        


if __name__=="__main__":
    solution=Solution()
    haystack="sadbutsad"
    needle="sad"
    solution.strStr(haystack,needle)
