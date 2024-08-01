class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multipliers = [1] * len(nums)

        l_side = 1
        for i in range(len(nums)):
            multipliers[i] *= l_side
            l_side *= nums[i]
        
        r_side = 1
        for i in range(len(nums)-1, -1, -1):
            multipliers[i] *= r_side
            r_side *= nums[i]
        
        return multipliers
