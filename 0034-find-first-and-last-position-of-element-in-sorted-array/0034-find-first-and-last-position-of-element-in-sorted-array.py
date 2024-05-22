class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = nums.index(target) if target in nums else -1
        
        if start == -1:
            return [-1, -1]
        
        nums[start] = float("inf")
        
        end = -1
        
        while target in nums:
            end = nums.index(target) 
            nums[end] = float("inf")
        
        return [start, end if end != -1 else start]