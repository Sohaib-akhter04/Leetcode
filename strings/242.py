#242. Valid Anagram
#Given two strings s and t, return true if t is an anagram of s, and false otherwise.An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map1={}
        map2={}
        for index,char_s in enumerate(s):
            if char_s in map1:
                map1[char_s]+=1
            else:
                map1[char_s]=1
        for index,char_t in enumerate(t):
            if char_t in map2:
                map2[char_t]+=1
            else:
                map2[char_t]=1
        if len(map1)!=len(map2):
            return False
        
        for key in map1:
            if key not in map2 or map1[key]!=map2[key]:
                return False
        return True

            


if __name__ == "__main__":
    solution=Solution()
    s = "rat"
    t = "car"
    print(solution.isAnagram(s,t))
