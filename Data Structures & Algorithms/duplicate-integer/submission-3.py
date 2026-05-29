class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list1 = list(set(nums))
        if len(list1) != len(nums):
            return True
        return False
        