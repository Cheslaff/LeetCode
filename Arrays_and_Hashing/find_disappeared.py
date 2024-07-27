# O(n) time |  O(n) space
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        bucket = [0] * (len(nums) + 1)

        for num in set(nums):
            bucket[num] = 1
        
        return [i for i in range(1, len(bucket)) if bucket[i] == 0]


# O(n) time |  O(1) space
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            i = abs(num) - 1
            nums[i] = -1 * abs(nums[i])

        res = []
        for i, num in enumerate(nums):
            if num > 0:
                res.append(i + 1)
        return res
