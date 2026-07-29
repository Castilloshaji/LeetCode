#643. Maximum Average Subarray I
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        add=sum(nums[:k])
        maxi=add
        for i in range(k,len(nums)):
            add=add-nums[i-k]+nums[i]
            maxi=max(maxi,add)

        return maxi/k    
       