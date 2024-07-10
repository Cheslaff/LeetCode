# naive approach
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# using hashing

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashmap = {}

        if len(s) != len(t):
            return False
            
        for i in range(len(s)):
            s_hashmap[s[i]] = s_hashmap.get(s[i], 0) + 1
            
        for j in range(len(t)):
            if s_hashmap.get(t[j], 0) == 0:
                return False
            s_hashmap[t[j]] -= 1
        
        return True
