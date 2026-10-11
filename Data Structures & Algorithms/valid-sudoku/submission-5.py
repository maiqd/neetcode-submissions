class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowDic = defaultdict(set)
        colDic = defaultdict(set)
        boxDic = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[row])):
                num = board[row][col]
                if num == ".":
                    continue

                if num in rowDic[row] or num in colDic[col] or num in boxDic[tuple([row // 3, col // 3])]:
                    return False

                rowDic[row].add(num)
                colDic[col].add(num)
                boxDic[tuple([row // 3, col // 3])].add(num)

        return True
