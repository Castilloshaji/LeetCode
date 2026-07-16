#875. Koko Eating Bananas
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        ans=high
        while low<=high:
            mid=(low+high)//2
            hi=0

            for i in piles:
                hi+=(i+mid-1)//mid
            if hi<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans                



        