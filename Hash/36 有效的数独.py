# 在一次迭代中完成对行、列、子数独的检查


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for _ in range(9)]
        columns = [{} for _ in range(9)]
        boxes = [{} for _ in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    # 字典(Dictionary) get() 函数返回指定键的值，如果值不在字典中返回默认值。dict.get(key, default=None)
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[(i // 3) * 3 + j // 3][num] = boxes[(i // 3) * 3 + j // 3].get(num, 0) + 1
                    # 加入字典后，判断是否有效
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[(i // 3) * 3 + j // 3][num] > 1:
                        return False
        return True