class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candy_set = set(candyType)

        n = len(candyType) / 2

        res = 0
        for candy in candy_set:
            if n > 0:
                res += 1
                n -= 1
            else:
                break
        return res
