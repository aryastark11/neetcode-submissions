class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)-1):
            newNums = nums[i+1:]
            requiredJ = target-nums[i]
            if requiredJ in newNums:
                j = newNums.index(requiredJ)
                return [i,j+i+1]
       