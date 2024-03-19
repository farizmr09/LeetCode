class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix  = [0] * len(nums)
        sufix   = [0] * len(nums)
        for i in range(0, len(nums)):
            prefix[i]           = 1 if i - 1 < 0 else nums[i - 1] * prefix[i - 1] 
            sufix[-1 * i -1]    = 1 if -1 * i -1 == -1 else nums[-1 * i] * sufix[-1 * i]

        for i in range(0, len(nums)):
            nums[i] = prefix[i] * sufix[i]
        
        return nums