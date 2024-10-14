class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []

        l = 0
        r = n

        for i in range(n):
            res.append(nums[l + i])
            res.append(nums[r + i])
        
        return res
