class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # to use 2sum technique of 2 pointers we need to sort array
        nums.sort()
        result = []

        for cur in range(len(nums)):
            # to avoid duplicates
            if cur > 0 and nums[cur] == nums[cur - 1]:
                continue

            target = -nums[cur]
            l = cur + 1
            r = len(nums) - 1
            
            while l < r:
                twosum = nums[l] + nums[r]

                if twosum > target:
                    r -= 1
                elif twosum < target:
                    l += 1
                else:
                    result.append([nums[l], nums[r], nums[cur]])
                    l += 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
        return result
