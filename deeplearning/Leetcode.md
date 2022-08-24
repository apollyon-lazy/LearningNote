## 剑指offer 62.圆圈中最后剩下的数字

0,1,···,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字（删除后从下一个数字开始计数）。求出这个圆圈里剩下的最后一个数字。  
例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

```Python
# 失败原因：超出时间限制
def lastRemaining(n: int, m: int) -> int:
    arr = list(range(n))
    i = m 
    while arr: 
        while i > n:
            i -= n
        result = arr.pop(i-1)
        n -= 1 
        i = i + m - 1 
    return result
lastRemaining(10,17)
```
#### 数学+迭代
```Python
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        f = 0
        for i in range(2, n + 1):
            f = (m + f) % i
        return f
# 时间复杂度：O(n) ，需要求解的函数值有 n 个。  
# 空间复杂度：O(1) ，只使用常数个变量。  
```