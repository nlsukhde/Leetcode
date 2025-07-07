class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #so we are going to loop through input nums
        #if we run into a number we havent already before
        #we start a contender state where we treat this number as the first triplet
        #and look for the next two that will add with it to equal 0 with the traditional two pointer approach method

        retval = []
        nums.sort()

        for i in range(len(nums) - 2):
            low = i + 1
            high = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = nums[i] * -1
            curList = []
            while low < high:
                if nums[low] + nums[high] < target:
                    low += 1
                elif nums[low] +nums[high] > target:
                    high -= 1
                else:
                    retval.append([nums[i],nums[low],nums[high]])
                    while low < high and nums[low + 1] == nums[low]:
                        low += 1
                    while low < high and nums[high -1] == nums[high]:
                        high -= 1
                    low += 1
                    high -= 1

        return retval





        