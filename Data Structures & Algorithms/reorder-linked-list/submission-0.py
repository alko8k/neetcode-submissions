# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        stack = []
        curr = head

        while curr:
            stack.append(curr)
            curr = curr.next

        counter = len(stack) // 2

        curr = head
        temp = head.next

        while stack and counter != 0:
            curr.next = stack.pop()
            counter -= 1
            curr = curr.next
            curr.next = temp
            curr = curr.next
            temp = curr.next
            curr.next = None
        return
        



        





        