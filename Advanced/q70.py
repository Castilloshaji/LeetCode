#691. Stickers to Spell Word
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        sticker_count = [Counter(s) for s in stickers]

        @lru_cache(None)
        def dfs(rem):

            if rem == "":
                return 0

            target_count = Counter(rem)
            ans = float("inf")

            for sticker in sticker_count:

                # Optimization
                if rem[0] not in sticker:
                    continue

                new_rem = ""

                for ch in target_count:

                    left = target_count[ch] - sticker.get(ch, 0)

                    if left > 0:
                        new_rem += ch * left

                temp = dfs(new_rem)

                if temp != -1:
                    ans = min(ans, 1 + temp)

            return -1 if ans == float("inf") else ans

        return dfs(target)
        