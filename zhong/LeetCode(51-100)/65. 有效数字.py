class Solution:
    def isNumber(self, s: str) -> bool:
        index = s.find('e')
        if index == -1:
            index = s.find('E')
        if index == -1:
            return self.isInt(s) or self.isFloat(s)
        pre = s[0: index]
        suf = s[index + 1:]
        return (self.isInt(pre) or self.isFloat(pre)) and self.isInt(suf)

    def isInt(self, s):
        if s.startswith('+') or s.startswith('-'):
            s = s[1:]
        n = len(s)
        if n < 1:
            return False
        for i in range(0, n):
            # 判断字符是否被包含在特定字符集
            if s[i] not in [x for x in '0123456789']:
                return False
        return True

    def isFloat(self, s):
        if s.startswith('+') or s.startswith('-'):
            s = s[1:]
        index = s.find('.')
        if index != -1:
            s = s[0: index] + s[index + 1:]
        n = len(s)
        if n < 1:
            return False
        for i in range(0, n):
            if s[i] not in [x for x in '0123456789']:
                return False
        return True


def main():
    s = eval(input())
    print(Solution().isNumber(s))


if __name__ == '__main__':
    main()