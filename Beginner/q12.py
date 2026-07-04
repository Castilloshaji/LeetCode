#383. Ransom Note
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash={}
        for i in magazine:
            if i in hash:
                hash[i]+=1
            else:    
                hash[i]=1
        for i in ransomNote:
            if i not in hash or hash[i]==0:
                return False
            hash[i]-=1
        return True                
        