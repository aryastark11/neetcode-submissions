from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        indexTrack = []
        for i in range(0, len(strs)-1):
            if i not in indexTrack:
                dict1[strs[i]] = []
                charList = list(strs[i])
                for j in range(i+1, len(strs)):
                    charList1 = list(strs[j])
                    if Counter(charList) == Counter(charList1):
                        dict1[strs[i]].append(strs[j])
                        indexTrack.append(j)
        if len(strs)-1 not in indexTrack:
            dict1[strs[-1]] = []
        list2 = []
        for k,v in dict1.items():
            x = [k] + v
            if list2:
                list2.append(x)
            else:
                list2 = [x]
        return list2