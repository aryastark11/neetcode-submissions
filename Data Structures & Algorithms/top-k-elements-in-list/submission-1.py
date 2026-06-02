class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        list1 = []
        dict1 = {}
        for i in nums:
            if i not in list(dict1.keys()):
                dict1[i] = nums.count(i)
        print(dict1)
        dict2 = dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True))
        list1 = list(dict2.keys())
        print(list1)
        return list1[:k]
        
        