#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.


class Solution(object):
    def isPalindrome(self,s):
        cleaned_s="".join(char.lower() for char in s if char.isalnum())
        return cleaned_s==cleaned_s[::-1]



if __name__=="__main__":
    solution=Solution()
    text="race a car"
    print(solution.isPalindrome(text))