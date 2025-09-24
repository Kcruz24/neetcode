from typing import List

class Solution:
    # O(N^2) Time | O(N) Space
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        ans = [0] * size

        for i in range(size):
            count = 1
            j = i + 1
            while j < size:
                if temperatures[j] > temperatures[i]:
                    break

                j += 1
                count += 1

            count = 0 if j == size else count
            ans[i] = count

        return ans


if __name__ == '__main__':
    sol = Solution()

    temperatures = [73,74,75,71,69,72,76,73]

    print(sol.dailyTemperatures(temperatures))