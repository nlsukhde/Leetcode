class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        count = 0
        retval = 0

        for i in range(len(nums)):
            if nums[i] == val:
                count += 1
            else:
                retval += 1
        for i in range(count):
            nums.remove(val)
        
        return retval