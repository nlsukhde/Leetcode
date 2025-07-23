class Solution:
    def trap(self, height: List[int]) -> int:

        leftmax = [0] * len(height)
        rightmax = [0] * len(height)

        curMax = 0
        for i in range(len(height)):
            leftmax[i] = max(height[i],curMax)
            curMax = max(height[i],curMax)

        curMax = 0
        for i in range(len(height)-1,-1,-1):
            rightmax[i] = max(height[i],curMax)
            curMax = max(height[i],curMax)
        water = 0

        for i in range(len(height)):
            curWater = min(leftmax[i],rightmax[i]) - height[i]
            water += curWater
    
        return water

    
        