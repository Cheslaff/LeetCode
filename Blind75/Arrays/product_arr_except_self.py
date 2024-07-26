class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        # forward pass
        multiplier = 1
        for i in range(len(nums)):
            result[i] *= multiplier
            multiplier *= nums[i]

        # backward pass
        multiplier = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= multiplier
            multiplier *= nums[i]
        
        return result
