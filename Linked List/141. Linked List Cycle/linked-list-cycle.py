from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # O(N) Time | O(N) Space
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        trav = head
        while trav:
            trav.val = True
            if trav in seen:
                return True
            seen.add(trav)
            trav = trav.next

        return False

class Solution:
    # Optimal
    # O(N) Time | O(1) Space
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast and fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next

        return True