class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for r in range(len(board)):
            vals = set()
            for c in range(len(board[0])):
                if board[r][c].isdigit():
                    if board[r][c] in vals:
                        return False
                    else:
                        vals.add(board[r][c])
        
        for c in range(len(board[0])):
            vals = set()
            for r in range(len(board)):
                if board[r][c].isdigit():
                    if board[r][c] in vals:
                        return False
                    else:
                        vals.add(board[r][c])
        
        row = [0, 3, 6]
        col = [0, 3, 6]

        for r in row:
            for c in col:
                vals = set()
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        if board[i][j].isdigit():
                            if board[i][j] in vals:
                                return False
                            else:
                                vals.add(board[i][j])
        return True
        