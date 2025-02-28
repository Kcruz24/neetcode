from typing import List


class Solution:
    # O(Nx2^N) Time | O(N) Space
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.backtrack(nums, [], [], 0)

    def backtrack(self, nums, subsets, sub, start):
        subsets.append(sub.copy())

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue

            sub.append(nums[i])
            self.backtrack(nums, subsets, sub, i + 1)
            sub.pop()

        return subsets


if __name__ == '__main__':
    sol = Solution()

    nums = [1, 2, 2]

    print(sol.subsetsWithDup(nums))