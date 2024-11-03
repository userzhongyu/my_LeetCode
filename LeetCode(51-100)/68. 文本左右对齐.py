import math
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        row = []
        exl, rel = 0, 0
        ans = []
        for item in words:
            if exl + len(item) <= maxWidth:
                row.append(item)
                rel += len(item)    # 单词真实长度
                exl += len(item) + 1    # 每个单词加上一个空格后的中长度
            elif len(row) == 1:
                temp = row[0]
                temp += (maxWidth - len(temp)) * ' '
                ans.append(temp)
                row = [item]
                rel = len(item)
                exl = len(item) + 1
            else:
                temp = ''
                row_len = len(row)
                space_count = maxWidth - rel
                # 处理前n-1个单词
                for i in range(0, len(row) - 1):
                    space = math.ceil(space_count / (row_len - 1))
                    temp += row[i] + ' ' * space
                    row_len -= 1
                    space_count -= space
                # 处理最后一个单词
                temp += row[-1]
                ans.append(temp)
                row = [item]
                rel = len(item)
                exl = len(item) + 1
        # 处理最后一行
        temp = ''
        for i in range(0, len(row) - 1):
            temp += row[i] + ' '
        temp += row[-1]
        temp += (maxWidth - len(temp)) * ' '
        ans.append(temp)
        return ans


def main():
    words = eval(input())
    maxWidth = int(input())
    print(Solution().fullJustify(words, maxWidth))


if __name__ == '__main__':
    main()