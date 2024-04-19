class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            cX = Counter(board[i])
            cY = Counter()
            cX.pop(".")
            if len(cX.values()) > 0 and max(cX.values()) > 1:
                return False
            for j in range(len(board)):
                if board[j][i] != ".":
                    cY.update(board[j][i])
                if len(cY.values()) > 0 and max(cY.values()) > 1:
                    return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                c = Counter()
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        if board[x][y] != ".":
                            c.update(board[x][y])
                        if len(c.values()) > 0 and max(c.values()) > 1:
                            return False
                
        
        return True