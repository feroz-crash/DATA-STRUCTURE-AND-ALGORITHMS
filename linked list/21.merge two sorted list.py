from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        t1 = list1
        t2 = list2

        while t1 and t2:
            if t1.val <= t2.val:
                current.next = t1
                t1 = t1.next
            else:
                current.next = t2
                t2 = t2.next
            current = current.next

        current.next = t1 if t1 else t2
        return dummy.next


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
    print(" -> ".join(vals) if vals else "None")


# ---------- Example usage ----------
if __name__ == "__main__":
    sol = Solution()

    # Test 1: both non-empty
    l1 = build_linked_list([1, 2, 4])
    l2 = build_linked_list([1, 3, 4])
    print("List 1:", end=" "); print_linked_list(l1)
    print("List 2:", end=" "); print_linked_list(l2)
    merged = sol.mergeTwoLists(l1, l2)
    print("Merged:", end=" "); print_linked_list(merged)

    print()

    # Test 2: one empty
    l3 = build_linked_list([])
    l4 = build_linked_list([0])
    merged2 = sol.mergeTwoLists(l3, l4)
    print("Merged (one empty):", end=" "); print_linked_list(merged2)

    print()

    # Test 3: both empty
    merged3 = sol.mergeTwoLists(None, None)
    print("Merged (both empty):", end=" "); print_linked_list(merged3)