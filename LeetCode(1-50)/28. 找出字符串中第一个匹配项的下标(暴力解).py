"""
暴力解
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res = -1
        n = len(haystack)
        for i in range(0, n):
            k = 0
            flag = True
            for j in range(0, len(needle)):
                if i + j < n and haystack[i + j] == needle[k]:
                    k += 1
                else:
                    flag = False
                    break
            if flag:
                res = i
                break
        return res


def main():
    haystack = input()
    needle = input()
    ob = Solution()
    print(ob.strStr(haystack, needle))


if __name__ == '__main__':
    main()
