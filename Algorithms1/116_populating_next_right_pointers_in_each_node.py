"""
You are given a perfect binary tree where all leaves are on the same level,
and every parent has two children.
The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.



Example 1:


Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A),
your function should populate each next pointer to point to its next right node,
just like in Figure B. The serialized output is in level order as connected by
the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 212 - 1].
-1000 <= Node.val <= 1000


Follow-up:

You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count
as extra space for this problem.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""




from collections import deque
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        """
        # solution one from post  https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/1654181/C%2B%2BPythonJava-Simple-Solution-w-Images-and-Explanation-or-BFS-%2B-DFS-%2B-O(1)-Optimized-BFS
        # all we have to do is set the pointers
        # this uses a bredth first search
        if not root:
            return None #if there is no root, return none
        q = deque([root])  #initalizes the queue with the start node

        while q:
            rightNode = None #initialise the right node of every level as none
            # this is initally, 1, 2, 4, 8 ext as its a perfect tree until it hits the correct depth
            for _ in range(len(q)):
                cur = q.popleft() #cur is our current positon, start by taking from the top of the list
                cur.next = rightNode #initaly set to None for the furtherst right
                rightNode = cur #move the right node to be
                if cur.right:
                    #adds the cur.rightnode and cur.leftnode to the queue. we are placing the right before the left.
                    q.extend([cur.right, cur.left])

        return root
        """
        """
        # solution 2 from post https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/1654181/C%2B%2BPythonJava-Simple-Solution-w-Images-and-Explanation-or-BFS-%2B-DFS-%2B-O(1)-Optimized-BFS
        # this uses a dfs depth first search method

        if not root:
            return None

        L, R, N = root.left, root.right, root.next
        if L:  # if L exists, then right must exist
            L.next = R  # the next of the left node is the right node
            if N:
                R.next = N.left  # if next is not none then there is another node on this level
            self.connect(L) #sends to the left and start through again goes all the way through rhw depth on the left 
            self.connect(R)
        return root
        """
        """
        # solution3 combining both logics by doing bfs but placing the next on the child nodes 
        # this uses the facy all next values start as null 
        #start of line 
        #my version of it 
        if not root: return None 
        head = root
        lineStart = root 
        while root: 
          if root.left: 
            root.left.next = root.right
            if root.next: 
              root.right.next = root.next.left
              oldRoot = root
              root = root.next
            else:
              lineStart = lineStart.left
              root = lineStart 
          else:
            return head

        """
        
        #there version, better then mine. 
        if not root: return None
        head = root
        while root:
            cur, root = root, root.left
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                    if cur.next: cur.right.next = cur.next.left
                else: break
                cur = cur.next
                
        return head
      




        
              

  

seven, six, five, four = Node(7), Node(6), Node(5), Node(4)
three, two = Node(3, six, seven), Node(2, four, five)
one = Node(1, two, three)
root = one
allNodes = [one, two, three, four, five, six, seven]
x = Solution().connect(one)
print(x.val, x.next)
for i in allNodes:
    print(i.val, i.next)
