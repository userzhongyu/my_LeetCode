"""
双指针
遍历数组,取三元组的和与target作差
"""


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        sub_min = 0xffffffff
        res = None
        nums.sort()
        n = len(nums)
        for i in range(0, n - 2):
            l = i + 1
            r = n - 1
            while l < r:
                temp = nums[i] + nums[l] + nums[r]
                sub = abs(temp - target)
                if sub == 0:
                    return temp
                elif sub < sub_min:
                    # 当前三数之和更加接近target
                    sub_min = sub
                    res = temp
                if temp < target:
                    # 三数之和比target小,左指针右移动
                    l += 1
                else:
                    # 三数之和比target小,右指针左移动
                    r -= 1
        return res


def main():
    while True:
        # 输入格式转换
        nums = eval(input())
        target = int(input())
        ob = Solution()
        print(ob.threeSumClosest(nums, target))


if __name__ == '__main__':
    main()