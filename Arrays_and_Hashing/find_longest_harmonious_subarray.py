class Solution:
    def findLHS(self, nums: List[int]) -> int:
        max_subarray = 0
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        for key in hashmap.keys():
            cur_subarray = hashmap[key] + hashmap.get(key+1, -hashmap[key])
            max_subarray = max(max_subarray, cur_subarray)
        
        return max_subarray
