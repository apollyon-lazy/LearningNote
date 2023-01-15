# 操作系统：设计与实现 —— 南京大学

## 目录

[操作系统上的程序](#操作系统上的程序)
[多核处理器编程](#多核处理器编程)

## 操作系统上的程序


:thinking: C语言程序可以理解成一个状态机。程序的全局变量是每条指令可以共同访问的资源，PC用来存放当前欲执行指令的地址。状态机的初始状态，是全局变量初始化，PC在main的第一条语句上。指令每执行一次，PC和全局变量就会发生变化，就相当于状态机的状态发生一次转移。当遇到函数调用和函数返回就相当于进入和走出一个局部的指令列表。

:memo:怎么理解一个最小的HelloWorld程序?

- [x] C语言写的 `printf("HelloWorld")` 不是实现对应功能的最小程序，因为它链接了很多库代码用了更加底层的函数，实际上程序只要有能打印HelloWorld的 **系统调用(system call)** 就足够了。



## 多核处理器编程

:thinking: 个人电脑一般是多核单CPU的，往往在一个核上会运行单个进程间的多个线程，或是不同进程间的多个线程，单核上线程调度属于**并发(Concurrency)**。历史上操作系统是第一个并发程序，很多并发应用程序技术也来自于此。

:memo:怎么理解并发程序的原子性、有序性和可见性？

- [x] 并发程序正确地执行，必须要保证原子性、可见性以及有序性。只要有一个没有被保证，就有可能会导致程序运行不正确。**原子性**：一个操作或多个操作要么全部执行完成且执行过程不被中断，要么就不执行（`以两个线程，都要对共享变量操作为例。操作可能是取内存值到寄存器，计算，写寄存器值到内存三步。线程二可能在中间操作，原子性丧失`)。**可见性**：当多个线程同时访问同一个变量时，一个线程修改了这个变量的值，其他线程能够立即看得到修改的值。（`线程二操作时不知道线程一状态，观察变量是否修改和修改变量是分开的两个操作，可见性丧失`）**有序性**：程序执行的顺序按照代码的先后顺序执行（`编译器和处理器会为了优化代码性能而重新对指令排序，有序性丧失`）。

## 并发控制：互斥

:thinking:多个线程同时进入 **临界区(critical section)** 可能会发生**数据竞争(race condition)**，所以需要保证线程 **互斥(mutual exclusion)** ，即只有一个线程在临界区执行。在硬件没有提供更多原子指令前有很多尝试 (Control Interrupts,Just using Loads/Stores,Peterson) ，后来有了 **自旋锁(spin lock)** 和 **互斥锁(mutux lock)**，通过在临界区加 **锁(lock)** 可以实现互斥。

:question:如何理解自旋锁和互斥锁？

:memo:用不同的原子指令(Test-And-Set, Compare-And-Swap, Load-Linked and Store-Conditional, Fetch-And-Add)可以搭建自旋锁，自旋锁可能会出现队列中多个线程争抢一把锁空转，或是操作系统将拿到锁的线程切换出去(处理I/O操作)的情况。用操作系统休眠线程和唤醒线程的系统调用(Syscall)可以搭建互斥锁，互斥锁会使等待上锁的线程在解锁前休眠解锁时唤醒。两种锁结合起来总体性能更好，不同的操作系统都有对这种锁的接口支持。

## 并发控制：同步

## M1: 打印进程树

**POSIX**：可移植操作系统接口（Portable Operating System Interface of UNIX，缩写为 POSIX ）。POSIX是IEEE为要在各种 UNIX 操作系统上运行的软件而定义的一系列API标准的总称。这套标准涵盖了很多方面，比如Unix系统调用的C语言接口、shell程序和工具、线程及网络编程。

:memo: Linux 和 BSD 都是免费的，开源的，类Unix系统，许多在 Linux 上使用的软件同样也在 BSD 上使用。

**KISS原则**是英语 Keep It Simple, Stupid 的首字母缩略字，是一种归纳过的经验原则。KISS 原则是指在设计当中应当注重简约的原则。—— 中文Wiki

**Everything is a file** is an idea that Unix, and its derivatives handle input/output to and from resources such as documents, hard-drives, modems, keyboards, printers and even some inter-process and network communications as simple streams of bytes exposed through the filesystem name space. —— Wiki

**断言语句** `assert()` 通常用于检查用户的输入是否符合规定，还经常用作程序初期测试和调试过程中的辅助工具。在程序运行时它计算括号内的表达式，如果表达式为假, 程序将报告错误，并终止执行；如果表达式为真，则继续执行后面的语句。

```
ctrl+P                  命令行重复上一条命令
gcc a.c && ./a.out      一键编译运行
```
:memo: Linux下 `/proc` 保存了系统信息，其中数字编号的文件夹对应的就是进程  

:memo: Linux 管道使用竖线 `|` 连接多个命令，这被称为管道符。当在两个命令之间设置管道时，管道符 `|` 左边命令的输出就变成了右边命令的输入。

:memo: 输出重定向 `>` `>>` 是指命令的结果不再输出到显示器上，而是输出到其它地方，一般是文件中。这样做的最大好处就是把命令的结果保存起来，当我们需要的时候可以随时查询。