from typing import List


class Solution:
    # O(Nx2^N) Time | O(N) Space
    def partition(self, s: str) -> List[List[str]]:
        return self.backtrack(s, 0, [], [])

    def backtrack(self, s, start, partitions, sub):
        if start == len(s):
            partitions.append(sub.copy())
            return

        for end in range(start, len(s)):
            substring = s[start: end + 1]
            if self.is_palindrome(substring):

                sub.append(substring)

                self.backtrack(s, end + 1, partitions, sub)

                sub.pop()

        return partitions

    def is_palindrome(self, s):
        return s == s[::-1]


if __name__ == '__main__':
    sol = Solution()

    s = 'aab'
    print(sol.partition(s))
