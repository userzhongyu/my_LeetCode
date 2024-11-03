"""
检查3*3:基地址加偏移量
"""
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(0, 9):
            temp_row = []
            temp_col = []
            for j in range(0, 9):
                # 检查行
                if board[i][j] != '.':
                    if board[i][j] not in temp_row:
                        temp_row.append(board[i][j])
                    else:
                        return False
                # 检查列
                if board[j][i] != '.':
                    if board[j][i] not in temp_col:
                        temp_col.append(board[j][i])
                    else:
                        return False
        # 检查3*3
        base_i = 0  # 行的基地址
        while base_i < 9:
            base_j = 0  # 列的基地址
            while base_j < 9:
                temp = []
                # 检查一个3*3
                # i为行的偏移量,j为列的偏移量
                for i in range(0, 3):
                    for j in range(0, 3):
                        if board[base_i + i][base_j + j] != '.':
                            if board[base_i + i][base_j + j] not in temp:
                                temp.append(board[base_i + i][base_j + j])
                            else:
                                return False
                base_j += 3
            base_i += 3
        return True


def main():
    board = eval(input())
    ob = Solution()
    print(ob.isValidSudoku(board))


if __name__ == '__main__':
    main()
