class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if i[-1] >= target:
                return target in i
            if i[0] > target:
                return False