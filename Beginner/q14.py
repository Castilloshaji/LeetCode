#49. Group Anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            w="".join(sorted(i))
            if w not in d:
                d[w]=[]
            d[w].append(i)    

        return list(d.values())    