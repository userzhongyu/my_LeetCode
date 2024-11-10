# 算法

## 动态规划

https://leetcode.cn/problems/scramble-string/solutions/51990/miao-dong-de-qu-jian-xing-dpsi-lu-by-sha-yu-la-jia/

**对于动态规划问题，将拆解为如下五步曲，这五步都搞清楚了，才能说把动态规划真的掌握了！**

1. 确定dp数组（dp table）以及下标的含义
2. 确定递推公式
3. dp数组如何初始化
4. 确定遍历顺序
5. 举例推导dp数组

## 递归

path用于存储路径

ans用于存储答案



# path

​    每一个‘高’对应一个列表，其中记录每一行连续1的个数作为‘宽’
​    取列表中最小的‘宽’与当前‘高’相乘作为‘面积’

```python
class Solution:
def maximalRectangle(self, matrix: List[List[str]]) -> int:
    n = len(matrix)
    m = len(matrix[0])
    ans = 0
    # 将每一个元素当做矩形右下角最后一个元素
    for i in range(n):
        for j in range(m):
            tmp_i = i
            tmp_j = j
            width = []  # 记录每一列对应的最长宽度
            height = 0
            # 逐列寻找连续的'1'
            while tmp_i >= 0 and matrix[tmp_i][tmp_j] == '1':
                tmp_width = 0
                height += 1
                # 逐行寻找连续的'1'
                while tmp_j >= 0 and matrix[tmp_i][tmp_j] == '1':
                    tmp_width += 1
                    tmp_j -= 1
                width.append(tmp_width)
                ans = max(ans, height * min(width))
                tmp_i -= 1
                tmp_j = j
    return ans

# 超时
```

结合84
    将每一个行结合该行上面的行组合成一个矩形
    计算出每一列的‘高度’，即连续的‘1’的‘高度’
    转换成84题



## [86. 分隔链表](https://leetcode.cn/problems/partition-list/)(链表创建代码)

```python
   	# 将输入的形如“[1,2,3,4,5]”的字符串转换成链表
    def create_ListNode(self):
        lst = list(input("list:")[1:-1].split(','))
        if lst == '[]':
            return ListNode()
        lst = [int(i) for i in lst]

        n = len(lst)

        # 头节点为空
        # head = ListNode()
        # tmp = ListNode(val=lst[0]
        # head.next = tmp

        # 头节点存数据
        head = tmp = ListNode(val=lst[0])
        for i in range(1, n):
            new = ListNode(val=lst[i])
            tmp.next = new
            tmp = tmp.next
        return head

```



## [87. 扰乱字符串](https://leetcode.cn/problems/scramble-string/)

### 动态规划

https://leetcode.cn/problems/scramble-string/solutions/51990/miao-dong-de-qu-jian-xing-dpsi-lu-by-sha-yu-la-jia/

**对于动态规划问题，将拆解为如下五步曲，这五步都搞清楚了，才能说把动态规划真的掌握了！**

1. 确定dp数组（dp table）以及下标的含义
2. 确定递推公式
3. dp数组如何初始化
4. 确定遍历顺序
5. 举例推导dp数组

**实践**

![image-20241104165028001](./my_LeetCode.assets/image-20241104165028001.png)

​	1.确定下标意义

​		i：从s的第i个字符起

​		j：从t的第j个字符起

​		l：对比长度为l的字符串

​	2.推导递推公式

![87a4f7ce752f6f399929e9510c25444](./my_LeetCode.assets/87a4f7ce752f6f399929e9510c25444.jpg)

​	3.将dp初始化为 i\*i\*l ，值均为"False"的矩阵 （取s1:'abc'，s2:'cab')

```python
dp = [[[False]*(4) for _ in range(3)] for _ in range(3)]  # 这是3*3*4的矩阵 代码从左往右，矩阵从外向内生成
```



![image-20241104161858373](./my_LeetCode.assets/image-20241104161858373.png)



![image-20241104161719090](./my_LeetCode.assets/image-20241104161719090.png)



​	4.确定遍历顺序

​		l->i->j，没有按行列顺序进行

```python
        for l in range(2, lens1+1):
            for i in range(lens1-l+1):
                for j in range(lens1-l+1):
                    # 子片段
                    for temp in range(1, l):
```

​	5.举例推导dp数组

```python
                        if dp[i][j][temp] and dp[i+temp][j+temp][l-temp]:
                            dp[i][j][l] = True
                        if dp[i][j+l-temp][temp] and dp[i+temp][j][l-temp]:
                            dp[i][j][l] = True
```



