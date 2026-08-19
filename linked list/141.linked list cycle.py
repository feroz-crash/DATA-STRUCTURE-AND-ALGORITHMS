from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


# Build a list with a cycle: 3 -> 2 -> 0 -> -4 -> (back to 2)
n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(0)
n4 = ListNode(-4)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n2  # creates the cycle

print(Solution().hasCycle(n1))  # True

# Build a list with no cycle: 1 -> 2
m1 = ListNode(1)
m2 = ListNode(2)
m1.next = m2

print(Solution().hasCycle(m1))  # False