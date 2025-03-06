from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = {}

        for num in nums:
            if num not in frequent:
                frequent[num] = 1
            else:
                frequent[num] += 1
                
        result = []
        max_key = float('-inf')
        for _ in range(k):
            max_value = -1
            for key, value in frequent.items():
                if value > max_value:
                    max_value = value
                    max_key = key

            result.append(max_key)
            if max_key in frequent:
                del frequent[max_key]

        return result


if __name__ == "__main__":
    s = Solution()

    nums = [1,1,1,2,2,3]

    k = 2

    s = Solution()

    print(s.topKFrequent(nums, k))