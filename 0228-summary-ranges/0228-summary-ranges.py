class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        list = []
        l = 0
        if len(nums) == 1:
            return ([str(nums[0])])
        for r in range(1, len(nums)):
            if nums[r] - nums[r - 1] != 1:
                if l == r - 1:
                    list.append("{}".format(nums[l]))
                else:    
                    list.append("{}->{}".format(nums[l], nums[r - 1]))
                l = r
            if r == len(nums) - 1:
                if l == r:
                    list.append("{}".format(nums[l]))
                else:    
                    list.append("{}->{}".format(nums[l], nums[r]))
        return list