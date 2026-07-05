#347. Top K Frequent Elements
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            elif i in d:
                d[i]+=1
        arr=[]        
        for i in d:
            arr.append([d[i],i])

        arr.sort(reverse=True)
        a=[]
        for i in range(k):
            a.append(arr[i][1])

        return a    

