from typing import List

class Solution:
    # O(1) Time | O(1) Space - Because the table is always 9x9
    # and the space is constant because we are only storing numbers.
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        validate_columns = self.__validate_column(board)
        validate_rows = self.__validate_row(board)
        validate_sub_boxes = self.__validate_sub_box(board)

        return validate_columns and validate_rows and validate_sub_boxes

    def __validate_column(self, board):
        col_length = len(board[0])
        row_length = len(board)

        for col in range(col_length):
            duplicates = set()

            for row in range(row_length):
                num = board[row][col]
                if num in duplicates:
                    return False

                if num == '.':
                    continue

                duplicates.add(num)

        return True

    def __validate_row(self, board):
        row_length = len(board)
        col_length = len(board[0])

        for row in range(row_length):
            duplicates = set()

            for col in range(col_length):
                num = board[row][col]
                if num in duplicates:
                    return False

                if num == '.':
                    continue

                duplicates.add(num)

        return True

    def __validate_sub_box(self, board):
        rows = 3
        cols = 3

        start_row = 0
        start_col = 0

        count = 0
        for _ in range(9):

            duplicates = set()
            for row in range(start_row, rows):
                for col in range(start_col, cols):
                    num = board[row][col]
                    if num in duplicates:
                        return False

                    if num == '.':
                        continue

                    duplicates.add(num)

            if cols == len(board[0]):
                start_col = 0
                cols = 3
                start_row += 3
                rows += 3
            else:
                start_col += 3
                cols += 3

            count += 1

        return True