#205. Isomorphic Strings
#Given two strings s and t, determine if they are isomorphic.Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping={}
        mapped_char=set()
        if len(s)!=len(t):
            return False
        for char_s,char_t in zip(s,t):
            if char_s in mapping:
                if mapping[char_s]!=char_t:
                    return False
            else:
                if char_t in mapped_char:
                    return False
                mapping[char_s]=char_t
                mapped_char.add(char_t)
        return True

if __name__=="__main__":
    solution=Solution()
    s="badc"
    t="kikp"
    first=solution.isIsomorphic(s,t)
    second=solution.isIsomorphic(t,s)
    print(first or second) 