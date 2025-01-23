class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # 分段
        version1 = version1.split('.')
        version2 = version2.split('.')

        # 转换成数字
        version1 = [int(num) for num in version1]
        version2 = [int(num) for num in version2]

        # 去除末尾的 0
        while version1 and version1[-1] == 0:
            version1.pop()
        while version2 and version2[-1] == 0:
            version2.pop()

        # 循环比较每一位的数字大小
        for v1, v2 in zip(version1, version2):
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1

        # 处理 version1 和 version2 长度不同的情况
        if len(version1) == len(version2):
            return 0
        elif len(version1) > len(version2):
            return 1
        else:
            return -1

def main():
    version1 = "1.2"
    version2 = "1.10"  # -1
    # version1 = "1.01"
    # version2 = "1.001"  # 0
    # version1 = "1.0"
    # version2 = "1.0.0.0"  # 0
    print(Solution().compareVersion(version1, version2))


if __name__ == '__main__':
    main()
