class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #do one pass over the array and make a left product and right product array
        
        left = []
        right = []

        curProduct = 1
        for i in range(len(nums)):
            left.append(curProduct)
            curProduct *= nums[i]
        
        curProduct = 1
        for i in range(len(nums)-1,-1,-1):
            right.append(curProduct)
            curProduct *= nums[i]
        
        reverse = right[::-1]
        
        output = []
        for i in range(len(nums)):
            output.append(reverse[i] * left[i])
        

        return output

