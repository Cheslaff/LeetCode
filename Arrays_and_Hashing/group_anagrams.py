class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = {}
        
        for word in strs:
            if "".join(sorted(word)) in anagrams:
                anagrams["".join(sorted(word))].append(word)
            else:
                anagrams["".join(sorted(word))] = [word]
        
        return [anagrams[key] for key in anagrams.keys()]
