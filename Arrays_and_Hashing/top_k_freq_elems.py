class Solution(object):
    def topKFrequent(self, nums, k):
        nums_dict = {}
        
        for element in nums:
            if element in nums_dict:
                nums_dict[element] += 1
            else:
                nums_dict[element] = 1
            

        nums_dict = [key for key, _ in sorted(nums_dict.items(), key=lambda item: item[1], reverse=True)]
        return nums_dict[:k]
