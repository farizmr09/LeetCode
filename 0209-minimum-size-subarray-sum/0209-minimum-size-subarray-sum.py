class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target in nums:
            return 1
        if sum(nums) < target:
            return 0
        j, total, minimum = 0, 0, float('inf') 
        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                minimum = min(minimum, i - j + 1)
                total -= nums[j]
                j += 1
        return minimum 
