class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        bucket = [0] * (len(nums) + 1)

        for num in set(nums):
            bucket[num] = 1
        
        return [i for i in range(1, len(bucket)) if bucket[i] == 0]
