# using HashMap
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


# Using MinHeap

import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # form pairs (num, count)
        occurrences = {}
        for num in nums:
            occurrences[num] = occurrences.get(num, 0) + 1
        
        # build heap of pairs (-count, num) we need - as we turn max heap into min heap
        heap = []

        for key, val in occurrences.items():
            heapq.heappush(heap, (-val, key))
        
        # pop most frequent pairs (we need only num)
        result = []
        while k > 0:
            result.append(heapq.heappop(heap)[1])
            k -= 1
        
        return result
