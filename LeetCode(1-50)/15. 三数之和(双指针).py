class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        lst_out = []
        l = len(nums)
        if l < 3:
            return []
        nums.sort()
        for i in range(0, l - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = l - 1
            if nums[i] > 0 or nums[k] < 0:
                break
            # 固定下标i,移动其他下标 进行判断
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    lst_out.append([nums[i], nums[j], nums[k]])
                    # 检查当前nums[i]的其他可能三元组
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    # 和过小,小数增加
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    # 和过大,大数减小
                    k -= 1
        return lst_out

def main():
    while True:
        # 输入格式转换
        nums = eval(input())
        nums = list(nums)
        # print(nums)
        # print(type(nums[0]))
        ob = Solution()
        print(ob.threeSum(nums))


if __name__ == '__main__':
    main()