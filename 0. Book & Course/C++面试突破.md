# C++编译与内存管理
## C++ 内存管理
### ELF文件

可执行与可链接格式 `(Executable and Linkable Format)` 是一种用于可执行文件、目标代码、共享库和核心转储 `（core dump）` 的标准文件格式，每个 **ELF** 文件都由一个 ELF header 和紧跟其后的文件数据部分组成，可以参考 **ELF** 文件的构成如下:
![[memory.jpg]]
`.text section`：代码段。通常存放已编译程序的机器代码，一般操作系统加载后，这部分是只读的。
`.rodata section`：只读数据段。此段的数据不可修改，存放程序中会使用的常量。比如程序中的常量字符串 `"aasdasdaaasdasd"`
`.data section`：数据段。主要用于存放已初始化的全局变量、常量。
`.bss section`: bss 段。该段主要存储未初始化全局变量，仅是占位符，不占据任何实际磁盘空间。目标文件格式区分初始化和非初始化是为了空间效率。

**操作系统在加载 ELF 文件时会将按照标准依次读取每个段中的内容，并将其加载到内存中，同时为该进程分配栈空间，并将 pc 寄存器指向代码段的起始位置，然后启动进程。**

### 内存分区

`C++`程序在运行时也会按照不同的功能划分不同的段，`C++` 程序使用的内存分区一般包括：栈、堆、全局/静态存储区、常量存储区、代码区。

**栈**：目前绝大部分 CPU体系都是基于栈来运行程序，栈中主要存放函数的局部变量、函数参数、返回地址等，栈空间一般由操作系统进行默认分配或者程序指定分配，栈空间在进程生存周期一直都存在，当进程退出时，操作系统才会对栈空间进行回收。

**堆**：动态申请的内存空间，就是由 malloc 函数或者 new 函数分配的内存块，由程序控制它的分配和释放，可以在程序运行周期内随时进行申请和释放，如果进程结束后还没有释放，操作系统会自动回收。

**全局区/静态存储区**：主要为 .bss 段和 .data 段，存放全局变量和静态变量，程序运行结束操作系统自动释放，在 C 中，未初始化的放在 .bss 段中，初始化的放在 .data 段中，C++ 中不再区分了。

**常量存储区：**.rodata 段，存放的是常量，不允许修改，程序运行结束自动释放。

**代码区：**.text 段，存放代码，不允许修改，但可以执行。编译后的二进制文件存放在这里。

我们参考常见的 Linux 操作系统下的内存分布图如下:

**从操作系统的本身来讲，以上存储区在该程序内存中的虚拟地址分布是如下形式（虚拟地址从低地址到高地址，实际的物理地址可能是随机的）**

![[memory2.jpg]]

```cpp
#include <iostream>
using namespace std;
/*说明：C++ 中不再区分初始化和未初始化的全局变量、静态变量的存储区，如果非要区分下述程序标注在了括号中*/
int g_var = 0; // g_var 在全局区（.data 段）
char *gp_var;  // gp_var 在全局区（.bss 段）

int main()
{
    int var;                    // var 在栈区
    char *p_var;                // p_var 在栈区
    char arr[] = "abc";         // arr 为数组变量，存储在栈区；"abc"为字符串常量，存储在常量区
    char *p_var1 = "123456";    // p_var1 在栈区；"123456"为字符串常量，存储在常量区
    static int s_var = 0;       // s_var 为静态变量，存在静态存储区（.data 段）
    p_var = (char *)malloc(10); // 分配得来的 10 个字节的区域在堆区
    free(p_var);
    return 0;
}
```

# C++语言对比

## C++11新特性

C++ 11 与 C++ 98 相比，引入新特性有很多，从面试的角度来讲，如果面试官问到该问题，常以该问题作为引子，对面试者提到的知识点进行深入展开提问。面试者尽可能的列举常用的并且熟悉的特性，尽可能的掌握相关原理，下文只是对相关知识点进行了简单的阐述，有关细节还需要结合相关知识点的相关问题。下面主要介绍 C++ 11 中的一些面试中经常遇到的特性。

`auto` 类型推导:
`auto` 关键字：自动类型推导，编译器会在 编译期间 通过初始值或者函数返回值推导出变量的类型，通过 `auto` 定义的变量必须有初始值。
`auto` 关键字基本的使用语法如下：

```cpp
auto var = val1 + val2; // 根据 val1 和 val2 相加的结果推断出 var 的类型
auto ret = [](double x){return x*x;}; // 根据函数返回值推导出 ret 的类型
auto al = { 10, 11, 12 }; //类型是std::initializer_list<int>
```

使用 auto 关键字做类型自动推导时，依次施加以下规则:
首先，如果初始化表达式是引用，首先去除引用；
上一步后，如果剩下的初始化表达式有顶层的 const 或 volatile 限定符，去除掉。使用 auto 关键字声明变量的类型，不能自动推导出顶层的 const 或者 volatile，也不能自动推导出引用类型，需要程序中显式声明，比如以下程序：

初始化表达式为数组，`auto` 关键字推导的类型为指针。数组名在初始化表达式中自动隐式转换为首元素地址的右值。

```cpp
int a[9]; 
auto j = a; // 此时j 为指针为 int* 类型，而不是 int(*)[9] 类型
std::cout << typeid(j).name() << " "<<sizeof(j)<<" "<<sizeof(a)<< std::endl;
```