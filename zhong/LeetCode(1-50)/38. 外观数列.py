class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        s = self.countAndSay(n - 1)
        s = [i for i in s]
        s.append('-1')  # 哨兵
        res = []
        # 计算并添加字符
        count = 1
        for i in range(0, len(s) - 1):
            # 字符不连续
            if s[i] != s[i + 1]:
                res.append(str(count))
                res.append(s[i])
                count = 1
            # 字符连续
            else:
                count += 1
        res = ''.join(res)
        return res


def main():
    n = int(input())
    ob = Solution()
    print(ob.countAndSay(n))


if __name__ == '__main__':
    main()

