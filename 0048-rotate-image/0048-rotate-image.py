class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r_img = [[] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in reversed(range(len(matrix[0]))):
                r_img[i].append(matrix[j][i])
        
        matrix.clear()
        matrix.extend(r_img)