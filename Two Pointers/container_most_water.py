class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_vol = 0

        while r > l:
            vol = min(height[l], height[r]) * (r - l)
            max_vol = max(max_vol, vol)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_vol
