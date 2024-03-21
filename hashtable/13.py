#13. Roman to Integer
#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000

        }
        result=0
        for i in  range(len(s)):
            if i<len(s)-1 and map[s[i]]<map[s[i+1]]:
                result-=map[s[i]]
            else:
                result+=map[s[i]]
        return result



if __name__=="__main__":
    solution=Solution()
    s = "III"
    print(solution.romanToInt(s))