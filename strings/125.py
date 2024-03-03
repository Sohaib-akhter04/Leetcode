class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned_s=''.join(char.lower() for char in s if char.isalnum())

        return cleaned_s==cleaned_s[::-1]


if __name__=="__main__":
    solution=Solution()
    text= "101"
    print(solution.isPalindrome(text))