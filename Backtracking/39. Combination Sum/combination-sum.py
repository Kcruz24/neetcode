from typing import List


class Solution:
    # O(N^T/M+1) Time | O(T/M) Space
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.backtrack(candidates, target, [], [])

    def backtrack(self, candidates, target, combinations, sub_comb):
        if target == 0:
            combinations.append(list(sub_comb))
            return

        elif target < 0:
            return

        for i in range(len(candidates)):
            sub_comb.append(candidates[i])
            fulfill = target - candidates[i]

            self.backtrack(candidates[i:], fulfill, combinations, sub_comb)

            sub_comb.pop()

        return combinations


if __name__ == '__main__':
    sol = Solution()

    candidates = [2, 3, 6, 7]
    target = 7

    print(sol.combinationSum(candidates, target))

