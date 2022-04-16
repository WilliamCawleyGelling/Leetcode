"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""

# Definition for singly-linked list.
from tracemalloc import start
from turtle import end_fill


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        #settwo maybe three pointers, one at the start and one n further down  

        start = head 
        end = head 
        for i in range(0,n): 
            end = end.next 
        while end: 
            start.next 
            end.next

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #set two pointers, one at the start and one at the end 
        #move the end pointer n steps ahead 
        #when the end pointer hits the end of the list, the start pointer will be at the nth node from the end 
        #remove the start pointer 
        #return the head 
        if not head: 
            return None 
        start = head 
        end = head 
        for i in range(0,n): 
            end = end.next 
        if not end: 
            return head.next 
        while end.next: 
            start = start.next 
            end = end.next 
        start.next = start.next.next 
        return head