```python
import numpy as np

class Solution:
    def isScramble(self, s1, s2):  # 判断s2是不是s1的扰乱字符串
        lens1 = len(s1)

        dp = [[[False]*(lens1+1) for _ in range(lens1)] for _ in range(lens1)]
        print(dp)
        print(np.array(dp).shape)
        # 先判断单个字母的是否匹配
        for i in range(lens1):
            for j in range(lens1):
                if s1[i] == s2[j]:
                    dp[i][j][1] = True

        for l in range(2, lens1+1):
            for i in range(lens1-l+1):
                for j in range(lens1-l+1):
                    # 子片段
                    for temp in range(1, l):
                        if dp[i][j][temp] and dp[i+temp][j+temp][l-temp]:
                            dp[i][j][l] = True
                        if dp[i][j+l-temp][temp] and dp[i+temp][j][l-temp]:
                            dp[i][j][l] = True

        return dp[0][0][lens1]


def main():
    # s1 = input("s1:")
    # s2 = input("s2:")
    s1 = "abcdefghijklmnopq"
    s2 = "efghijklmnopqcadb"
    ans = Solution().isScramble(s1, s2)
    print(ans)


if __name__ == '__main__':
    main()

```



### 递归

![87_3](./my_LeetCode.assets/87_3.jpg)



```python
 	# 按位置逐位分割后进行子片段判断
    for i in range(1, lens1):
            if self.isScramble(s1[0: i], s2[0: i]) and self.isScramble(s1[i: lens1], s2[i: lens1]) \
                    or self.isScramble(s1[0: i], s2[lens1-i: lens1]) and self.isScramble(s1[i: lens1], s2[0: lens1-i]):
                return True
```



超时，进行剪枝

```python
        # 比较字符串构成的元素是否相同
        if sorted(s1) != sorted(s2):
            return False
```



```python
class Solution:
    def isScramble(self, s1, s2):  # 判断s2是不是s1的扰乱字符串
        lens1 = len(s1)
        lens2 = len(s2)
        if lens1 != lens2:
            return False
        # 比较字符串构成的元素是否相同
        if sorted(s1) != sorted(s2):
            return False
        if s1 == s2:
            return True

        # 按位置逐位分割后进行子片段判断
        for i in range(1, lens1):
            if self.isScramble(s1[0: i], s2[0: i]) and self.isScramble(s1[i: lens1], s2[i: lens1]) \
                    or self.isScramble(s1[0: i], s2[lens1-i: lens1]) and self.isScramble(s1[i: lens1], s2[0: lens1-i]):
                return True
        return False

def main():
    s1 = "abb"
    s2 = "bba"
    # s1 = "abcdefghijklmnopq"
    # s2 = "efghijklmnopqcadb"
    ans = Solution().isScramble(s1, s2)
    print(ans)


if __name__ == '__main__':
    main()
```



##  [89. 格雷编码](https://leetcode.cn/problems/gray-code/)

存在问题：无法正确跳出递归。从path去除的数字放入con后，会再次放入path的相同位置，导致死循环

```python
import math
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0, ]
        con = [i for i in range(1, pow(2, n))]
        return self.dfs(ans, con, n)

    def dfs(self, path: list, con: list, n: int):
        if len(path) == pow(2, n):
            return path
        if len(path) == pow(2, n)-1:
            if (path[-1] ^ con[-1]) & ((path[-1] ^ con[-1]) - 1) == 0 and (path[0] ^ con[-1]) & ((path[0] ^ con[-1]) - 1) == 0:
                path.append(con[-1])
                return path
            else:
                con.append(path.pop())
                return

        for i in range(len(con)+1):
            if (path[-1] ^ con[i]) & ((path[-1] ^ con[i]) - 1) == 0:
                path.append(con[i])
                con.remove(con[i])
                self.dfs(path, con, n)
                if len(path) == pow(2, n):
                    return path
                temp = path.pop()
                con.insert(i, temp)


def main():
    n = 4
    print(Solution().grayCode(n))


if __name__ == '__main__':
    main()

```

### 动态规划

https://leetcode.cn/problems/gray-code/solutions/9730/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by--12/

按照动态规划或者说递归的思路去想，也就是解决了小问题，怎么解决大问题。

我们假设我们有了 n = 2 的解，然后考虑怎么得到 n = 3 的解。

n = 2 的解

```
00 - 0
10 - 2
11 - 3
01 - 1
```

如果再增加一位，无非是在最高位增加 0 或者 1，考虑先增加 0。由于加的是 0，其实数值并没有变化。

n = 3 的解，最高位是 0

```
000 - 0
010 - 2
011 - 3
001 - 1 
```


再考虑增加 1，在 n = 2 的解基础上在最高位把 1 丢过去？

```
100 - 4
110 - 6
111 - 7
101 - 5  
```

似乎没这么简单哈哈，第 4 行 001 和新增的第 5 行 100，有 3 个 bit 位不同了，当然不可以了。怎么解决呢？

很简单，第 5 行新增的数据最高位由之前的第 4 行的 0 变成了 1，所以其它位就不要变化了，直接把第 4 行的其它位拉过来，也就是 101。

