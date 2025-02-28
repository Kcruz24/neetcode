from typing import List


class Solution:
    # O(N) Time | O(N) Space
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        distincts = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in distincts:
                return [i, distincts[complement]]
            distincts[nums[i]] = i
