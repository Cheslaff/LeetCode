class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        best = 0

        for n in nums_set:
            if n - 1 not in nums_set:
                n_next = n + 1
                while n_next in nums_set:
                    n_next += 1
                
                best = max(best, n_next - n)
        
        return best

# Finished Arrays And Hashing!!! 
