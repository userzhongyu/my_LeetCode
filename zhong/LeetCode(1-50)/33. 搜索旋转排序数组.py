class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # 左边有序
            if nums[left] <= nums[mid]:
                # target 位于左边有序段中(包含左右端点)
                # right左移至mid处(若移至mid - 1处,当target等于nums[mid]时,漏解)
                if nums[left] <= target <= nums[mid]:
                    right = mid
                # target 位于右边含旋转数组的部分,left右移
                else:
                    left = mid + 1
            # 右边有序
            else:
                # target 位于右边有序段中(包含左右端点)
                # left右移至mid处(若移至mid + 1处,当target等于nums[mid]时,漏解)
                if nums[mid] <= target <= nums[right]:
                    left = mid
                # target 位于左边含旋转数组的部分,right左移
                else:
                    right = mid - 1
        if left == right and nums[left] == target:
            return left
        else:
            return -1


def main():
    nums = eval(input())
    target = int(input())
    ob = Solution()
    print(ob.search(nums, target))


if __name__ == '__main__':
    main()
