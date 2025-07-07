class Solution:
    def maxArea(self, height: List[int]) -> int:

        #Input: height = [1,7,2,5,4,7,3,6]
        # Output: 36

        l = 0
        r = len(height) - 1

        maxArea = 0

        while l < r:
            width = r - l
            h = min(height[r],height[l])
            area = width * h
            maxArea = max(area,maxArea)
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1
                r -= 1
        
        return maxArea

            

        