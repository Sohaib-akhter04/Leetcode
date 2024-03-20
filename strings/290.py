# 290. Word Pattern
#Topics Companies Given a pattern and a string s, find if s follows the same pattern.Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words=s.split()
        # print(words)
        mapping={}
        mapped_words=set()
        if len(words)!=len(pattern):
            return False
        for word,char_s in zip(words,pattern):
            if char_s in mapping:
                if mapping[char_s]!=word:
                    return False
            else:
                if word in mapped_words:
                    return False
                mapping[char_s]=word
                mapped_words.add(word)
        return True



            

       

if __name__=="__main__":
    solution=Solution()
    pattern="abba"
    s="dog cat ca dog"
    print(solution.wordPattern(pattern,s))