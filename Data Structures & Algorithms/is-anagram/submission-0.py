class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = 0
        
        unique_S = set(s[::])
        for i in unique_S:
            print(i)
            countOfI_s = s.count(i)
            print(countOfI_s)
            countOfI_t= t.count(i)
            print(countOfI_t)
            if countOfI_s != countOfI_t:
                return False
        return True

