class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0

        dupeset = set()

        for r in range(len(s)):
            while(s[r] in dupeset):
                dupeset.remove(s[left])
                left += 1 
            dupeset.add(s[r])
            longest = max(longest, len(dupeset))
        
        return longest

       
            