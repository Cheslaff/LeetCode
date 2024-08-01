class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}

        for i in range(len(nums)):
            if target - nums[i] in checked:
                return [checked[target - nums[i]], i]
            checked[nums[i]] = i

        return None
