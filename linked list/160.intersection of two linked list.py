from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pa = headA
        pb = headB
        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa


# Build intersecting lists: A = 4->1->8->4->5, B = 5->6->1->8->4->5 (shared from 8)
shared = ListNode(8)
shared.next = ListNode(4)
shared.next.next = ListNode(5)

headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = shared

headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = shared

result = Solution().getIntersectionNode(headA, headB)
print(result.val if result else None)