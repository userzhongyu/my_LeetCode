"""
滑动窗口
在s中取长度为word的子串str1
如果str1在words中,则截取连续的len(words)个word组成lst
检查words中每个word是否都存在与lst中
"""
'''
测试用例
barfoothefoobarman
foo bar

lingmindraboofooowingdingbarrwingmonkeypoundcake
fooo barr wing ding wing
'''
class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        # 处理边界值
        if len(s) == len(words) and set(s) == set(words):
            return [0]
        n = len(words[0])
        i = 0
        res = []
        for i in range(0, len(s)):
            lst = []
            # 逐个字符判断,从第一个出现的word开始,截取连续的len(words)个word
            if s[i:i + n] in words:
                index = i
                count = 0
                while count < len(words):
                    lst.append(s[index:index + n])
                    index += n
                    count += 1
                # 判断所截取的字符串组是否包含words中全部的字符串
                flag = True
                for k in range(0, len(words)):
                    if words[k] not in lst:
                        flag = False
                        break
                    # 存在,则逐个删除元素->解决words中存在重复word问题
                    else:
                        lst.remove(words[k])
                if flag:
                    res.append(i)
        return res


def main():
    s = input()
    # words = input().split()
    words = input().replace('","', ' ')
    words = words.replace('"', '')
    words = words.split()
    ob = Solution()
    print(ob.findSubstring(s, words))


if __name__ == '__main__':
    main()
