from typing import List


class Solution:
    # O(N) Time | O(1) Space
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr1, ptr2 = 0, len(numbers) - 1

        while ptr1 < ptr2:
            total = numbers[ptr1] + numbers[ptr2]
            if total == target:
                return [ptr1 + 1, ptr2 + 1]
            elif total > target:
                ptr2 -= 1
            elif total < target:
                ptr1 += 1