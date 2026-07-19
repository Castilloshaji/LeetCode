#198. House Robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        p=0
        c=0
        for i in nums:
            temp=c
            c=max(c,p+i)
            p=temp
        return c    
        