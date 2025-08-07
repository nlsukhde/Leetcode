class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)

        while left <= right:
            mid = (right + left)//2

            hoursLeft = h
            for i in range(len(piles)):
                hoursEating = math.ceil(piles[i]/mid)
                hoursLeft -= hoursEating
            
            if hoursLeft < 0:
                left = mid + 1
            else:
                right = mid -1
        
        return left
            

                
                
                



            

        