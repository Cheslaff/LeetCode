class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unq = 1
        for cur in range(1, len(nums)):
            if nums[cur] != nums[cur-1]:
                nums[unq] = nums[cur]
                unq += 1
        
        return unq