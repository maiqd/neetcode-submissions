class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        squareMap = defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board[row])):
                val = board[row][col]
                if val == '.':
                    continue
                
                if val in rowMap[row] or val in colMap[col] or val in squareMap[tuple([row//3, col//3])]:
                    return False

                rowMap[row].add(val)
                colMap[col].add(val)
                squareMap[tuple([row//3, col//3])].add(val)
        return True