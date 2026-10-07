class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # ez question, we compare row, column, and figure out a clever way for 3x3
        # know that we should use set for dupe 
        seen = set()
        # check row for sus
        for row in range(9):
            seen.clear()
            for e in board[row]:
                if e in seen and e!=".":
                    return False
                seen.add(e)
        # check col for sus
        for i in range(9):
            seen.clear()
            for j in range(9):
                if board[j][i] in seen and board[j][i]!=".":
                    return False
                seen.add(board[j][i])
        # check 3x3 for sus
        # while not elegant, a fault proof way
        # is to not try to do everything in the loop in initial try
        # observed that the 9 vertices for left upper are 
        # (0,0) (0,3) (0,6)
        # (3,0) (3,3) (3,6)
        # (6,0) (6,3) (6,6) 
        # (x,y)
        for x in range(0,7,3):
            for y in range(0,7,3):
                seen.clear()
                for w in range(3):
                    for z in range(3):
                        if board[x+w][y+z] in seen and board[x+w][y+z]!=".":
                            return False
                        seen.add(board[x+w][y+z])
        return True
                