class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        leftArray = []
        rightArray = []

        product = 1
        for i in range(len(nums)):

            leftArray.append(product)
            product *= nums[i]


        product = 1
        for i in range(len(nums)-1,-1,-1):
            rightArray.insert(0,product)
            product *= nums[i]
        
        for i in range(len(nums)):
            leftArray[i] = leftArray[i] * rightArray[i]
        
        return leftArray



        