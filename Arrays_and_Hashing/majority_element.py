# 80%
# time complexity: O(n)
# space complexity: O(n)


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_table = {}

        for num in nums:
            hash_table[num] = hash_table.get(num, 0) + 1

            if hash_table[num] > len(nums) // 2:
                return num
        return None
