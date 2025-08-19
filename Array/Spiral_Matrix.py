class Solution(object):
    def spiralOrder(self, matrix):
        n = len(matrix)  # rows
        m = len(matrix[0])  # columns

         #track of the current outer layer of the matrix we are working on.
        top, bottom = 0, n - 1
        left, right = 0, m - 1

        result = []

        while left <= right and top <= bottom:
            # Traverse left to right 
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # Traverse top to bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # Traverse bottom right to left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            # Traverse left column bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result

        