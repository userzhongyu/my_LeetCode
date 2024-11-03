"""
作者：Mcdull
链接：https: // leetcode.cn / problems / minimum - window - substring / solutions / 258513 / tong - su - qie - xiang - xi - de - miao - shu - hua - dong - chuang - k /
来源：力扣（LeetCode(1-50)）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        needCnt = len(t)
        i = 0
        res = (0, float('inf'))  # 正无穷
        for j, c in enumerate(s):
            if need[c] > 0:
                needCnt -= 1
            need[c] -= 1
            if needCnt == 0:  # 步骤一：滑动窗口包含了所有T元素
                while True:  # 步骤二：增加i，排除多余元素
                    c = s[i]
                    if need[c] == 0:
                        break
                    need[c] += 1
                    i += 1
                if j - i < res[1] - res[0]:  # 记录结果
                    res = (i, j)
                need[s[i]] += 1  # 步骤三：i增加一个位置，寻找新的满足条件滑动窗口
                needCnt += 1
                i += 1
        return '' if res[1] > len(s) else s[res[0]:res[1] + 1]  # 如果res始终没被更新过，代表无满足条件的结果



def main():
    s = eval(input())
    t = eval(input())
    print(Solution().minWindow(s, t))


if __name__ == '__main__':
    main()
