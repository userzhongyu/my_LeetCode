"""
从后向前 查找第一个 相邻升序 的元素对 (i,j)，满足 A[i] < A[j]。此时 [j,end) 必然是降序
在 [j,end) 从后向前 查找第一个满足 A[i] < A[k] 的 k。A[i]、A[k] 分别就是上文所说的「小数」、「大数」
将 A[i] 与 A[k] 交换
可以断定这时 [j,end) 必然是降序，逆置 [j,end)，使其升序
如果在步骤 1 找不到符合的相邻元素对，说明当前 [begin,end) 为一个降序顺序，则直接跳到步骤 4

作者：Imageslr
链接：https://leetcode.cn/problems/next-permutation/solutions/80560/xia-yi-ge-pai-lie-suan-fa-xiang-jie-si-lu-tui-dao-/
来源：力扣（LeetCode(1-50)）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        end = len(nums)
        i = end - 2
        j = i + 1
        # 从后往前找到第一对相邻的升序对
        while nums[j] <= nums[i] and i >= 0:
            i -= 1
            j -= 1
        # nums为当前最大排列
        if i < 0:
            nums.sort()
        else:
            # 从[j,end]中找到第一个大于nums[i]的数nums[k],这里[j,end]是逆序的
            k = end - 1
            while nums[i] >= nums[k]:
                k -= 1
            # 交换nums[i]和nums[k]
            temp = nums[i]
            nums[i] = nums[k]
            nums[k] = temp
            # 将[j,end]从小到大排序(逆序)
            nums[j:end] = sorted(nums[j:end])


def main():
    nums = eval(input())
    ob = Solution()
    ob.nextPermutation(nums)
    print(nums)


if __name__ == '__main__':
    main()

