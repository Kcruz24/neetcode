import heapq
from typing import Counter, List


class Solution:
    # O(N^2) Time | O(N) Space
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

class Solution2:
    # O(NLog(N)) Time | O(N) Space
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        sorted_dict_items = sorted(counter.items(), key=lambda item: item[1], reverse=True)
        sorted_dict = dict(sorted_dict_items)
        res = []

        for key in sorted_dict.keys():
            res.append(key)
            k -= 1
            if k == 0:
                break

        return res

class Solution3:
    # Optimized version
    # O(N log K) Time | O(N) Space
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        heap = []

        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)

        result = [num for _, num in heap]
        return result

if __name__ == "__main__":
    s = Solution()

    nums = [1,1,1,2,2,3]

    k = 2

    s = Solution2()

    print(s.topKFrequent(nums, k))