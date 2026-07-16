#128. Longest Consecutive Sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        curr=1
        lens=0
        for i in range(len(nums) - 1):

            if nums[i]==nums[i+1]:
                continue     

            elif nums[i]+1==nums[i+1]:
                curr+=1

            else:
                lens=max(lens,curr)
                curr=1
        return max(lens,curr)                      
        