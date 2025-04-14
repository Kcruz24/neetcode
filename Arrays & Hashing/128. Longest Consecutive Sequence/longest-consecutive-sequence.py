from typing import List

class Solution:
    # O(N) Time | O(N) Space
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            if num - 1 not in num_set:
                curr_num = num
                curr_streak = 1

                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_streak += 1

                longest_streak = max(curr_streak, longest_streak)

        return longest_streak



if __name__ == '__main__':
    sol = Solution()

    nums = [100, 4, 200, 1, 3, 2]
    print(sol.longestConsecutive(nums))

    nums = [0,3,7,2,5,8,4,6,0,1]
    print(sol.longestConsecutive(nums))

    nums = [1,0,1,2]
    print(sol.longestConsecutive(nums))
