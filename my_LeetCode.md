# LeetCode

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

