class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        #sort the array
        #loop through in twos 
        #keep adding the max

        sum = 0
        nums.sort()

        for i in range(0,len(nums),2):
            themin = min(nums[i],nums[i+1])
            sum += themin
        
        return sum


        