class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        for word in strs:
            word1 = "".join(sorted(word))
            if word1 not in dict1:
                dict1[word1] = []
            dict1[word1].append(word)
        return list(dict1.values())

        