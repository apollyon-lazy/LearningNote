# Python个人总结
(在没看书前做项目中遇到没记住的语法会记下来)
## 列表
### 列表定义 
1. Python中用方括号\[ \]来表示列表，并用逗号，来分隔其中的元素
2. 数据类型为 list **有序可变**序列
3. listname = [element1 , element2 , element3 , ... ,elementn]

### 列表内置函数

| Function | Description | Return | 
| :---  | :--- | :--- |
| listname.append(obj)        | 在列表的末尾追加obj一个单元素 |
| listname.extend(obj)        | 在列表的末尾追加obj中所有元素 |
| listname.insert(index, obj) | 在列表的中间插入单元素       |
| listname.pop([index=-1])    | 移出列表对应索引元素    | 返回该元素 |
| listname.remove(obj)        | 删除列表对象                  |


## 元组 
### 元组定义
1. Python中通常是用小括号( )来表示元组(非必须) 只要将各元素用逗号,隔开就会视为元组    
2. 数据类型为 tuple **有序不可变**序列    
3. tuplename = (element1, element2, ..., elementn)    

## 字典
### 字典定义
1. Python中键(key)和值(value)用冒号:隔开 相邻元素用逗号,隔开 所有元素放在大括号{ }中    
2. 数据类型为 dict **无序可变**序列     
3. dictname = {'key'(键):'value1'(值), 'key2':'value2', ..., 'keyn':valuen}  
### 字典内置函数
dict.item() 返回可遍历的(键, 值)元组列表



## Python内置函数

| Function      | Description                              | Return | 
| :---          | :---                                     | :--- |
| abs()         |  返回数字的绝对值                         |
| enumerate()   | 将可遍历数据合成索引序列<br> for i,(X,y) in enumerate(data) | enumerate object |
| print()       | 用于打印输出                              |
| input()       | 用于输入一个数据                          |
| isinstance()  | 判断一个对象是否属于已知类型<br> isinstance(object, classinfo)|  |
| iter()        |  产生迭代器                              | list_iterator Object |
| next()        | 返回迭代器的下一个项目                    | 
| range()       | 生成序列<br> range(start=0, stop, step=1)|
| set()         | 创建一个无序不重复的元素集                |
| sorted()      | 对所有可迭代的对象进行排序操作<br> sorted(iterable, reverse=False) |
| type()        | 返回对象的类型                           |
| zip()         | 打包对应元素为元组列表                   | list |

- type()不会认为子类是一种父类类型，不考虑继承关系
- list_iterator Object最后一个元素是StopIteration 
- isinstance()会认为子类是一种父类类型，考虑继承关系
- range 只适用于生成整型序列

#### 导入
from 模块名 import 成员名 as 别名 &emsp; 从模块中导入成员名起个别名  

#### 函数
name = lambda[list]:表达式 &emsp;  lambda 匿名函数 常用来简写函数体只有一行的函数  


#### 类和对象
\_\_init\_\_(self,...) 构造函数  
self 调用构造函数时无需给self赋值  
super() 调用直接父类函数  
class 类名(父类1，父类2...) 多继承机制  

with EXPR as VAR:  
BLOCK  
确保with中的语句出现问题不会占用资源

#### 变量作用域
python 访问局部变量和全局变量的规则：当搜索一个变量的时候，python 先从局部作用域开始搜索，如果在局部作用域没有找到那个变量，那样 python 就按照作用域逐层寻找，如果找不到则抛出 UnboundLocalError 异常。
如果内部函数有引用外部函数的同名变量或者全局变量，并且对这个变量有修改的时候，此时 python 会认为它是一个局部变量，而当函数中没有变量的定义和赋值的时候，就会报错。

