class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        highest = 1
        current = 1
        j = 0
        
        if(len(nums) == 0):
            return 0
        elif(len(nums) == 1):
            return 1
        print(nums)
        for i in range(1,len(nums)):
            print(str(nums[i]))
            print(str(1 + nums[j]))
            if(nums[i] == 1 + nums[j]):
                current += 1
                highest = max(highest, current)
            elif(nums[i] == nums[j]):
                pass
            else:
                current = 1
            
            j += 1
        
        return highest

        