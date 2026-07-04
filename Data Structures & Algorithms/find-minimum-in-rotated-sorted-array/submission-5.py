class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        BRUTE FORCE

        minN = nums[0]
        for i in range(1, len(nums)):
            minN = min(minN, nums[i])
        return minN
        """
        minNumber = 1001
        left = 0
        right = len(nums)-1
        
        while(left < right):
            mid = int((left + right) // 2)
            #fully sorted - ascending 
            # if nums[left] <= nums[mid] and nums[mid] <= nums[right]:
                # minNumber = min(minNumber,nums[left])
                # return nums[left]
                # break
            # 3 4 5 1 2
            # min is on the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            # 4 5 0 1 2
            else:
                right = mid
                # minNumber = nums[mid]
        return nums[left]





        