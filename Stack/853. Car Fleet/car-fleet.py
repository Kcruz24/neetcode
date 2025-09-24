from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(pos, speed) for pos, speed in zip(position, speed)]
        stack = []

        for pos, speed in sorted(pair, reverse=True): # type: ignore
            car = (target - pos) / speed # type: ignore
            stack.append(car)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        fleets = len(stack)
        return fleets
