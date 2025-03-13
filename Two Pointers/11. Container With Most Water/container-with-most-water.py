from typing import List

class Solution:
    # Brute Force
    # O(N^2) Time | O(1) Space
    def maxArea(self, height: List[int]) -> int:
        res = 0
        for left in range(len(height)):
            for right in range(left + 1, len(height)):
                area = (right - left) * min(height[left], height[right])
                res = max(res, area)

        return res


class Solution2:
    # Optimal Solution
    # O(N) Time | O(1) Space
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left = 0
        right = len(height) - 1

        while left < right:
            area = (right - left) * min(height[left], height[right])
            res = max(res, area)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return res

sol = Solution2()
height = [1, 8 , 6, 2, 5, 4, 8, 3, 7]
print(sol.maxArea(height))
