class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        in_arr1 = set()

        for num in nums1:
            in_arr1.add(num)

        for num in nums2:
            if num in in_arr1:
                res.append(num)
                in_arr1.remove(num)
        return res
