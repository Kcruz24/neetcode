from typing import List


class Solution:
    # O(4^NxN) Time | O(N) Space
    def letterCombinations(self, digits: str) -> List[str]:
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        if len(digits) == 0:
            return []

        combinations = []
        path = []
        curr_idx = 0

        self.backtrack(digits, phone_map, curr_idx, path, combinations)

        return combinations

    def backtrack(self, digits, phone_map, curr_idx, path, combinations):
        if len(path) == len(digits):
            combinations.append(''.join(path))
            return

        letters = phone_map[digits[curr_idx]]
        for letter in letters:
            path.append(letter)

            self.backtrack(digits, phone_map, curr_idx + 1, path, combinations)
            
            path.pop()


if __name__ == '__main__':
    sol = Solution()

    digits = '232'
    print(sol.letterCombinations(digits))

    digits = '2'
    print(sol.letterCombinations(digits))
