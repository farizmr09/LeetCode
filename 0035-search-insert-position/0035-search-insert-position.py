class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        if max(nums) < target:
            return len(nums)
        if min(nums) > target:
            return 0
        if target > nums[len(nums) // 2]:
            return len(nums) // 2 + self.searchInsert(nums[len(nums) // 2:], target)
        else:
            return self.searchInsert(nums[:len(nums) // 2], target)