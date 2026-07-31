#68. Text Justification
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        i = 0
        n = len(words)

        while i < n:

            j = i
            length = 0

            while j < n and length + len(words[j]) + (j - i) <= maxWidth:
                length += len(words[j])
                j += 1

            spaces = maxWidth - length
            gaps = j - i - 1

            # Last line or single word
            if j == n or gaps == 0:

                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))

            else:

                even = spaces // gaps
                extra = spaces % gaps

                line = ""

                for k in range(i, j - 1):

                    line += words[k]

                    cnt = even
                    if extra > 0:
                        cnt += 1
                        extra -= 1

                    line += " " * cnt

                line += words[j - 1]

            ans.append(line)
            i = j

        return ans
        