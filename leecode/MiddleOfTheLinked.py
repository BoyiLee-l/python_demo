# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head:[ListNode]) -> [ListNode]:
        fast = slow = head
        while fast and fast.next:
            print(f"fast:{fast.val}, next:{fast.next.val}")
            fast = fast.next.next
            slow = slow.next
        print(slow.val)
        return slow

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8))))))))
solution = Solution()
solution.middleNode(head)