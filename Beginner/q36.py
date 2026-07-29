#859. Buddy Strings
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            seen = set()

            for ch in s:
                if ch in seen:
                    return True
                seen.add(ch)

            return False

        diff = []

        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append((s[i], goal[i]))

        return len(diff) == 2 and \
               diff[0][0] == diff[1][1] and \
               diff[0][1] == diff[1][0]
        