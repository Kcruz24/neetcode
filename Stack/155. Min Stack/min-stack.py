class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    # O(1) Time
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            min_val = min(val, self.min_stack[-1])
            self.min_stack.append(min_val)
        else:
            self.min_stack.append(val)

    # O(1) Time
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    # O(1) Time
    def top(self) -> int:
        return self.stack[-1]

    # O(1) Time
    def getMin(self) -> int:
        return self.min_stack[-1]