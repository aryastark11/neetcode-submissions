class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in s:
            countInS = s.count(i)
            if i in t:
                countInT = t.count(i)
                if countInS != countInT:
                    return False
            else:
                return False
        return True
        
        