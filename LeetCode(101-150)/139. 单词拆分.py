from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]


def main():
    # s = "leetcode"
    # wordDict = ["leet", "code"]
    # s = "catsandog"
    # wordDict = ["cats", "dog", "sand", "and", "cat"]
    # s = "a"
    # wordDict = ["a"]
    # s = "ab"
    # wordDict = ["a"]
    # s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # wordDict = ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", "ba"]
    print(Solution().wordBreak(s, wordDict))


if __name__ == '__main__':
    main()
