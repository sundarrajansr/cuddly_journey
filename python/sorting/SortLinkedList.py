# sort linked list using merge sort (  n log n)
# same is a problem @ https://leetcode.com/problems/sort-list/
import sys


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: # base case of list with 1 element or no element
            return head
        left = None
        right = None
        if head.next.next is None: # base case of list with 2 elements
            left = head
            right = head.next
            head.next = None
            right.next = None
        else:
            middle = self.mid(head)
            left = head
            right = middle.next
            middle.next = None # unlike array , linked list allows the cut the lists where ever needed.
            # In array , while sorting we need p and r limit for sorting , in linked list end can be nullified.
        return self.merge(self.sortList(left), self.sortList(right))

    # left and right are already sorted lists
    # merge return a single list with left and right
    def merge(self, left, right):
        root = ListNode(0)
        cur = root
        while left or right:
            l = left.val if left else sys.maxsize
            r = right.val if right else sys.maxsize
            if l < r:
                cur.next = ListNode(l)
                cur = cur.next
                left = left.next
            else:
                cur.next = ListNode(r)
                cur = cur.next
                right = right.next
        return root.next

    def mid(self, head):
        if head is None or head.next is None:
            return head
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow


arr = [10, 7, 6, 2, 1, 6, 5, 3, 12, 19, 13, 14]
head = ListNode(arr[0])
cur = head
for x in arr:
    cur.next = ListNode(x)
    cur = cur.next
head = head.next
cur = head

s = Solution()
result = s.sortList(head)
cur = result
while cur:
    print(cur.val, end=' -> ')
    cur = cur.next
