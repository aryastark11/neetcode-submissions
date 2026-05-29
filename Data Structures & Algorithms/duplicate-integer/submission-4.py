class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setNums = list(set(nums))
        if len(setNums) == len(nums):
            return False
        return True

        