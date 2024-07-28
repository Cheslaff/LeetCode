class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1_map = {}

        for i in range(len(list1)):
            list1_map[list1[i]] = i
        
        output = []
        min_idx_sum = float("inf")
        for j in range(len(list2)):
            if list2[j] in list1_map:
                idx_sum = j + list1_map[list2[j]]

                if idx_sum < min_idx_sum:
                    output = [list2[j]]
                elif idx_sum == min_idx_sum:
                    output.append(list2[j])

                min_idx_sum = min(min_idx_sum, idx_sum)
        
        return output
