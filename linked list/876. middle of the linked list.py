from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow


# ---------- Helper functions for testing ----------
def build_linked_list(values):
    """Create a linked list from a Python list and return its head."""
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def print_linked_list(head):
    """Print a linked list starting at the given node."""
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" -> ".join(vals))


# ---------- Example usage ----------
if __name__ == "__main__":
    sol = Solution()

    # Odd length: [1,2,3,4,5] -> middle is 3
    head1 = build_linked_list([1, 2, 3, 4, 5])
    print("List 1:", end=" ")
    print_linked_list(head1)
    mid1 = sol.middleNode(head1)
    print("Middle of List 1:", end=" ")
    print_linked_list(mid1)

    print()

    # Even length: [1,2,3,4,5,6] -> middle is 4 (second middle)
    head2 = build_linked_list([1, 2, 3, 4, 5, 6])
    print("List 2:", end=" ")
    print_linked_list(head2)
    mid2 = sol.middleNode(head2)
    print("Middle of List 2:", end=" ")
    print_linked_list(mid2)