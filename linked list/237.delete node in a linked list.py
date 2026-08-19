# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


# ---------- Helper functions for testing ----------
def build_linked_list(values):
    """Create a linked list from a Python list and return its head."""
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


def print_linked_list(head):
    """Print a linked list starting at the given node."""
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" -> ".join(vals) if vals else "None")


def find_node(head, target_val):
    """Find and return the node with the given value."""
    while head:
        if head.val == target_val:
            return head
        head = head.next
    return None


# ---------- Example usage ----------
if __name__ == "__main__":
    sol = Solution()

    # Test: 1 -> 2 -> 3 -> 4, delete node with value 3
    head = build_linked_list([1, 2, 3, 4])
    print("Original list:", end=" ")
    print_linked_list(head)

    node_to_delete = find_node(head, 3)
    sol.deleteNode(node_to_delete)

    print("After deleting node 3:", end=" ")
    print_linked_list(head)

    print()

    # Test: 4 -> 5 -> 1 -> 9, delete node with value 5
    head2 = build_linked_list([4, 5, 1, 9])
    print("Original list:", end=" ")
    print_linked_list(head2)

    node_to_delete2 = find_node(head2, 5)
    sol.deleteNode(node_to_delete2)

    print("After deleting node 5:", end=" ")
    print_linked_list(head2)