"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange 
becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a 
fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) 
is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, 
the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""
from numpy import ones
from collections import deque 

class Solution:
    def orangesRotting(self, grid):

        #number of rows 
        m = len(grid)
        #number of columns 
        n = len(grid[0])

        #keep a total number of fresh oranges 
        fresh = 0 

        #queue with rotten oranges (for BFS) 
        rotten = deque() 

        for i in range(m):
            for j in range(n):

                if grid[i][j] == 2: 
                    # add the rotten oranges coordinates to the queue 
                    rotten.append((i,j))
                elif grid[i][j] == 1: 
                    #update the number of fresh oranges 
                    fresh += 1 

        #we now have a queue of all the rotten oranges and the number of fresh ornages 
        #keep track of mins passed 
        mins = 0 

        #if rotten still in queue and fresh still in grid keep looping 
        while rotten and fresh > 0: 

            mins += 1 
            
            # process rotten oranges on the current level 
            for _ in range(len(rotten)):
                x , y = rotten.popleft() 

                #look at the adjacent cells 
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]: 
                    #calculate the coordinates of the adacent cell 
                    xx, yy = x+dx, y+dy 

                    # ignore the cell if it is out of the grid boundrys 
                    if xx < 0 or xx == m or yy < 0 or yy == n:
                        continue 

                                        # ignore the cell if it is empty '0' or visited before '2'
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue
                        
                    # update the fresh oranges count
                    fresh -= 1
                    
                    # mark the current fresh orange as rotten
                    grid[xx][yy] = 2
                    
                    # add the current rotten to the queue
                    rotten.append((xx, yy))

        
        # return the number of minutes taken to make all the fresh oranges to be rotten
        # return -1 if there are fresh oranges left in the grid (there were no adjacent rotten oranges to make them rotten)
        return mins if fresh == 0 else -1

        #this was taken from https://leetcode.com/problems/rotting-oranges/discuss/563686/Python-Clean-and-Well-Explained-(faster-than-greater-90)


grid = [[2,1,1],[1,1,0],[0,1,1]]
print(Solution().orangesRotting(grid))










