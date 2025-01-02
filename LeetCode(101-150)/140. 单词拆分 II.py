from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        path = []
        self.dfs(s, wordDict, path,  ans)
        return ans

    def dfs(self, s: str, wordDict: list, path: list, ans: list):
        if s == '':
            temp = ' '.join(path)
            ans.append(temp)
            return

        for i in range(len(s)):
            if s[:i + 1] in wordDict:
                path.append(s[:i + 1])
                self.dfs(s[i + 1:], wordDict, path, ans)
                path.pop()


def main():
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    # s = "pineapplepenapplepineapplepenapple"
    # wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    # s = "catsandog"
    # wordDict = ["cats", "dog", "sand", "and", "cat"]
    # s = "c"
    # wordDict = ["c", "dog", "sand", "and", "cat"]
    print(Solution().wordBreak(s, wordDict))


if __name__ == '__main__':
    main()
