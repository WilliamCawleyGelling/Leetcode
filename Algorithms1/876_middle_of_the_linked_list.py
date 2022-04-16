"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100


"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #make two poibters skiw abd fast. 
        #let fast travel at double the speed of slow 
        #if they both move one step then when fast ends slow will be in the middle 
        #put a if not head check in 

        if not head: 
            return None 
        
        slow = head
        fast = head 
        while fast and fast.next: #while these can happen and the link list has not ended 
            slow = slow.next
            fast = fast.next.next
        return slow


























        # Solution 1:
        # if not head:
        #     return None
        # slow = head
        # fast = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # return slow
        
        # Solution 2:
        # if not head:
        #     return None
        # slow = head
        # fast = head
        # while fast.next and fast.next.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # return slow
        
        # Solution 3:
        # if not head:
        #     return None
        # slow = head
        # fast = head
        # while fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # return slow
        
        # Solution 4:
        # if not head:
        #     return None
        # slow = head
        # fast = head
        # while fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # return slow
        
        # Solution 5:
        # if not head:
        #     return None
        # slow = head
        # fast = head
        # while fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # return slow
        
        # Solution 6:
        # if not head:
        #     return None
        # slow = head
        # fast = head
        # while fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # return slow
        
        # Solution 7:
        # if not head:
        #     return None
        # slow = head
        # fast = head
        # while fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # return slow
        
        # Solution 8:
        # if not head:
        #     return None