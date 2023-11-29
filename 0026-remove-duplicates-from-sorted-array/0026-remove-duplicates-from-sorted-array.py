class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        holder = []
        counter = 0
        while i < len(nums):
            jump = nums.count(nums[i])
            holder.append(nums[i])
            i = i + jump
            counter = counter + 1
        nums.clear()
        nums.extend(holder)
        return counter