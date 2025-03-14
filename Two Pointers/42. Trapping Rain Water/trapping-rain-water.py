from typing import List

class Solution:
    # O(N) Time | O(N) Space
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        maxLeft[0] = height[0]
        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i - 1], height[i])

        maxRight[len(height) - 1] = height[len(height) - 1]
        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i])

        water = 0
        for i in range(len(height)):
            trapped = min(maxLeft[i], maxRight[i]) - height[i]

            if trapped > 0:
                water += trapped

        return water


class Solution2:
    # O(N) Time | O(1) Space
    def trap(self, height: List[int]) -> int:
        water = 0

        left = 0
        right = len(height) - 1
        maxLeft = 0
        maxRight = height[-1]

        while left < right:
            trapped = 0

            if height[left] > height[right]:
                maxRight = max(maxRight, height[right])
                trapped = maxRight - height[right]
                right -= 1
            else:
                maxLeft = max(maxLeft, height[left])
                trapped = maxLeft - height[left]
                left += 1

            if trapped > 0:
                water += trapped

        return water

sol = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(sol.trap(height))

sol = Solution2()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(sol.trap(height))




