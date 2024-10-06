class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        l_prod = 1
        r_prod = 1
        for i in range(len(nums)):
            res.append(l_prod)
            l_prod *= nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            res[i] *= r_prod
            r_prod *= nums[i]
        
        return res
