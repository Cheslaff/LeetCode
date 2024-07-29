class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = 0

        while l + len(needle) <= len(haystack):
            r = l + len(needle)
            if haystack[l:r] == needle:
                return l
            l += 1
        
        return -1
