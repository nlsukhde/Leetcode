class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixArray = []
        suffixArray = []

        currProduct = 1
        for i in range(len(nums)):
            if i == 0:
                prefixArray.append(1)
                continue
            currProduct = currProduct * nums[i-1]
            prefixArray.append(currProduct)
        
        currProduct = 1
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                suffixArray.insert(0,1)
                continue
            currProduct = currProduct * nums[i+1]
            suffixArray.insert(0,currProduct)

        retval = []

        for i in range(len(nums)):
            retval.append(suffixArray[i] * prefixArray[i])

        return retval

        
        



       

        
 
        


        

       

        
 
        


        