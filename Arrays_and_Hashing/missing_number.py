class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        upd_nums = [-1] * (len(nums) + 1)

        for num in nums:
            upd_nums[num] = num
        
        for n in range(len(upd_nums)):
            if upd_nums[n] == -1:
                return n
