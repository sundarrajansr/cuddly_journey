# sort linked list using merge sort (  n log n)
# same is a problem @ https://leetcode.com/problems/sort-list/
import sys


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        pass

    def partition(self, start, end):
        pass

    # left and right are already sorted lists
    # merge return a single list with left and right
    def merge(self, left, right):
        root = ListNode(0)
        cur = root
        while left or right:
            l = left.val if left else sys.maxsize
            r = right.val if right else sys.maxsize
            cur.next = ListNode(min(l, r))
            cur = cur.next
            if left:
                left = left.next
            if right:
                right = right.next
        return root.next

    def mid(self, head):
        slow = head
        fast = head
        while fast:
            if fast.next:
                fast = fast.next
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
while cur:
    print(cur.val, ' ')
    cur = cur.next
