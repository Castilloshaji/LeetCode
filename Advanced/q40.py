#4. Median of Two Sorted Arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge=nums1+nums2
        merge.sort()
        n=len(merge)
        if n%2==0:
            k=n//2
            j=merge[k]+merge[k-1]
            return j/2
        else:
            k=n//2
            return merge[k]

        