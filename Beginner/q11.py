#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.Given a string s, return true if it is a palindrome, or false otherwise.

 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        c=""
        for i in s:
            if i.isalnum():
                c+=i.lower()
        if c==c[::-1]:
            return True
        return False        
        