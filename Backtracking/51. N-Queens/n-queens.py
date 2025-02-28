from typing import List

'''
n = 4

[
    [".Q..","...Q","Q...","..Q."],
    ["..Q.","Q...","...Q",".Q.."]
]

'''

class Solution:
    # O(N!) Time | O(N^2) Space
    def solveNQueens(self, n: int) -> List[List[str]]:
        def create_board(state):
            board = []
            for row in state:
                board.append(''.join(row))

            return board

        def backtrack(row, diagonals, anti_diagonals, columns, state):
            if row == n:
                ans.append(create_board(state))
                return

            for col in range(n):
                curr_diagonal = row - col
                curr_anti_diagonal = row + col

                is_col_seen = col in columns
                is_diagonal_seen = curr_diagonal in diagonals
                is_anti_diagonal_seen = curr_anti_diagonal in anti_diagonals

                if is_col_seen or is_diagonal_seen or is_anti_diagonal_seen:
                    continue

                # Add the queen to the board
                columns.add(col)
                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_anti_diagonal)

                state[row][col] = 'Q'

                # Move on the the next row with the updated board
                backtrack(row + 1, diagonals, anti_diagonals, columns, state)

                # Remove
                columns.remove(col)
                diagonals.remove(curr_diagonal)
                anti_diagonals.remove(curr_anti_diagonal)

                state[row][col] = '.'

        ans = []
        empty_board = [['.'] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), empty_board)

        return ans


