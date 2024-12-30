class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqMap = {}

        for num in nums:
            if num in freqMap:
                freqMap[num] += 1
            else:
                freqMap[num] = 1
        
        sortedMap = sorted(freqMap.items(), key = lambda item: item[1], reverse=True)

        retval = []

        for i in range(k):
            retval.append(sortedMap[i][0])
        
        return retval


        
        
        



        

        