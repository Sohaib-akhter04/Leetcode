# 290. Word Pattern
#Topics Companies Given a pattern and a string s, find if s follows the same pattern.Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """



if __name__=="__main__":
    solution=Solution()
    pattern="abba"
    s="dog cat cat dog"
    print(solution.wordPattern(pattern,s))