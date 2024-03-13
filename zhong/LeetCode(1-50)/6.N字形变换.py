class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = len(s)
        if numRows <= 1:
            return s
        lst = [[''] * l for _ in range(0, numRows)]
        # print(lst)
        index = 0
        i = 0
        j = 0
        while index < l:
            while i < numRows - 1 and index < l:
                lst[i][j] = s[index]
                index += 1
                # 向下到底
                i += 1
            while i > 0 and index < l:
                lst[i][j] = s[index]
                index += 1
                # 向右上到顶
                i -= 1
                j += 1
        str_out = ''
        for i in range(0, numRows):
            for j in range(0, l):
                if lst[i][j] != '':
                    str_out += (lst[i][j])
        return str_out

def main():
    s = eval(input())
    num = int(input())
    print(Solution().convert(s, num))



if __name__ == '__main__':
    main()
