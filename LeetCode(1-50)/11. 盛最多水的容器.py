class Solution:
    def maxArea(self, height: list[int]) -> int:
        v = 0
        i = 0
        j = len(height) - 1
        while i < j:
            if height[i] < height[j]:
                v = max(v, (j - i) * height[i])
                i += 1
            else:
                v = max(v, (j - i) * height[j])
                j -= 1
        return v


def main():
    lst = eval(input())
    # print(lst)
    # print(type(lst))
    ob = Solution()
    print(ob.maxArea(lst))


if __name__ == '__main__':
    main()