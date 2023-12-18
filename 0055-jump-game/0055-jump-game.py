class Solution:
    def canJump(self, nums: List[int]) -> bool:
        holder = [False] * len(nums)
        holder[0] = True
        for i in range(len(nums) - 1):
            if holder[-1] == True:
                break
            if holder[i] == True:
                for j in range(i, min(nums[i] + i, len(nums) - 1)):
                    holder[j + 1] = True
        return holder[-1]    