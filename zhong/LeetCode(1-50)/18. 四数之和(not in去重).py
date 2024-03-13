"""
列表排序
双指针选择性移动
由于列表经过排序,所以所含元素相同的列表,其元素位置也相同
"""


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        res= []
        if len(nums) < 4:
            return res
        # 数组去重
        # 排序
        nums.sort()
        n = len(nums)
        for i in range(0, n - 3):
            # 极大缩短程序耗时
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if sum(nums[i:i + 4]) > target:
                break
            if nums[i] + sum(nums[n - 3:]) < target:
                continue
            for j in range(i + 1, n - 2):
                k = j + 1
                l = n - 1
                while k < l:
                    my_sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if my_sum == target:
                        # not in函数去重
                        if [nums[i], nums[j], nums[k], nums[l]] not in res:
                            res.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        while nums[k] == nums[k - 1] and k < l:
                            k += 1
                        l -= 1
                        while nums[l] == nums[l + 1] and k < l:
                            l -= 1
                    elif my_sum < target:
                        k += 1
                    else:
                        l -= 1
        return res


def main():
    nums = eval(input())
    target = int(input())
    ob = Solution()
    print(ob.fourSum(nums, target))


if __name__ == '__main__':
    main()
