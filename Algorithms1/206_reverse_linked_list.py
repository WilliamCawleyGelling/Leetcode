"""
Given the head of a singly linked list, reverse the list, 
and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. 
Could you implement both?
"""

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        #ideas can it be done in one pass 
        #if you have cur and next need to be two ahead 
        """
        if not head : return None 
        end = head
        cur = head

        if head.next: cur = head.next
        else: return head

        head.next = None 
        if cur.next: end = cur.next
        else:  
            cur.next = head 
            head.next = None
            return cur  
        
        while end: 
            cur.next = head
            head = cur 
            cur = end 

            if not end.next: 
                break
            else: 
                end = end.next 

        end.next = head 
        
        return end 
        """

        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

        


        

list0 = None 
list1 = ListNode(1)
list2 = ListNode(1,ListNode(2))
list3 = ListNode(1,ListNode(2, ListNode(3)))
list4 = ListNode(1,ListNode(2, ListNode(3, ListNode(4))))

for i in [list1,list2,list3,list4]: 
    x =Solution().reverseList(i)
    print(x.val)
