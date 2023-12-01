class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maps = Counter(nums)
        sets = set(nums)
        for i in sets:
            if maps[i]>(len(nums)/2):
                return i