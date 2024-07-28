class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hashmap = {}

        for i in range(1, max(nums)+2):
            hashmap[i] = 0

        for value in nums:
            hashmap[value] = hashmap.get(value, 0) + 1
        
        missing = 0
        double = 0
        for key in hashmap.keys():
            if hashmap[key] == 0 and missing == 0:
                missing = key
            elif hashmap[key] > 1 and double == 0:
                double = key
        
        return [double, missing]
