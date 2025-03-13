from typing import List

class Solution:
    # O(N^2) Time | O(N) Space
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i == 0 or nums[i - 1] != nums[i]:
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    total = nums[i] + nums[left] + nums[right]

                    if total == 0:
                        res.append((nums[i], nums[left], nums[right]))
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                    elif total > 0:
                        right -= 1
                    elif total < 0:
                        left += 1

        return res

sol = Solution()

nums = [-1,0,1,2,-1,-4]
print(sol.threeSum(nums))

nums = [0, 1, 1]
print(sol.threeSum(nums))

nums = [0,0,0]
print(sol.threeSum(nums))

nums = [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]
print(sol.threeSum(nums))