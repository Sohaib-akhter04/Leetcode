#345. Reverse Vowels of a String
#Given a string s, reverse only all the vowels in the string and return it.The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


class Solution(object):
    def reverseVowels(self,s):
        left=0
        right=len(s)-1
        vowels=['a','e','i','o','u']
        vowel_right=0
        s=list(s)
        vowel_left=0
        while(left<right):
            if s[left].lower() in vowels and s[right].lower() in vowels:
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
            elif s[left].lower() in vowels:
                right-=1
            elif s[right].lower() in vowels:
                left+=1
            else:
                left+=1
                right-=1
        return ''.join(s)




if __name__ =="__main__":
    solution=Solution()
    s="aA"
    print(solution.reverseVowels(s))
