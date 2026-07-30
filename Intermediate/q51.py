#131. Palindrome Partitioning
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []

        def isPalindrome(sub):
            return sub == sub[::-1]

        def backtrack(start):

            if start == len(s):
                ans.append(path[:])
                return

            for end in range(start, len(s)):

                curr = s[start:end + 1]

                if isPalindrome(curr):
                    path.append(curr)
                    backtrack(end + 1)
                    path.pop()

        backtrack(0)

        return ans
        