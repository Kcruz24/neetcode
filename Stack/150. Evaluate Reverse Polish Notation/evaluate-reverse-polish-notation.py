from typing import List

class Solution:
    # O(N) Time | O(N) Space
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                num_2 = stack.pop()
                num_1 = stack.pop()

                stack.append(num_1 + num_2)
            elif token == "-":
                num_2 = stack.pop()
                num_1 = stack.pop()

                stack.append(num_1 - num_2)
            elif token == "/":
                num_2 = stack.pop()
                num_1 = stack.pop()

                stack.append(int(num_1 / num_2))
            elif token == "*":
                num_2 = stack.pop()
                num_1 = stack.pop()

                stack.append(num_1 * num_2)
            else:
                stack.append(int(token))

        return stack[0]


if __name__ == '__main__':
    sol = Solution()