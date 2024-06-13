class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pointer1 = 0
        pointer2 = 1

        
        while ((nums[pointer1] + nums[pointer2]) != target):
            if pointer2 < len(nums) -1:
                pointer2 += 1 
            else:
                pointer1 += 1
                pointer2 = pointer1 + 1

        

        return [pointer1,pointer2]
        