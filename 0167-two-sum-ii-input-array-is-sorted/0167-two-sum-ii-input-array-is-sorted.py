class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #set a pointer for the beginning of list and end
        #while left < right
        # we will go through and see if the two numbers are greater than or less than target
        #if it is less than the target we increment left pointer so we get slightly bigger
        #if it is greater than the target we decrement right pointer so we get smaller

        left, right = 0, len(numbers)-1

        while left < right:
            currSum = numbers[left] + numbers[right]
            if currSum < target:
                left += 1
            elif currSum > target:
                right -= 1
            elif currSum == target:
                return [left+1,right+1]