from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        max_height_index = height.index(max(height))    # 最高的墙
        # 最高的墙左边
        i = 0
        while i < max_height_index:
            j = i + 1
            while j <= max_height_index:
                if height[j] < height[i]:
                    res -= height[j]
                else:
                    res += min(height[i], height[j]) * (j - i - 1)
                    break
                j += 1
            i = j
        # 最高的墙右边
        i = len(height) - 1
        while i > max_height_index:
            j = i - 1
            while j >= max_height_index:
                if height[j] < height[i]:
                    res -= height[j]
                else:
                    res += min(height[i], height[j]) * (i - j - 1)
                    break
                j -= 1
            i = j
        return res


def main():
    height = eval(input())
    ob = Solution()
    print(ob.trap(height))


if __name__ == '__main__':
    main()
