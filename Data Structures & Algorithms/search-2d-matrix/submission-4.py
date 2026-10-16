class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # matrix = [[1,3],[10,11]], target = 3
        # x=0, y=0, g=0
        x, y = 0, len(matrix)-1
        while x <= y:
            g = (x+y)//2
            if matrix[g][0] > target:
                y = g-1
            elif matrix[g][0] < target:
                x = g+1
            else:
                return True #whyyyyyyyyyyyy????????????
        if y < 0:
            return False
        k=y #whyy?
        x, y = 0, len(matrix[k])-1
        while x <= y:

            g = (x+y)//2
            if matrix[k][g] > target:
                y = g-1
            elif matrix[k][g] < target:
                x = g+1
            else:
                return True
        return False