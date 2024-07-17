class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(needle) > len(haystack):
            return -1

        
        strlen = len(needle)

        for i in range(len(haystack)):
            j = i + strlen
            if haystack[i:j] == needle:
                return i
        
        return -1 

