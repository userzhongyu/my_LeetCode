class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ''
        for i in range(0, len(s)):
            if len(s) - i < len(t):
                break
            temp = list(t)
            if s[i] in temp:
                for j in range(i, len(s)):
                    if j - i > len(ans) > 0:
                        break
                    if s[j] in temp:
                        temp.remove(s[j])
                    if not temp:
                        ans = s[i: j + 1] if ans == '' or j - i < len(ans) else ans
                        break
        return ans


def main():
    s = eval(input())
    t = eval(input())
    print(Solution().minWindow(s, t))


if __name__ == '__main__':
    main()