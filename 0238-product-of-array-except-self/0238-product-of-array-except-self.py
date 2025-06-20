class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        finalArray = [1] * len(nums)

        left = 1
        for i in range(len(nums)):

            finalArray[i] *= left
            left *= nums[i]


        right = 1
        for i in range(len(nums)-1,-1,-1):
            finalArray[i] *= right
            right *= nums[i]
        
        
        return finalArray



        