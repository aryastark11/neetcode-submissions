class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''.join(s.split(' '))
        s2 = ''.join(char for char in s1 if char.isalnum())
        print(s2)
        i = 0; j = len(s2)-1
        if (len(s2)%2 == 1):
            limit = int(len(s2)/2) + 1
        else:
            limit = int(len(s2)/2)
        for k in range(0, limit):
            if s2[i].lower() == s2[j].lower():
                i = i+1
                j = j-1
                continue
            else:
                return False
        return True
        