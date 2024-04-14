class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        i = 0
        j = len(height) - 1
        max = 0
        while i < j:
            if max < min(height[i], height[j]) * (j - i):
                max = min(height[i], height[j]) * (j - i)
            if height[i] < height[j]:
                i += 1
                continue
            j -= 1
        return max