class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        blyaaaa = []

        left_pointa = 1
        right_pointa = 1

        for i in range(len(nums)):
            blyaaaa.append(left_pointa)
            left_pointa *= nums[i]
            
        for i in range(len(nums)-1, -1, -1):
            blyaaaa[i] *= right_pointa
            right_pointa *= nums[i]
            
        return blyaaaa
