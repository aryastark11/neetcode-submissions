class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # All 3 zeroes
        # 2 small positive numbers and 1 big negative number
        # 2 small negative numbers and 1 big positive number
        # 1 pos, 1 neg, 1 zero
        output = []
        nums.sort()
        i = 0;
        # -4, -1, -1, 0, 1, 2
        while i < len(nums)-2:
            if nums[i] == 0 and nums.count(0) > 2 and len(nums) == nums.count(0):
                output.append([0,0,0])
                break
            else:
                j = i + 1
                while j < len(nums)-1:
                    secNum = nums[j]
                    thirdNum = -1 * (secNum + nums[i])
                    if thirdNum in nums[j+1:]:
                        list1 = [nums[i], nums[j], thirdNum]
                        if list1 not in output:
                            output.append(list1)
                    j = j + 1
                i = i + 1
        return output