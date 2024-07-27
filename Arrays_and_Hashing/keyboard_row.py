class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = "qwertyuiop"
        second = "asdfghjkl"
        third = "zxcvbnm"

        hmap = {}
        res = []

        # fill in hashmap
        for char in first:
            hmap[char] = 1
        for char in second:
            hmap[char] = 2
        for char in third:
            hmap[char] = 3

        for word in words:
            word_lower = word.lower()
            i = 1
            fst_char_row = hmap[word_lower[0]]

            while i < len(word) and hmap[word_lower[i]] == fst_char_row:
                i += 1
            
            if i == len(word):
                res.append(word)
        
        return res
