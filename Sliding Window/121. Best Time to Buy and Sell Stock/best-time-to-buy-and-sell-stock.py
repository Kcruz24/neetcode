from typing import List

class Solution:
    # Brute Force
    # O(N^2) Time | O(1) Space
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > profit:
                    profit = prices[j] - prices[i]

        return profit

class Solution2:
    # Optimal
    # O(N) Time | O(1) Space
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit


if __name__ == '__main__':
    sol = Solution()

    prices = [7,1,5,3,6,4]
    print(sol.maxProfit(prices))


