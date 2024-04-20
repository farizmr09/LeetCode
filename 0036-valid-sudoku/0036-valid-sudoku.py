class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        x = defaultdict(set)
        y = defaultdict(set)
        s = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in x[i] or board[i][j] in y[j] or board[i][j] in s[i // 3, j // 3]:
                    return False
                x[i].add(board[i][j])
                y[j].add(board[i][j])
                s[i // 3, j // 3].add(board[i][j])
        return True