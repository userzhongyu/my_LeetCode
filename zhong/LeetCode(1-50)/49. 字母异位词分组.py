"""
C V
键值对的使用
"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = dict()
        res = []
        for s in strs:
            key = ''.join(sorted(list(s)))  # 将字符串按位排序
            # key对应的值为列表
            if key in hashtable:
                hashtable[key].append(s)
            else:
                hashtable[key] = [s]
        for key, value in hashtable.items():
            res.append(value)
        return res


def main():
    strs = eval(input())
    print(Solution().groupAnagrams(strs))


if __name__ == '__main__':
    main()