# 《Python编程从入门到实践》

## 目录
[第一章 起步](#第一章-起步)  
[第二章 变量和数据类型](#第二章-变量和数据类型)  
[第三章 列表简介](#第三章-列表简介)  
[第四章 操作列表](#第四章-操作列表)  
[第五章 if 语句](#第五章-if-语句)  
[第六章 字典](#第六章-字典)  
[第七章 用户输入和while循环](#第七章-用户输入和while循环)  
[第八章 函数](#第八章-函数)  
[第九章 类](#第九章--类)   
[第十章 文件和异常](#第十章-文件和异常)  
[第十一章 测试代码](#第十一章-测试代码)  

## 第一章 起步

## 第二章 变量和数据类型

### 参考小节
- 2.1 2.2 运行hello_world.py时发生的情况 & 变量
- 2.3 2.4 2.5 字符串 & 数字 & 注释

### 知识点
- 用单引号或双引号括起的都是字符串，字符串可以使用 + 进行拼接
- 编程中，空白泛指任何非打印字符，如空格、制表符和换行符
> 可以将余生都用来学习Python和编程的纷繁难懂之处，但这样什么项目都会完不成

## 第三章 列表简介

### 参考小节
- 3.1 列表是什么
- 3.2 修改，添加和删除元素
- 3.3 组织列表
- 3.4 使用列表时避免索引错误

### 知识点
  - 通常给列表变量起复数的名字是不错的选择
  - **列表**用方括号`[]`来表示，用逗号来分隔元素
  - 数据类型是 list, 是`有序可变`序列
  - 最后一个元素的索引可以是 -1
  - 列表的索引 listname.index(value)
  - 列表的增 listname.append(); listname.extend()
  - 列表的删 del XXX; listname.pop(); listname.remove()
  - 列表组织（排序，反转，求长度） listname.sort(); sorted(); listname.reverse(); len()

## 第四章 操作列表

### 参考小节
- 4.1 4.2 遍历整个列表 & 避免缩进错误
- 4.3 4.4 创建数值列表 & 使用列表的一部分
- 4.5 4.6 元组 & 设置代码格式

### 知识点 
- 列表解析将for循环和创建的新元素代码合并成一行，例如 
  `squares = [value**2 for value in range(1,11)]`
- PEP 8 建议每级缩进使用四个空格而非制表符，大多数文本编辑器会将制表符转为空格
- **元组**用小括号`()`(非必须)来表示，只要用逗号来分隔元素，就会视为元组
- 数据类型为 tuple，是`有序不可变`序列

## 第五章 if 语句

## 第六章 字典

### 参考小节
- 6.1 一个简单的字典
- 6.2 使用字典
- 6.3 遍历字典
- 6.4 嵌套

### 知识点
- **字典**中键和值用冒号`:`隔开，相邻元素用逗号`,`隔开 所有元素放在大括号`{ }`中 
- 数据类型为 dict `无序可变`序列
- 提取字典中的所有键组成一个列表 dictname.key()；提取字典中的所有值组成一个列表 dictname.value()；提取字典中所有键值对醉组成一个列表 dictname.items()
- **集合**使用 `{}` 或 `set()`函数创建集合，空集合必须是`set()`，集合是`无序不重复`元素序列

## 第七章 用户输入和while循环

## 第八章 函数

### 参考小节

- 8.1 8.2 定义函数 & 传递实参  
- 8.3 8.4 返回值 & 传递列表  
- 8.5 传递任意数量的实参  
- 8.6 将函数存储在模块中  
- 8.7 编写函数指南  

### 知识点

- 向函数传递参数的方式有位置实参，关键字实参  
- 形参指定默认值，或者调用关键词实参，等号两边不要有空格  
- 使用默认值时，形参必须先列出没有默认值的形参  
- 禁止函数修改列表，可以用切片表示法 [:] 创建列表的副本作为实参传入函数  
- 形参名 * args 将创建一个名为 args 的空元组，放在形参末尾  
- 形参名 ** args 将创建一个名为 args 的空字典，放在形参末尾  
- 函数存储在被称为**模块**的独立文件中，函数和模块导入时可以起**别名**  
- 使用并非自己编写的大型模块时，最好不要用星号运算符 * 导入模块中的所有函数，以免名称冲突  
- 通常函数名使用小写字母和下划线；通常函数注释紧跟在函数定义后面，并采用文档字符串格式
- PEP (Python Enhancement Proposal Python 增强建议书)：import 只导入一个模块；行尾不添加分号；每行不超过80字符，超过用小括号隐式连接；顶级定义间空两行，方法定义空一行，某些功能空一行；通常情况下，运算符两侧，函数参数之间以及逗号两侧，建议空格分隔

![[python_1.jpg]]

## 第九章  类

### 参考小节
- 9.1 9.2 创建和使用类 & 使用类和实例
- 9.3 继承
- 9.4 9.5 导入类 & Python 标准库
- 9.6 类编码风格

### 知识点
- 类中的函数叫做**方法**，可通过实例访问的变量称为**属性**
- 方法中的第一个形参是 self 且必不可少，实例(句点表示法)调用方法时不用给self传值
- 类中的每个属性都必须有初始值，哪怕这个值是零或空字符串
- 继承中子类的super()是一个特殊函数，帮助Python将父类和子类关联起来
- 子类中可以重写父类中的方法，实例也可以是类的属性
- 类采用驼峰命名法，即类名中每个单词首字母都大写，而不使用下划线；实例名采用小写，并在单词之间加下划线
> 一开始应让代码结构尽可能简单，先尽可能在一个文件中完成所有的工作，确定一切都能正常运行后，再将类移到独立的模块

  ![[python_2.jpg]]

## 第十章 文件和异常

### 参考小节
- 10.1 10.2 从文件中读取数据 & 写入文件
- 10.3 异常
- 10.4 存储数据

### 知识点
-  open() 用于打开文件返回一个文件对象，close() 用于关闭文件；关键字 with 会在不需要访问时将文件关闭；文件对象的方法 read() 读取文件所有内容，到文件末尾会返回一个空白字符串；方法 rstrip() 可以帮助消除多余空行；方法 readline() 会读取文件每一行作为一个元素存放到一个列表当中；或者文件对象当成列表循环遍历也可以获取每行字符串
- 读取文本文件数字数据，必须使用 int() 或者 float() 转换类型；写入文本文件数据，必须使用函数 str() 转换类型
- Python使用被称为**异常**的特殊对象来管理程序执行期间发生的错误
- try-except-else 代码块可以避免让用户看到 traceback，用pass在捕获异常后可以什么都不做 ，向用户展示多少信息取决于你
- 标准库中 `json 包` 让你能够将简单的 python 数据结构转储到文件中。json.dump() 存储数据到 json文件中；json.load() 加载数据到内存中

  ![[python_3.jpg]]

>代码能正常运行，可改进划分为一系列完成具体工作的函数，这样的过程叫**重构**，能让代码更清晰、更易于理解、更容易扩展


## 第十一章 测试代码

### 参考小节
- 11.1 11.2 测试函数 & 测试类

### 知识点
- **断言**方法用来核实得到的结果是否与期望的结果一致
- python标准库中 `unittest 包`提供了代码测试工具
  ![[python_4.jpg]]






