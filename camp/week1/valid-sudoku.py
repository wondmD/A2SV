class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        sub_boxes = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                if num in rows[i]:
                    return False
                rows[i].add(num)
                if num in columns[j]:
                    return False
                columns[j].add(num)
                box_row = i // 3
                box_col = j // 3
                if num in sub_boxes[box_row][box_col]:
                    return False
                sub_boxes[box_row][box_col].add(num)

        return True