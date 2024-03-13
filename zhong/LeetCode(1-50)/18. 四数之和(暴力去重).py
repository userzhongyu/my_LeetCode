"""
列表排序
双指针选择性移动
"""


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        temp = []
        res = []
        if len(nums) < 4:
            return res
        # 数组去重
        # 排序
        nums.sort()
        n = len(nums)
        for i in range(0, n - 3):
            for j in range(i + 1, n - 2):
                k = j + 1
                l = n - 1
                while k < l:
                    my_sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if my_sum == target:
                        temp.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                    elif my_sum < target:
                        k += 1
                    else:
                        l -= 1
        # 去重
        for i in range(0, len(temp)):
            flag = True
            for j in range(0, len(res)):
                if set(temp[i]) == set(res[j]):
                    flag = False
                    break
            if flag:
                res.append(temp[i])
        return res


def main():
    nums = eval(input())
    target = int(input())
    ob = Solution()
    print(ob.fourSum(nums, target))


if __name__ == '__main__':
    main()
