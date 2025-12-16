# Solution is O(n^2) time and O(1) time for sumRegion. Space is O(n^2)

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        self.cdf = []

        for row in range(len(matrix)):
            c = [matrix[row][0]]
            for col in range(1, len(matrix[0])):
                c.append(matrix[row][col] + c[col - 1])
            self.cdf.append(c)
        
        for col in range(len(matrix[0])):
            for row in range(1, len(matrix)):
                self.cdf[row][col] += self.cdf[row-1][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.call_cdf(row2, col2) - self.call_cdf(row2, col1-1) - self.call_cdf(row1-1,col2) + self.call_cdf(row1-1,col1-1)
    
    def call_cdf(self, i, j):
        if (i < 0 or j < 0):
            return 0
        return self.cdf[i][j]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
