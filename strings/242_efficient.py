#242. Valid Anagram
#Given two strings s and t, return true if t is an anagram of s, and false otherwise.An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        for w in set(s):
            if s.count(w)!=t.count(w):
                return False
        return True

            


if __name__ == "__main__":
    solution=Solution()
    s = "rat"
    t = "car"
    print(solution.isAnagram(s,t))
