class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = {}
        
        for word in strs:
            if "".join(sorted(word)) in anagrams:
                anagrams["".join(sorted(word))].append(word)
            else:
                anagrams["".join(sorted(word))] = [word]
        
        return [anagrams[key] for key in anagrams.keys()]


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        checked = set()
        
        for l in range(len(strs)):
            if strs[l] in checked:
                continue

            anagram = [strs[l]]
            checked.add(strs[l])

            for r in strs[l+1:]:
                if len(r) != len(strs[l]): continue
                if sorted(r) == sorted(strs[l]):
                    anagram.append(r)
                    checked.add(r)
            
            result.append(anagram)
        
        return result
