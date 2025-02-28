from typing import List


class Solution:
    # O(sum(1, n) P(N, K)) Time | O(N!) Space
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.backtrack(nums, [], [], 0)

    def backtrack(self, nums, permutations, perm, start):
        if start == len(nums):
            permutations.append(nums.copy())

        for i in range(start, len(nums)):
            self.swap(nums, i, start)
            self.backtrack(nums, permutations, perm, start + 1)
            self.swap(nums, start, i)

        return permutations


    def swap(self, nums, first, second):
        nums[first], nums[second] = nums[second], nums[first]


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3]

    print(sol.permute(nums))
