class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        c = set()
        l = 0
        for r in range(len(nums)):
            if abs(l - r) > k:
                c.remove(nums[l])
                l += 1
            if nums[r] in c:
                return(True)
            c.add(nums[r])
        return(False)