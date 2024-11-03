class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        lst_temp = []
        l = len(nums)
        for i in range(0, l - 2):
            for j in range(i + 1, l - 1):
                for k in range(j + 1, l):
                    if nums[i] + nums[j] + nums[k] == 0:
                        lst_temp.append([nums[i], nums[j], nums[k]])
        # 去重
        if len(lst_temp) == 0:
            return []
        lst_out = [lst_temp[0]]
        for i in range(1, len(lst_temp)):
            # 在remove后len(lst_out)自减,导致下标越界
            # 解决办法:倒序判断
            # for j in range(i + 1, len(lst_out)):
            # 漏判最后一元素
            # for j in range(temp - 1, i, -1):
            #     if set(lst_out[i]) == set(lst_out[j]):
            #         lst_out.remove(lst_out[j])
            flag = True
            for j in range(0, len(lst_out)):
                if set(lst_temp[i]) == set(lst_out[j]):
                    flag = False
            if flag:
                lst_out.append(lst_temp[i])
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