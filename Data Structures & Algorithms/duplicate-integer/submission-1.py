class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        visited_nums = set()
        for num in nums:
            if num in visited_nums:
                return True
            visited_nums.add(num)
        return False 