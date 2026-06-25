class Solution:
    def maxArea(self, heights: List[int]) -> int:
        totalWater = 0
        for i in range(0, len(heights)):
            water = 0
            for j in range(i+1, len(heights)):
                if heights[j] >= heights[i]:
                    water = heights[i]
                else:
                    water = heights[j]
                waterCollected = water * (j-i)
                #print(i, waterCollected)
                totalWater = max(totalWater, waterCollected)
        return totalWater