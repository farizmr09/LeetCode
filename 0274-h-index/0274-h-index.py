class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 0
        for i in range(max(citations) + 1):
            if len(list(filter(lambda x: x >= i, citations))) > h:
                h = i
        return h