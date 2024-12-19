from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        n = len(cost)
        ans = 0
        sub = [g - c for g, c in zip(gas, cost)]
        buffer = 0
        min_bf = 0

        # 由于答案唯一，所以
        # 找出累计耗油最大的站台，从该站台之后开始 汽油都有剩余
        for i in range(n):
            buffer += sub[i]
            if buffer < min_bf:
                min_bf = buffer
                ans = i + 1
        return ans


def main():
    # gas = [1, 2, 3, 4, 5]
    # cost = [3, 4, 5, 1, 2]
    gas = [2, 3, 4]
    cost = [3, 4, 3]
    # gas = [2]
    # cost = [2]
    print(Solution().canCompleteCircuit(gas, cost))


if __name__ == '__main__':
    main()
