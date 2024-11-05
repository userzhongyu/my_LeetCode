# LeetCode

## 85. 最大矩形

暴力解：
    将每一个元素当做矩形右下角元素，向上向左寻找尽可能多的连续的1
    每一个‘高’对应一个列表，其中记录每一行连续1的个数作为‘宽’
    取列表中最小的‘宽’与当前‘高’相乘作为‘面积’

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



## 86. 分隔链表(链表创建代码)

```python
    def create_ListNode(self):
        l = input("input:")
        if l == '[]':
            return ListNode()
        l = l[1: -1]
        l = l.split(',')
        n = len(l)
        head = tmp = ListNode(val=int(l[0]))
        for i in range(1, n):
            new = ListNode(val=int(l[i]))
            tmp.next = new
            tmp = tmp.next
        return head

```



## 87.扰乱字符串

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



##  89. 格雷编码

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


