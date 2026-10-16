class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # loop as 1d array
        x, y = 0, len(matrix)*len(matrix[0])-1
        while x <= y:
            g = (x+y)//2
            if matrix[g//len(matrix[0])][g%len(matrix[0])] < target:
                x = g+1
            elif matrix[g//len(matrix[0])][g%len(matrix[0])] > target:
                y = g-1
            else:
                return True
        return False