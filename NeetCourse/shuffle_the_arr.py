class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        l = 0
        r = n

        while len(result) < len(nums):
            result.append(nums[l])
            result.append(nums[r])
            l += 1
            r += 1
        return result
