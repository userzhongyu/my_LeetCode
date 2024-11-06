class Solution:
    def numDecodings(self, s: str) -> int:
        ans = 0
        num = [int(i) for i in s]
        while num:
            path = []
            i = 0
            # 一次判断
            while i < len(num):
                if num[i] != 0 and i+1 < len(num) and num[i]*10+num[i+1] <= 26 and (i+2 >= len(num) or num[i+2] != 0):
                    path.append((num[i]*10+num[i+1]))
                    i += 2
                elif num[i] != 0:
                    path.append(num[i])
                    i += 1
                else:
                    break
            # 整个字符串编译完成
            if i >= len(num):
                ans += 1
                print(path)
            # 将num[0]编译成字母,如果 num[0] == 0 上述循环和判断直接跳出
            num = num[1:]
        return ans


def main():
    s = '11106'
    print(Solution().numDecodings(s))


if __name__ == '__main__':
    main()
