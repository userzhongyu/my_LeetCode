class Solution:
    def myAtoi(self, s: str) -> int:
        temp = '0'
        for i in range(0, len(s)):
            if s[i] in [' ', '"'] and temp == '0':
                continue
            elif s[i] in ['-', '+'] and temp == '0':
                temp = s[i]
            elif '0' <= s[i] <= '9':
                temp += s[i]
            else:
                break
        try:
            temp = int(temp)
        except:
            return 0
        if 2 ** 31 * -1 <= temp < 2 ** 31 - 1:
            return temp
        elif temp < 0:
            return 2 ** 31 * -1
        else:
            return 2 ** 31 - 1


def main():
    while True:
        s = input()
        print(Solution().myAtoi(s))


if __name__ == '__main__':
    main()
