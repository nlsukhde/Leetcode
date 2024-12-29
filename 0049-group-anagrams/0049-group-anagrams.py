class Solution(object):
    def groupAnagrams(self, strs):

        #map of sortedWOrd -> list of words that when sorted are equal to sorted word

        wordMap = {}

        for word in strs:
            sortedWord = ''.join(sorted(word))
            wordMap[sortedWord] = []
        
        for word in strs:
            sortedWord = ''.join(sorted(word))

            if sortedWord in wordMap:
                wordMap[sortedWord].append(word)

        retval = []

        for value in wordMap.values():
            retval.append(value)

        return retval      
        