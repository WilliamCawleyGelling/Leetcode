"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""


class Solution:

    def maxAreaOfIsland(self, grid):
        """
        :type grid: list[list[int]]
        :rtype: int 
        """
        m = len(grid)  # y axis
        n = len(grid[0])  # x axis

        maxArea = 0
        coordinates = []  # using list but could use dictionary as quicker

        def findIsland(area, i, j):

            if i+1 < m and (i+1, j) not in coordinates:
                coordinates.append((i+1, j))
                if grid[i+1][j] == 1:
                    area = findIsland(area+1, i+1, j)
            if i-1 >= 0 and (i-1, j) not in coordinates:
                coordinates.append((i-1, j))
                if grid[i-1][j] == 1:
                    area = findIsland(area+1, i-1, j)
            if j+1 < n and (i, j+1) not in coordinates:
                coordinates.append((i, j+1))
                if grid[i][j+1] == 1:
                    area = findIsland(area+1, i, j+1)
            if j-1 >= 0 and (i, j-1) not in coordinates:
                coordinates.append((i, j-1))
                if grid[i][j-1] == 1:
                    area = findIsland(area+1, i, j-1)

            return area

        for i in range(m):
            for j in range(n):
                if (i, j) not in coordinates:
                    coordinates.append((i, j))
                    if grid[i][j] == 1:
                        area = 1
                        area = findIsland(area, i, j)
                        maxArea = max(maxArea, area)

        return maxArea

    #idea number 2, same again but replace the 1 with 0 once visited 
    #this method foes from 4353 ms to 163ms 
    def maxAreaOfIsland2(self, grid):
        """
        :type grid: list[list[int]]
        :rtype: int 
        """
        m = len(grid)  # y axis
        n = len(grid[0])  # x axis

        maxArea = 0

        def findIsland(area, i, j):

            if i+1 < m and grid[i+1][j] == 1:
                grid[i+1][j] = 0
                area = findIsland(area+1, i+1, j)
            if i-1 >= 0 and grid[i-1][j] == 1:
                grid[i-1][j] = 0
                area = findIsland(area+1, i-1, j)
            if j+1 < n and grid[i][j+1] == 1:
                grid[i][j+1] = 0
                area = findIsland(area+1, i, j+1)
            if j-1 >= 0 and grid[i][j-1] == 1:
                grid[i][j-1] = 0
                area = findIsland(area+1, i, j-1)
            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    area = 1
                    area = findIsland(area, i, j)
                    maxArea = max(maxArea, area)

        return maxArea

    def maxAreaOfIsland3(self, grid):
        """
        :type grid: list[list[int]]
        :rtype: int 
        """
        def findIsland(i,j):
            if not(0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]):
                return 0
            grid[i][j] = 0
            return (1+findIsland(i+1,j)+findIsland(i-1,j)+findIsland(i,j+1)+findIsland(i,j-1))

        return max(findIsland(i,j) for i in range(len(grid)) for j in range(len(grid[0])))







if __name__ == "__main__":
    
    area1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    exp1 = 6
    area2 = [[0,0,0,0,0,0,0,0]]
    exp2 = 0
    area3 = [[1]]
    exp3  = 1
    area4 = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
    exp4 = 4
    area5 = [[0]] 
    exp5 = 0
    for x, y in zip([area1, area2, area3, area4, area5], [exp1, exp2, exp3, exp4, exp5]):
        print(Solution().maxAreaOfIsland3(x),"the expected asnwer was ", y)
    
