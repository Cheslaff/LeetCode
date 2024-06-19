class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}

        for i in range(len(nums)):
            if target - nums[i] in checked:
                return [i, checked[target - nums[i]]]
            checked[nums[i]] = i

        return []
    