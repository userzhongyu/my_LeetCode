from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        path = []

        def dfs(__ans, __path, index: int):
            if len(path) > 4:
                return
            if len(__path) == 4 and index == len(s):
                __ans.append('.'.join(__path[:]))
                return
            # 检查随后的连续3个数字
            for i in range(1, 4):
                tmp = s[index: index+i]  # 切出需要进行判断的数字组合
                if tmp and 0 <= int(tmp) <= 255 and str(int(tmp)) == tmp:  # 判断当前数字组合能否当做一个段地址
                    path.append(tmp[:])
                    dfs(__ans, __path, index+i)  # 深入
                    path.pop()  # 恢复现场

        dfs(ans, path, 0)
        return ans


def main():
    # s = "25525511135"
    s = '0000'
    # s = "101023"
    print(Solution().restoreIpAddresses(s))


if __name__ == '__main__':
    main()
