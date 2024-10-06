class Solution:

    def encode(self, strs: List[str]) -> str:
        str_ = ""
        for s in strs:
            str_ += f"{len(s)}/" + s
        return str_

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0
        r = l
        while l < len(s):
            while s[r] != "/":
                r += 1
            length = int(s[l:r])
            l = r + 1
            r = l + length
            res.append(s[l:r])
            l = r
        return res
            
# Revisited this problem!
