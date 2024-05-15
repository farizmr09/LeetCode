class Solution:
    def partitionString(self, s: str) -> int:
        counter = 1
        partitionSet = []
        for i in s:
            if i in partitionSet:
                counter += 1
                partitionSet.clear()
            partitionSet.append(i)
                
        return counter