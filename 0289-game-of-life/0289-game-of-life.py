class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        prev = copy.deepcopy(board)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                holder = 0
                if i > 0:
                    holder += prev[i - 1][j]
                    if j > 0:
                        holder += prev[i - 1][j - 1]
                if j > 0:
                    holder += prev[i][j - 1]
                if i < len(prev) - 1:
                    holder += prev[i + 1][j]
                    if j > 0:
                        holder += prev[i + 1][j - 1]
                    if j < len(prev[0]) - 1:
                        holder += prev[i + 1][j + 1]
                if j < len(prev[0]) - 1:
                    holder += prev[i][j + 1]
                    if i > 0:
                        holder += prev[i - 1][j + 1]
                if holder < 2 or holder > 3:
                    board[i][j] = 0
                if holder == 2 or holder == 3:
                    board[i][j] = prev[i][j]
                if holder == 3:
                    board[i][j] = 1