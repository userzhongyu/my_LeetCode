from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        stack = []
        for i in range(n):
            if tokens[i] != '+' and tokens[i] != '-' and tokens[i] != '*' and tokens[i] != '/':
               stack.append(int(tokens[i]))
            else:
                o2 = stack.pop()
                o1 = stack.pop()
                if tokens[i] == '+':
                    res = o1 + o2
                elif tokens[i] == '-':
                    res = o1 - o2
                elif tokens[i] == '*':
                    res = o1 * o2
                else:
                    res = int(o1 / o2)
                stack.append(res)
        return stack.pop()


def main():
    tokens = ["2","1","+","3","*"]
    tokens = ["4", "13", "5", "/", "+"]
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    res = Solution().evalRPN(tokens)
    print(res)


if __name__ == '__main__':
    main()
