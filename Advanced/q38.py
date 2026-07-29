#2659. Make Array Empty
class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        n = len(nums)

        bit = [0] * (n + 1)

        def update(i, val):
            i += 1
            while i <= n:
                bit[i] += val
                i += i & -i

        def query(i):
            s = 0
            i += 1
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        for i in range(n):
            update(i, 1)

        arr = sorted((v, i) for i, v in enumerate(nums))

        ans = 0
        prev = 0

        for _, idx in arr:
            if idx >= prev:
                ans += query(idx) - query(prev - 1)
            else:
                ans += query(n - 1) - query(prev - 1)
                ans += query(idx)

            update(idx, -1)
            prev = idx

        return ans