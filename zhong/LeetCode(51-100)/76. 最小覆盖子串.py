class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic = {key: 0 for key in t}
        # 记录字符串t中各字母数量
        for c in t:
            dic[c] += 1
        i = 0
        j = 0
        len_s = len(s)
        len_t = len(t)
        # 返回值的初始窗口足够大
        ans = (0, float('inf'))
        # j后移
        while j < len_s:
            if s[j] in t:
                if dic[s[j]] > 0:
                    len_t -= 1
                dic[s[j]] -= 1
            j += 1
            # 包含全部的t
            if len_t == 0:
                # i后移
                while i < j:
                    if s[i] not in t:
                        i += 1
                    # 窗口内存在多余的字母
                    elif dic[s[i]] < 0:
                        dic[s[i]] += 1
                        i += 1
                    # i值不可移动
                    else:
                        if ans[1] - ans[0] > j - i:
                            ans = (i, j)
                            # 下一个窗口
                            dic[s[i]] += 1
                            i += 1
                            len_t += 1
                        break
        # 如果返回值未被修改,则说明字符串s中不包含完整的字符串t
        return '' if ans == (0, float('inf')) else s[ans[0]: ans[1]]


def main():
    s = eval(input())
    t = eval(input())
    print(Solution().minWindow(s, t))


if __name__ == '__main__':
    main()
