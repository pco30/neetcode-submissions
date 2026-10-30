# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         curr = head
#         ans = []

#         while curr is not None:
#             ans.append(curr.val)
#             curr = curr.next
        
#         ans = ans[::-1]

#         dummy = ListNode(0)
#         curr3 = dummy
        
#         for val in ans:
#             curr3.next = ListNode(val)
#             curr3 = curr3.next

#         head = dummy.next
#         return head

        