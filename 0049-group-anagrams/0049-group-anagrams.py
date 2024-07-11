class Solution(object):
    def groupAnagrams(self, strs):

        #create a hashmap for anagram -> list of words it is an anagram of
        hashmap = {}


        for word in strs:
            sorted_chars = sorted(word)
            sorted_word = ''.join(sorted_chars)

            if sorted_word in hashmap:
                hashmap[sorted_word].append(word)
            else:
                hashmap[sorted_word] = list([word])
        
        ret_list = []

        for each_list in hashmap.values():
            ret_list.append(each_list)
        
        return ret_list


       

       

        
        