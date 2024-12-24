class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # [2,7,11,15]
        # 0 , 1, 2, 3
        pointer1 = 0
        pointer2 = 1

        while True:
            if nums[pointer1] + nums[pointer2] == target:
                return (pointer1,pointer2)
            if pointer2 == len(nums) - 1:
                pointer1 += 1
                pointer2 = pointer1 + 1
            else:
                pointer2 += 1

        