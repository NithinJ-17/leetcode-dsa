# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode()
        dummy.next = head
        slow , fast = dummy,dummy
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        cur = slow.next
        slow.next = None
        while cur!= None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        newList = ListNode()
        while prev!=None and head!=None:
            newList.next = head
            newList = newList.next
            head=head.next
            newList.next = prev
            prev = prev.next
            newList = newList.next
        

        if head:
            newList.next = head

        return newList.next
            
            


        
        