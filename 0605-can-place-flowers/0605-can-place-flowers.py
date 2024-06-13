class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        #calculate max number of plants that can be planted in the given 
        #flowerbed, if that number is greater of equal to n it is true

        currMax = 0 

        if n == 0:
            return True



        for i in range(len(flowerbed)):
            if len(flowerbed) == 1:
                if (flowerbed[i] == 0 and n == 1):
                    return True
                else:
                    return False
            if (i == 0): #first position
                if(flowerbed[i] == 0 and flowerbed[i + 1] == 0):
                    flowerbed[i] = 1
                    currMax += 1
            elif(i == len(flowerbed) - 1): #last position
                if(flowerbed[i] == 0 and flowerbed[i - 1] == 0):
                    flowerbed[i] = 1
                    currMax += 1
            else:
                if(flowerbed[i] == 0 and flowerbed [i + 1] == 0 and flowerbed[i - 1] == 0):
                    flowerbed[i] = 1
                    currMax += 1
    
        if currMax >= n:
            return True
        
        return False




                