# import copy
# from typing import List
#
# a = [1, 3, 5, "a"]
# b, c, d, e = [], [], [], []
# b.append(a)
# c.append(a[:])
# d.append(list(a))
# e.append(copy.deepcopy(a))
# print(b)  # [[1, 3, 5, 'a']]
# print(c)  # [[1, 3, 5, 'a']]
# print(d)  # [[1, 3, 5, 'a']]
# print(e)  # [[1, 3, 5, 'a']]
# a.append("aha")
# print(b)  # [[1, 3, 5, 'a', 'aha']]  b也被修改了
# print(c)  # [[1, 3, 5, 'a']]
# print(d)  # [[1, 3, 5, 'a']]
# # print(e)  #


# s = '123456'
#
# num = [int(i) for i in s]
#
# print(num)


# print([1, 2, 3] in [1, 2, 3, 4])
# a = 'a'
# b = a+11
# print(b)

# lst = list(input()[1:-1].split(','))
# lst = [int(i) for i in lst]
# print(lst)

# path = '123456'
# tmp = '789'
# path = path + tmp + '.'
# print(path)
# path = path[0: -len(tmp)-1]
# print(path)

# tmp = '01'
# print(int(tmp))
#
# s = '123'
# t = s[2: 3]
# print(t)

lst = [1, 2, 3]
lst = lst[: -2]
print(lst)
