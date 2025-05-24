class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        highest = 0
        current = 0
        
        hashset = set(nums)

        for num in hashset:
            #we are at the start of a sequence
            if num - 1 not in hashset:
                current = 1
                contender = num
                highest = max(current, highest)
                while contender + 1 in hashset:
                    current +=1
                    highest = max(current,highest)
                    contender += 1

        return highest







    

        