from typing import List


class Solution:
    # O(N) Time | O(N) Space
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for idx, height in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > height:
                i, h = stack.pop()
                max_area = max(max_area, h * (idx - i))
                start = i

            stack.append((start, height))

        for i, height in stack:
            max_area = max(max_area, height *  (len(heights) - i))

        return max_area

if __name__ == '__main__':
    sol = Solution()