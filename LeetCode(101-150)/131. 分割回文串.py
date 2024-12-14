from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def judge(_s):
            return _s == _s[:: -1]

        def dfs(path, _s):
            if not _s:
                ans.append(path)
                return
            for left in range(1, len(_s) + 1):
                if judge(_s[:left]):
                    dfs(path + [_s[:left]], _s[left:])

        dfs([], s)
        return ans
#
# class Solution(object):
#     def partition(self, s):
#         self.isPalindrome = lambda s: s == s[::-1]
#         res = []
#         self.backtrack(s, res, [])
#         return res
#
#     def backtrack(self, s, res, path):
#         if not s:
#             res.append(path)
#             return
#         for i in range(1, len(s) + 1):  # 注意起始和结束位置
#             if self.isPalindrome(s[:i]):
#                 self.backtrack(s[i:], res, path + [s[:i]])


def main():
    s = "aab"
    # s = "a"
    # s = "bb"
    print(Solution().partition(s))


if __name__ == '__main__':
    main()
