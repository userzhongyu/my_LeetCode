class Solution:
    def longestPalindrome(self, s: str) -> str:
        my_len = len(s)
        j = 0
        k = 0
        max_str = ''
        if my_len == 1:
            max_str = s
            return max_str
        for index in [0, 1]:
            for i in range(0, my_len - 1):
                if index == 0:
                    j = i - 1
                else:
                    j = i
                k = i + 1
                while j >= 0 and k < my_len and s[j] == s[k]:
                    j -= 1
                    k += 1
                temp = s[j + 1:k]
                if len(max_str) < len(temp):
                    max_str = temp
        return max_str


def main():
    print(Solution.longestPalindrome())


if __name__ == '__main__':
    main()
