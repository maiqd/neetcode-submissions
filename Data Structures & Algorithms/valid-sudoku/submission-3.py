class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHashMap = defaultdict(set)
        colHashMap = defaultdict(set)
        boxHashMap = defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == '.':
                    continue
                if board[row][col] in rowHashMap[row]:
                    print(board[row][col])
                    return False
                if board[row][col] in colHashMap[col]:
                    return False
                if board[row][col] in boxHashMap[(row//3, col//3)]:
                    return False
                rowHashMap[row].add(board[row][col])
                colHashMap[col].add(board[row][col])
                boxHashMap[(row//3, col//3)].add(board[row][col])
        return True