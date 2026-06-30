class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # for each element in the string
        # check the next elements. if unique, add to the result. if repeated, stop
        # get the length of this new string formed. Track the max Length
        maxLength = 1
        if len(s) == 0:
            return 0
        for i in range(0, len(s)-1):
            list1 = [s[i]]
            for j in range(i+1, len(s)):
                if s[j] not in list1:
                    list1.append(s[j])           
                    maxLength = max(maxLength, len(list1))
                else:
                    break
        return maxLength