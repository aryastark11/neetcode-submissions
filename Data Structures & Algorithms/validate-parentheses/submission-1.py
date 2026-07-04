class Solution:
    def isValid(self, s: str) -> bool:
        map1 = {']': '[', '}': '{', ')': '('}
        arr = []
        for i in range(len(s)):
            if s[i] in map1.values():
                arr.append(s[i])
            else:
                if arr and arr[-1] == map1[s[i]]:
                    arr.pop()
                else:
                    return False
        if arr:
            return False
        return True
