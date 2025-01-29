class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curMax = 0
        lenCounter = 1
        nums.sort()
        
        print(nums)
        for i in range(len(nums)-1):
            currentNum = nums[i]
            nextNum = nums[i + 1]
            
            if nextNum == currentNum + 1:
                lenCounter += 1
            elif nextNum == currentNum:
                pass
            else:
                lenCounter = 1 
        
            if lenCounter > curMax:
                curMax = lenCounter

        if len(nums) == 1:
            return 1

        print(lenCounter)
        return curMax

            
