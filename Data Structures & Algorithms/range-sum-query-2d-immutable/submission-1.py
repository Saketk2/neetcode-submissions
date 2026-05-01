class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = []
        for row in matrix:
            temp = [row[0]]
            for val in row[1:]:
                temp.append(temp[-1] + val)
            self.prefix.append(temp.copy())
        print(self.prefix)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for i in range(row1, row2 + 1):
            total += self.prefix[i][col2] - self.prefix[i][col1 - 1] if col1 > 0 else self.prefix[i][col2]
        return total

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)