class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #build a hashmap of sortedword -> list of anagrams

        hashmap = {}

        for string in strs:
            sortedW = ''.join(sorted(string)) 

            if sortedW in hashmap:
                hashmap[sortedW].append(string)
            else:
                hashmap[sortedW] = [string]
        
        retval = []

        for group in hashmap.values():
            retval.append(group)
        
        return retval
