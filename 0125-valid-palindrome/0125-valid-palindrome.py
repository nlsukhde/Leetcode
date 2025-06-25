class Solution:
    def isPalindrome(self, s: str) -> bool:
        #convert the string to a list
        #remove all non alphanumeric characters
        #make every letter lower case

        original = list(s)
        cleaned = []

        for character in s:
            if character.isalnum():
                lowered = character.lower()
                cleaned.append(lowered)
        
        reversed_list = cleaned[::-1]
        
        if reversed_list == cleaned:
            return True
            
        return False

        