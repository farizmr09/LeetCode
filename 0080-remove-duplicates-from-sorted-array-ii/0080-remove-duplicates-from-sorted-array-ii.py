class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = Counter(nums)
        maps = set(nums)
        for i in maps:
            for j in range(2, c[i]):
                nums.remove(i)
        return len(nums)
