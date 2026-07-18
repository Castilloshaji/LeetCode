#20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        for i in s:
            if i=="(":
                stack.append(")")
            elif i=="[":
                stack.append("]")
            elif i=="{":
                stack.append("}")
            else:
                if not stack or stack.pop()!=i:
                    return False
        return not stack                        
        