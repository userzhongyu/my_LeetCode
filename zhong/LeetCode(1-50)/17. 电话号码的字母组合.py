"""
创建字典
创建临时变量存储输入的每一位对应字母集中一个字母,并依次拼接上下一位输入对应的所有字母
"""
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        digits = str(eval(digits))
        if digits == '' or len(digits) > 4:
            return []
        n = len(digits)
        dic = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        res = dic[digits[0]]
        for i in range(1, n):
            res = mix(res, dic[digits[i]])
        return res


# 实现两个列表的拼接
def mix(lst1, lst2):
    res = []
    for i in range(0, len(lst1)):
        for j in range(0, len(lst2)):
            temp = lst1[i] + lst2[j]
            res.append(temp)
    return res


def main():
    digits = input()
    ob = Solution()
    print(ob.letterCombinations(digits))


if __name__ == '__main__':
    main()