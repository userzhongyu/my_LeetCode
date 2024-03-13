class Solution:
    def longestValidParentheses(self, s: str) -> int:
        s = list(s)
        res = 0
        stack = []
        top = -1
        # 添加辅助栈,将可以匹配的部分字符串置为0
        for i in range(0, len(s)):
            if s[i] == '(':
                top += 1
                stack.append(i)
            elif s[i] == ')' and top > -1:
                s[stack[top]:i + 1] = [0] * (i + 1 - stack[top])
                stack.pop()
                top -= 1
        # # 将其余部分置为1
        #     else:
        #         s[i] = 1
        # for i in range(0, len(stack)):
        #     s[stack[i]] = 1
        # print(s)
        temp = 0
        for i in range(0, len(s)):
            # 记录连续的0的最大长度
            if s[i] == 0:
                temp += 1
            # 出现中断,记录长度
            else:
                res = max(res, temp)
                temp = 0
        # 可能0一直连续到结尾
        return max(res, temp)


def main():
    ob = Solution()
    s = input()
    print(ob.longestValidParentheses(s))


if __name__ == '__main__':
    main()
