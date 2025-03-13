from typing import List

class Solution:
    # Optimal solution
    # O(N) Time | O(1) Space
    # The output array does not count towards the space complexity analysis
    @classmethod
    def productExceptSelf(cls, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]

        pos = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= pos
            pos *= nums[i]

        return res


if __name__ == "__main__":

    nums = [1, 2, 3, 4]
    print(Solution.productExceptSelf(nums))