接下来，为了使得第 6 行和第 5 行只有一位不同，由于第 5 行拉的第 4 行的低位，而第 4 行和第 3 行只有一位不同。所以第 6 行可以把第 3 行的低位拿过来。其他行同理，如下图。

![image-20241105205642225](./my_LeetCode.assets/image-20241105205642225.png)

```python
import math
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0, 1]
        # 一轮一轮生成
        for i in range(1, n):
            temp = []  # 增加的新列表
            for j in range(1, len(ans)+1):
                temp.append(ans[-j]+pow(2, i))  # 总结出来的规律
            ans.extend(temp)
        return ans


def main():
    n = 4
    print(Solution().grayCode(n))


if __name__ == '__main__':
    main()

```

## [90. 子集 II](https://leetcode.cn/problems/subsets-ii/)

### 超时

```python
# 超时
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path = [[], ]
        nums.sort()  # 排序，避免[1,2]和[2,1]都插入的情况
        self.dfs(path, nums)
        return path

    def dfs(self, path: list, nums: List[int]):
        if len(nums) == 0:
            return
        templst = []
        for i in range(len(nums)):
            templst.append(nums[i])
            if templst not in path:
                path.append(templst[:])  # 深拷贝
            tempval = nums[i]
            nums.remove(nums[i])
            self.dfs(path, nums)
            nums.insert(i, tempval)


def main():
    nums = [1, 4, 3, 5, 4, 4, 7, 7, 8, 0]
    print(Solution().subsetsWithDup(nums))


if __name__ == '__main__':
    main()

```

### Accepted

**思路**

考虑数组 [1,2~1~,2~2~]，选择前两个数，或者第一、三个数，都会得到相同的子集。

也就是说，对于当前选择的数 2~2~，若前面有与2~2~相同的2~1~，且没有选择 2~1~，此时包含2~2~ 的子集，必然会出现在包含2~1~ 的所有子集中。

代码实现时，可以先将数组排序；迭代时，若发现没有选择上一个数，且当前数字与上一个数相同，则可以跳过当前生成的子集。




i：本轮次当前操作到第i个元素

j：操作i-len(nums)

j == i：开始操作nums[j]

j > i and nums[j] == nums[j-1]：当前元素与其前一个元素相同，且包含前一个元素的子集已经生成结束（前一个元素已经操作过了）

```python
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        nums.sort()  # 排序，使得相同元素相邻
        self.dfs(ans, path, nums, 0)
        return ans

    def dfs(self, ans: list, path: list, nums: List[int], i: int):
        ans.append(path[:])  # 深拷贝
        if i == len(nums):
            return
        for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j-1]:
                continue
            path.append(nums[j])
            self.dfs(ans, path, nums, j+1)  # 本轮次已经操作到第j个元素，下一轮次从j+1开始操作
            path.pop()


def main() -> object:
    # nums = [1, 4, 3, 5, 4, 4, 7, 7, 8, 0]
    nums = [1, 2, 2]
    print(Solution().subsetsWithDup(nums))


if __name__ == '__main__':
    main()

```



## [93. 复原 IP 地址](https://leetcode.cn/problems/restore-ip-addresses/)

https://leetcode.cn/problems/restore-ip-addresses/solutions/100433/hui-su-suan-fa-hua-tu-fen-xi-jian-zhi-tiao-jian-by/

思路：

`path[]` 存储满足`0 <= tmp <= 255`的值

`len(path) `就是地址的段数

`index` 记录当前操作到什么位置了

当`len(path) == 4 and index == len(s)` 时，说明`path[]`中存的数字所组成的地址是合理的

`ans[]`存储满足要求的地址

```python
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        path = []

        def dfs(__ans, __path, index: int):
            if len(path) > 4:
                return
            if len(__path) == 4 and index == len(s):
                __ans.append('.'.join(__path[:]))
                return
            # 检查随后的连续3个数字
            for i in range(1, 4):
                tmp = s[index: index+i]  # 切出需要进行判断的数字组合
                if tmp and 0 <= int(tmp) <= 255 and str(int(tmp)) == tmp:  # 判断当前数字组合能否当做一个段地址
                    path.append(tmp[:])
                    dfs(__ans, __path, index+i)  # 深入
                    path.pop()  # 恢复现场

        dfs(ans, path, 0)
        return ans


def main():
    # s = "25525511135"
    s = '0000'
    s = "101023"
    print(Solution().restoreIpAddresses(s))


if __name__ == '__main__':
    main()

```

`'.'.join(__path[:])`将列表转换成以`'.'`连接的字符串

```python
                if tmp and 0 <= int(tmp) <= 255 and str(int(tmp)) == tmp:  # 判断当前数字组合能否当做一个段地址
```

当下标越界时，`tmp == ''`

当`tmp == 012`这种类似的数字时，`str(int(tmp)) != tmp`
