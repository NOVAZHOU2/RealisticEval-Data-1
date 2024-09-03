"""
To improve, separate the DFS logic for better readability and maintainability.
Note the the interative soln is almost two times slower than ChatGPT's recursive soln. This could be inefficient calculation of values?

Time Complexity: -- INCORRECT
O(m * n * log(m *n))
O(n^2 * log(n^2)) where n = max(m, n)

Time Complexity:
O(m * n)
O(n^2) where n = max(m, n)
Because of memoization, each cell value only needs to be calculated once, and there are at most m * n cells

Space Complexity:
O(m * n)
O(n^2) where n = max(m, n)

https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

#dfs #stack #2024
"""

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        self.m = len(matrix)
        self.n = len(matrix[0])

        result = 0
        dp = {}  # O(m * n) space
        move = (
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        )

        # loop through all cells bc the path can start anywhere
        # O(m * n) time
        for i in range(self.m):
            for j in range(self.n):
                if (i, j) in dp:
                    continue
                
                stack = [(i, j)]  # start the DFS

                while len(stack) != 0:
                    x = stack[-1][0]
                    y = stack[-1][1]

                    dp[(x, y)] = 1  # init longest increasing path w/ itself
                    
                    for xMove, yMove in move:
                        xNew = x + xMove
                        yNew = y + yMove

                        if (
                            self.inBounds(xNew, yNew) and
                            matrix[x][y] < matrix[xNew][yNew]
                        ):
                            if (xNew, yNew) in dp:
                                dp[(x, y)] = max(dp[(x, y)], dp[(xNew, yNew)] + 1)
                            else:
                                stack.append((xNew, yNew))
                    
                    if stack[-1] == (x, y):  # only execute this logic if all paths have been explored
                        result = max(result, dp[(x, y)])
                        stack.pop()

        return result

    def inBounds(self, i, j):
        return i >= 0 and j >= 0 and i < self.m and j < self.n




"""
Recursive solution generated by ChatGPT
"""

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        m = len(matrix)
        n = len(matrix[0])

        dp = {}
        move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x, y):
            if (x, y) in dp:
                return dp[(x, y)]

            max_path = 1

            for dx, dy in move:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
                    max_path = max(max_path, 1 + dfs(nx, ny))

            dp[(x, y)] = max_path

            return max_path

        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j))

        return result