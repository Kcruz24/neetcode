from typing import List
from collections import Counter

# Backtracking with Counters
class Solution:
    # O(2^N) Time | O(N) Space
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        frequencies = Counter(candidates)
        frequencies = [(num, frequencies[num]) for num in frequencies]

        return self.backtrack(candidates, target, [],  0, frequencies, [])
    

    def backtrack(self, candidates, target, combinations, curr, counter, sub_comb):
        if target == 0:
            combinations.append(sub_comb.copy())
            return

        elif target < 0:
            return

        for next_curr in range(curr, len(counter)):
            candidate, freq = counter[next_curr]

            if freq <= 0:
                continue

            sub_comb.append(candidate)
            counter[next_curr] = (candidate, freq - 1)

            fulfill = target - candidate
            self.backtrack(candidates[next_curr:], fulfill, combinations, next_curr, counter, sub_comb)

            counter[next_curr] = (candidate, freq)
            sub_comb.pop()

        return combinations


# Backtracking with index
class Solution:
    # O(2^N) Time | O(N) Space
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.backtrack(candidates, target, [], [], 0)


    def backtrack(self, candidates, target, combinations, sub_comb, start):
        if target == 0:
            combinations.append(list(sub_comb))
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            pick = candidates[i]
            if target - pick < 0:
                break

            sub_comb.append(pick)
            fulfill = target - pick

            self.backtrack(candidates, fulfill, combinations, sub_comb, i + 1)

            sub_comb.pop()

        return combinations


if __name__ == '__main__':
    sol = Solution()

    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8

    print(sol.combinationSum2(candidates, target))
