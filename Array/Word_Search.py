class Solution(object):
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word): 
                return True
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != word[i]):
                return False
            
           
            temp = board[r][c]
            board[r][c] = "#"

            #  neighbors
            found = (dfs(r+1, c, i+1) or  # down
                    dfs(r-1, c, i+1) or  # up
                    dfs(r, c+1, i+1) or  # right
                    dfs(r, c-1, i+1))    # left

            board[r][c] = temp  # undo marking
            return found

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False

        