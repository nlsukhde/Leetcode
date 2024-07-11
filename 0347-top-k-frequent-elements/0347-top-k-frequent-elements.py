class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #make a frequency map
        #sort by the maps's value
        #add to list and return it

        freq_map = {}
        
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1 
            else:
                freq_map[num] = 1 

        #now we have map with frequencys

        sorted_keys = sorted(freq_map, key=freq_map.get, reverse=True)

        #now we have a list of the keys in the map from hightest to loweset freqs


        #RETURN the first k elements
        ret_list = sorted_keys[:k]

        return ret_list
        
        
        



        

        