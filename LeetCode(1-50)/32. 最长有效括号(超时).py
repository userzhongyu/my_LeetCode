class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        # 从后向前检查,左闭右开
        for end in range(len(s), 1, -1):
            for start in range(0, end):
                # 剪枝1:长度必需为偶数
                if (end - start) % 2:
                    continue
                # 剪枝2:最大长度单调不减
                if s[end - 1] != ')' or end - start <= res:
                    break
                if self.isMatch(s, start, end):
                    res = max(res, end - start)
                    end += 1
        return res

    # 判断字符串s[start,end]中括号是否匹配
    def isMatch(self, s: str, start: int, end: int) -> bool:
        count = 0
        for i in range(start, end):
            if s[i] == '(':
                count += 1
            else:
                count -= 1
            if count < 0:
                return False
        if count == 0:
            return True
        else:
            return False


def main():
    ob = Solution()
    s = input()
    print(ob.longestValidParentheses(s))


if __name__ == '__main__':
    main()
