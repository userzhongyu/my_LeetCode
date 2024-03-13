class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        res = []
        start = -1
        end = -1
        left = 0
        right = len(nums) - 1
        if left > right:
            return [-1, -1]
        if nums[left] == nums[right] == target:
            return [0, len(nums) - 1]
        mid = (left + right) // 2
        while left < right and nums[mid] != target:
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
            mid = (left + right) // 2
        if nums[mid] == target:
            start = mid
            while nums[start] == target:
                start -= 1
                if start == -1:
                    break
            start += 1
            end = mid
            while nums[end] == target:
                end += 1
                if end == len(nums):
                    break
            end -= 1
        res.append(start)
        res.append(end)
        return res


def main():
    nums = eval(input())
    target = int(input())
    ob = Solution()
    print(ob.searchRange(nums, target))


if __name__ == '__main__':
    main()
