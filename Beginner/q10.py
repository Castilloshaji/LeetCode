#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s)==sorted(t):
            return True
        else:
            return False    
        



#better solution
'''class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            s1 = set(s)
            for i in s1:
                if s.count(i) != t.count(i):
                    return False
            return True
            '''