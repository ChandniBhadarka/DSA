class Solution(object):
    def gameOfLife(self, board):
        m, n = len(board), len(board[0])
        copy_board = [row[:] for row in board]


        def count_live_neighbors(r, c):
            directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
            live_neighbors = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if copy_board[nr][nc] == 1:
                        live_neighbors += 1
            return live_neighbors

        for r in range(m):
            for c in range(n):
                live_neighbors = count_live_neighbors(r, c)

                if copy_board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = 0  # live → dead
                elif copy_board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 1  # dead → live