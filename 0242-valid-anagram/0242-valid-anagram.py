class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        smap = {}
        tmap = {}

        for letter in s:
            if letter in smap:
                smap[letter] += 1
            else:
                smap[letter] = 1
        
        for letter in t:
            if letter in tmap:
                tmap[letter] += 1
            else:
                tmap[letter] = 1

        if smap == tmap:
            return True
        
        return False
        

        
        