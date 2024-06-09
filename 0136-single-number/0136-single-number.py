class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        counter = 0
        for i in nums:
            if i in s:
                counter -= i
                continue
            counter += i
            s.add(i)
        return counter