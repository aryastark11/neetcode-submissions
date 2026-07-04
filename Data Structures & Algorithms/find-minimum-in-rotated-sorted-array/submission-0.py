class Solution:
    def findMin(self, nums: List[int]) -> int:
        minN = nums[0]
        for i in range(1, len(nums)):
            minN = min(minN, nums[i])
        return minN
        """
        left = 0
        right = len(nums)-1
        mid =""" 

        