from typing import List


class Solution:
    # O(Nx3^L) Time | O(L) Space - "L" is the length of the word to be matched.
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_length = len(board)
        col_length = len(board[0])

        for row in range(row_length):
            for col in range(col_length):
                if self.backtrack(board, word, row, col):
                    return True

        return False

    def backtrack(self, board, word, row, col):
        if len(word) == 0:
            return True

        is_row_out_of_bounds = row < 0 or row >= len(board)
        is_col_out_of_bounds = col < 0 or col >= len(board[0])
        is_out_of_bounds = is_row_out_of_bounds or is_col_out_of_bounds

        if is_out_of_bounds:
            return False

        is_not_equal_letter = word[0] != board[row][col]
        if is_not_equal_letter:
            return False

        # Mark visited
        board[row][col] = '#'

        result = self.backtrack(board, word[1:], row + 1, col) or \
            self.backtrack(board, word[1:], row - 1, col) or \
            self.backtrack(board, word[1:], row, col + 1) or \
            self.backtrack(board, word[1:], row, col - 1)

        board[row][col] = word[0]

        return result
