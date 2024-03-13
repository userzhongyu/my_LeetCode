class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i in range(0, len(s)):
            lst = []
            for j in range(i, len(s)):
                if s[j] not in lst:
                    lst.append(s[j])
                else:
                    break
            longest = longest if longest > len(lst) else len(lst)
        return longest


def main():
    s = eval(input())
    sol = Solution()
    longeset = sol.lengthOfLongestSubstring(s)
    print(longeset)


if __name__ == '__main__':
    main()
