class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()  # 删除首尾空格
        s = s.split()  # 分割字符串，将会删除所有长度的空格
        s = s[:: -1]  # 翻转单词列表
        return ' '.join(s)  # 拼接为字符串并返回


def main():
    s = "a good   example"
    # s = "EPY2giL"
    print(Solution().reverseWords(s))


if __name__ == '__main__':
    main()
