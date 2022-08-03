### 实验零：python中对象的引用


```python
a = 1
a = 'adc'
# 对与学过C的人都会觉得很离谱
# 因为明明1和adc是数字和字符串
# 类型完全不一致却可以自由切换？
# 这是因为a只是一个指针
# 在它从1重新指向adc时之前的1已经被释放了，不会占用内存空间
```

### 实验一：利用python函数传导参数


```python
# python传不可变对象实例
# 我们注意到change中的a是形式参数 代码改变不改变实参----
def change1(a):
    a = a + 100
    
a = 1
change1(a)
print(a)
#------那么我们怎么才能将实参改变呢？----------
#------这就需要return语句的书写了---------------
def change2(a):
    a = a + 100
    return(a)

a = 1
a = change2(a)
print(a)
```

    1
    101
    

### 实验二：向python中导入包


```python
# from 是代表从某个模块中导出东西
# import 表示要导出模块中的某个组件
# * 代表导出模块或者组件的所有内容
# as 代表给导出的模块或者组件起新的一个名字
#下面我们来举个例子
# 哦？！这里竟然有两个datetime?
# 是因为模块是很大的，里面会有子类，
# 子组件下还可能有子子类，直到最后一层才可能会出现函数
import datetime
print(datetime.datetime.now())
```

    2022-07-24 21:54:40.632545
    


```python
# 验证一下我们的猜想
# 果然datetime有一个同名的组件datetime
# 哦？！细心的我们发现一个命名习惯
# 为什么有些模块中的组件还要定义 __doc__ 这种前后带双下划线
# 通过网络上给出的一些解释
# 其中一种解释是表示他们的用途是使得函数能够运行的底层代码
# 像是函数调用、函数创建、内存分配诸如此类……
import datetime
dir(datetime)
```




    ['MAXYEAR',
     'MINYEAR',
     '__all__',
     '__builtins__',
     '__cached__',
     '__doc__',
     '__file__',
     '__loader__',
     '__name__',
     '__package__',
     '__spec__',
     'date',
     'datetime',
     'datetime_CAPI',
     'sys',
     'time',
     'timedelta',
     'timezone',
     'tzinfo']




```python
# from语句可以帮助我们只导入模块中的一个组件
# 用from语句我们验证一下我们的猜想
from datetime import datetime
print(datetime.now())
```

    2022-07-24 21:54:41.427761
    


```python
# 假如你嫌datetime这个包名称太长，想要给它取个别名
# 以后每次用到它的时候都用它的别名代替它，这时就需要用到import…as，例子如下：
from datetime import datetime as dt
print (dt.now())
```

    2022-07-24 21:54:41.843957
    


```python
# import datetime.datetime as dt 的写法是错误
# import 模块名
# from 模块名 import 模块中函数或类 as 别名
from datetime import datetime as dt
print(dt.now())
```

    2022-07-24 21:54:50.890042
    


```python
# 最后我们建议不要 from modulename import module as *
# 原因是因为*代表模块里的所有被写入程序
# 可能会导致部分模块不会被导入
# 像是echo和ECHO大小写不同但被Windows识别为同一文件的可能……
```

### 实验三：变量的作用域问题


```python

# 我们都知道，在程序中根据变量的作用域的不同可以把变量分为全局变量与局部变量
# 在函数中的变量如果没有特别声明即使变量名与全局变量名完全一致也不会对全局的变量产生影响
# 这样我们就解决了函数内部对外部全局变量的更改
a = 'a'
def change():
    a = 'b'
change()
print(a)
# 如果我想对a做出更改就要
a = 'a'
def change():
    global a
    a = 'b'
change()
print(a)
```


```python
# 测试全局变量是否能在函数中被赋值
# python中逻辑运算符是and or not 注意与C区分
dst1, dst2, dst3 = 0.0, 0.0, 0.0
def Gear_WeightOnWheels():
    global dst1, dst2, dst3
    return ((dst1 < -1.0) or ( dst2 >= 0.0))
Gear_WeightOnWheels()
```


```python
# 变量后的赋值一定要紧跟变量在同一行
# 否则会报语法错误
# python中的单行注释用‘#’开始
# python中的多行注释用三单引号或者三双引号包起来
damping_nose = [ [0.0, 7.0], [6.0, 7.0], [10.0, 10.0], [14.0, 15.0], 
[16.0, 29.0], [20.0, 38.0], [25.0, 67.0] ] 
print(damping_nose[2][1])
```


```python
"""
在计算机程序的开发过程中，随着程序代码越写越多，在一个文件里代码就会越来越长，越来越不容易维护
为了编写可维护的代码，我们把很多函数分组，分别放到不同的文件里，这样，每个文件包含的代码就相对较少
很多编程语言都采用这种组织代码的方式。在Python中，一个.py文件就称之为一个模块（Module）
使用模块有什么好处？
最大的好处是大大提高了代码的可维护性。其次，编写代码不必从零开始。
当一个模块编写完毕，就可以被其他地方引用
我们在编写程序的时候，也经常引用其他模块，包括Python内置的模块和来自第三方的模块。
使用模块还可以避免函数名和变量名冲突
相同名字的函数和变量完全可以分别存在不同的模块中，因此，我们自己在编写模块时，不必考虑名字会与其他模块冲突。
但是也要注意，尽量不要与内置函数名字冲突
你也许还想到，如果不同的人编写的模块名相同怎么办？
为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）
举个例子，一个abc.py的文件就是一个名字叫abc的模块，一个xyz.py的文件就是一个名字叫xyz的模块
现在，假设我们的abc和xyz这两个模块名字与其他模块冲突了，于是我们可以通过包来组织模块，避免冲突
方法是选择一个顶层包名，比如mycompany，按照如下目录存放
mycompany
    __init__.py
    abc.py
    xyz.py
引入了包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突。
现在，abc.py模块的名字就变成了mycompany.abc，类似的，xyz.py的模块名变成了mycompany.xyz
请注意，每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的
否则，Python就把这个目录当成普通目录，而不是一个包
__init__.py可以是空文件，也可以有Python代码
因为__init__.py本身就是一个模块，而它的模块名就是mycompany。
"""

import math
math.sin(math.pi/2)
dir(math)
```




    ['__doc__',
     '__loader__',
     '__name__',
     '__package__',
     '__spec__',
     'acos',
     'acosh',
     'asin',
     'asinh',
     'atan',
     'atan2',
     'atanh',
     'ceil',
     'copysign',
     'cos',
     'cosh',
     'degrees',
     'e',
     'erf',
     'erfc',
     'exp',
     'expm1',
     'fabs',
     'factorial',
     'floor',
     'fmod',
     'frexp',
     'fsum',
     'gamma',
     'gcd',
     'hypot',
     'inf',
     'isclose',
     'isfinite',
     'isinf',
     'isnan',
     'ldexp',
     'lgamma',
     'log',
     'log10',
     'log1p',
     'log2',
     'modf',
     'nan',
     'pi',
     'pow',
     'radians',
     'remainder',
     'sin',
     'sinh',
     'sqrt',
     'tan',
     'tanh',
     'tau',
     'trunc']




```python

```
