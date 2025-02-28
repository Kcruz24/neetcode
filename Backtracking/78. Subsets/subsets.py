from typing import List


class Solution:
    # O(Nx2^N) Time | O(N) Space
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.possible_subsets(nums, 0, [], [])

    def possible_subsets(self, nums, start, output, subset):
        output.append(subset.copy())

        for i in range(start, len(nums)):
            subset.append(nums[i])
            self.possible_subsets(nums, i + 1, output, subset)
            subset.pop()

        return output
