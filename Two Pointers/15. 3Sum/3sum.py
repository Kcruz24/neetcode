from typing import List

class Solution:
    # O(N^2) Time | O(log(N)) Space
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for idx in range(len(nums)):
            if nums[idx] > 0:
                break
            if idx == 0 or nums[idx - 1] != nums[idx]:
                self.twoSum(nums, idx, ans)
        return ans

    def twoSum(self, numbers: List[int], idx: int, ans: List[List[int]]) -> List[int]:
        left = idx + 1
        right = len(numbers) - 1

        while left < right:
            total = numbers[idx] + numbers[left] + numbers[right]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                ans.append([numbers[left], numbers[right], numbers[idx]])

                left += 1
                right -= 1
                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1


sol = Solution()

nums = [-1,0,1,2,-1,-4]
print(sol.threeSum(nums))

nums = [0, 1, 1]
print(sol.threeSum(nums))

nums = [0,0,0]
print(sol.threeSum(nums))

nums = [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]
print(sol.threeSum(nums))