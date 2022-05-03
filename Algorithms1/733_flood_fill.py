"""
An image is represented by an m x n integer grid image where image[i][j] 
represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. 
You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, 
plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, 
plus any pixels connected 4-directionally to those pixels (also with the same color), 
and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.

 

Example 1:


Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
Output: [[2,2,2],[2,2,2]]
 

Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], newColor < 216
0 <= sr < m
0 <= sc < n

"""


class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]] -> image[i][j] 
        :type sr: int
        :type sc: int
        :type newColor: int 
        rtype List[List[int]]
        """
        # ideas
        # (sr,sc) is the starting location, so need to check (sr+1, sc), (sr-1, sc), (sr, sc+1), (sr, sc-1) from every point
        # write a diffrent function that can do this and be called,
        # if a function = sr,sc then pass through to diffrent one
        m, n = len(image), len(image[0])
        startColor = image[sr][sc]

        if newColor == startColor:
            return image

        def aroundFill(i, j):
            if image[i][j] == startColor:
                image[i][j] = newColor
                if i+1 < m: aroundFill(i+1, j)
                if i-1 >= 0: aroundFill(i-1, j)
                if j+1 < n: aroundFill(i, j+1)
                if j-1 >= 0: aroundFill(i, j-1)

        aroundFill(sr, sc)

        return image

    def floodFillprint(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]] -> image[i][j] 
        :type sr: int
        :type sc: int
        :type newColor: int 
        rtype List[List[int]]
        """
        # ideas
        # (sr,sc) is the starting location, so need to check (sr+1, sc), (sr-1, sc), (sr, sc+1), (sr, sc-1) from every point
        # write a diffrent function that can do this and be called,
        # if a function = sr,sc then pass through to diffrent one
        m = len(image)
        n = len(image[0])
        startColor = image[sr][sc]

        if newColor == startColor:
            return image

        def aroundFill(i, j):
            print(i, j, 0)
            if image[i][j] != startColor:
                print("its not the start color")
                return
            image[i][j] = newColor
            if i+1 < m:
                print(i+1, j, 1)
                aroundFill(i+1, j)
            if i-1 >= 0:
                print(i-1, j, 2)
                aroundFill(i-1, j)
            if j+1 < n:
                print(i, j+1, 3)
                aroundFill(i, j+1)
            if j-1 >= 0:
                print(i, j-1, 4)
                aroundFill(i, j-1)

        aroundFill(sr, sc)

        return image


if __name__ == "__main__":
    
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newColor = 2
    """
    image = [[0, 0, 0], [0, 1, 1]]
    sr = 1
    sc = 1
    newColor = 1
    """
    print(len(image))
    print(len(image[0]))
    print(Solution().floodFill(image, sr, sc, newColor))
