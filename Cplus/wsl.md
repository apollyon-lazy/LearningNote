## 目录

[安装 wsl (Windows Subsystem for Linux)](#安装-wsl-windows-subsystem-for-linux)  
[Terminal 和 VScode](#terminal-和-vscode)  
[Unix 和 Linux](#unix-和-linux)  
[安装gcc/g++(Ubantu)](#安装-gccgubantu)  
[熟悉基础命令行工具](#熟悉基础命令行工具)  
[配置自己的环境](#配置自己的环境)  
[进程与线程](#进程与线程)  
[并发与并行](#并发与并行)     
[库函数和系统调用](#库函数和系统调用)   
[main()函数的参数](#main函数的参数)  
[打印进程树](#打印进程树)  
[操作系统：设计与实现 —— 南京大学](#操作系统设计与实现--南京大学)   

## 安装 wsl (Windows Subsystem for Linux)
https://www.bilibili.com/video/BV1aA411s7PJ/  
wsl 安装成功视频 —— b站   
https://learn.microsoft.com/en-us/windows/wsl/  
wsl 官方安装文档 —— 官网

## Terminal 和 VScode
在Microsoft store中安装Windows terminal，它是适用于**命令提示符**，**Powershell**，**wsl**等的终端应用程序。
```
简单命令：
    mkdir <foldername>  新建空目录
    cd                  打开文件目录
    ls                  展示当前目录下所有文件
    pwd                 显示用户当前所在的目录
    cat <xxx>           查看目标文件内容
    code .              链接到vscode并打开
    ps                  显示当前进程的状态 
    rm                  删除文件或文件夹
    file                查看文件类型
    man                 查看帮助文档
```
- [x] 这样就可以实现在Windows下编辑代码，在Linux下编译运行的效果；链接到 VScode 后新建终端和外部终端（保持打开）作用一样

## Unix 和 Linux
http://c.biancheng.net/view/707.html  
Linux和Unix的关系及区别——C语言中文网 

UNIX 操作系统由肯•汤普森（Ken Thompson）和丹尼斯•里奇（Dennis Ritchie）发明。后来由芬兰人林纳斯·托瓦兹（Linus Torvalds）写了新的操作系统 Linux，它与 Unix 在外观和交互上类似，故也称是类 Unix 系统。Linux 开源后与缺少内核的 GNU 打包发布，故也称 GNU/Linux，后来大家省略 GNU 叫的 Linux 其实是类 Uinx 的内核和大量 GNU 开源软件的一个集合体。

<img src="./images/linux_1.jpg" width="100%">

Linux 发行版说简单点就是将 Linux 内核与应用软件进行一个打包，目前市面上知名的发行版有 Ubantu、CentOS 等等。

## 安装 gcc/g++（Ubantu）
Linux 下使用最广泛的 C/C++ 编译器是 gcc/g++，大多数的 Linux 发行版本都默认安装。

apt（Advanced Packaging Tool）是一个在 Debian 和 Ubuntu 中的 Shell 前端软件包管理器。
```
sudo apt update                     列出所有可更新的软件清单命令
sudo apt upgrade                    升级软件包
sudo apt install <package_name>     安装指定软件命令
!!! 安装失败考虑旧版命令 apt-get
sudo apt autoremove                清理不再使用的依赖和库文件
```

默认的 Ubuntu 软件源仓库中包含了一个软件包组，名称为 `build-essential`，它包含了 GNU 编辑器集合，GNU 调试器，和其他编译软件所必需的开发库和工具。很多开源项目包括 Linux kernel 和 GNU 工具，都是使用 gcc 进行编译的。GNU 编译器集合是一系列用于语言开发的编译器和库的集合，包括: C, C++, Objective-C, Fortran, Ada, Go, and D等编程语言。
```
sudo apt install bulid-essential    安装 bulid-essential
gcc --version                       打印 gcc 版本验证是否安装成功
```

https://blog.csdn.net/weixin_44718794/article/details/106751513  
wsl 链接到 VScode 编写 C/C++代码 检测到 #include 错误解决办法 —— CSDN

http://c.biancheng.net/view/475.html  
Linux gcc/g++ 简明教程 —— C语言中文网

- [x] 这样就掌握了在Linux下结合VScode编辑编译链接C/C++代码的技能
- [x] Linux内核大部分是用C语言编写的，还有部分是用汇编语言写的，因为在对于硬件上，汇编有更好的性能和速度。
- [x] Linux一个文件是否能被执行，和后缀名没有太大的关系，主要看文件的属性有关

## 熟悉基础命令行工具

- **tldr** = Too Long; Didn't Read，它简化了烦琐的man指令帮助文档，仅列出常用的该指令的使用方法。相比较man给出完整的帮助文档而言，大多数情况下，给出几个指令的使用demo可能正是我们想要的。

  https://github.com/tldr-pages/tldr 
  tldr —— github

  ```
      sudo apt install nodejs     安装 Node.js（JavaScript的运行环境）
      sudo apt install npm        安装 npm（Node.js官方提供的包管理工具）
      npm install -g tldr         安装 tldr
  ```
- **Git** 软件包被包含在 Ubuntu 默认的软件源仓库中，并且可以使用 apt 包管理工具安装。
  ```
      sudo apt install git        安装 git
      git --version               查看 git 版本
  ```
- **GNU make** 在 Linux（unix ）环境下使用GNU 的make工具能够比较容易的构建一个属于你自己的工程，整个工程的编译只需要一个命令就可以完成编译、连接以至于最后的执行。不过这需要我们投入一些时间去完成一个或者多个称之为Makefile 文件的编写。

- [x] 安装tldr有助于帮助更好的阅读文档；git有助于更好的版本管理；GNU make有助于构建工程；GNU make, bash, gcc, libc 属于是 GNU 免费软件，tldr, tmux 是 github 社区开源软件

## 配置自己的环境

- **Shell** 是一个应用程序，它连接了用户和 Linux 内核，让用户能够更加高效、安全、低成本地使用 Linux 内核，这就是 Shell 的本质。**bash**(**B**ourne **A**gain **Sh**ell)，由GNU开发的Shell，是各种Linux发行版标准配置的Shell。Fish（**F**riendly **I**nteractive **Sh**ell）最大特点就是方便易用，很多其他 Shell 需要配置才有的功能，Fish 默认提供，不需要任何配置。

    <img src="./images/linux_2.jpg" width="60%">

    Shell中输入的命令，有内置命令(cd,pwd等)，也有其他应用程序（一个程序就是一个命令），叫外部命令。
    
    ```  
     echo $SHELL    查看当前使用的shell
     echo $0        查看当前使用的shell
     sudo apt install fish      安装 fish shell
     fish/exit      进入fish/退出fish
     
     !!! 考虑bash和fish的不同，不设置fish为默认shell
    ```

    http://c.biancheng.net/view/706.html   
    什么是Shell —— C语言中文网 

- **Tmux** 是一个终端复用器（terminal multiplexer），非常有用，属于常用的开发工具。命令行的典型使用方式是，打开一个终端窗口（terminal window，以下简称"窗口"），在里面输入命令。用户与计算机的这种临时的交互，称为一次"会话"（session） 。会话的一个重要特点是，窗口与其中启动的进程是连在一起的。打开窗口，会话开始；关闭窗口，会话结束，会话内部的进程也会随之终止，不管有没有运行完。Tmux 就是会话与窗口的"解绑"工具，将它们彻底分离。
    ```
        tmux        进入tmux窗口
        Ctrl+d      退出tmux窗口
        窗格操作
        Ctrl+b %    划分左右两个窗格
        Ctrl+b "    划分上下两个窗格
        Ctrl+b <arrow key>      光标切换到其他窗格
        Ctrl+b Ctrl+<arrow key> 按箭头方向调整窗格大小
        Ctrl+b q    显示窗格编号
        Ctrl+b x    关闭当前窗格
    ```

- **Vim** 是一个基于文本界面的编辑工具，使用简单且功能强大。更重要的是，Vim 是所有 Linux 发行版本默认的文本编辑器。Linux Vim有三种工作模式（命令模式、输入模式和编辑模式）。
    <img src="./images/linux_3.jpg" width="100%">

    http://c.biancheng.net/linux_tutorial/40/  
    Vim文本编辑器 —— C语言中文网

- [x] 操作系统中常见的应用程序有Core Utilities (coreutils)（命令有cat，ls等）、系统/工具程序（bash,apt,vim,tmux,python等）、其他应用程序（浏览器、播放器等）

## 进程与线程

**进程**是资源分配的最小单位，**线程**是CPU调度的最小单位。进程间资源不共享，同类线程是共享同一进程分配的资源的。

:memo:Linux中查看进程用ps命令，windows中打开任务管理器

一个进程崩溃后，在保护模式下不会对其他进程产生影响，但是一个线程崩溃整个进程都死掉。所以多进程要比多线程健壮。每个独立的进程有程序运行的入口、顺序执行序列和程序出口。但是线程不能独立执行，必须依存在应用程序中，由应用程序提供多个线程执行控制，两者均可并发执行。

**临界区**指的是一个访问共用资源（例如：共用设备或是共用存储器）的程序片段，而这些共用资源又无法同时被多个线程访问的特性。 

每一个进程都有一个**进程号**（PID, Process Identification），进程号是一个正数，用以唯一标识系统中的某个进程。一个进程创建的另一个新进程称为子进程相反地，创建子进程的进程称为父进程。创建进程会不断递增进程号，全部使用完后会循环回一定值重新递增。Linux中PID分别是0,1(init),2的进程会在OS启动之后一直运行直到关机OS结束运行。

<img src="./images/linux_4.jpg" width="100%">



## 并发与并行

所谓**并发**，就是通过一种算法将 CPU 资源合理地分配给多个任务，当一个任务执行 I/O 操作时（I/O操作是相当耗时的），CPU 可以转而执行其它的任务，等到 I/O 操作完成以后，或者新的任务遇到 I/O 操作时，CPU 再回到原来的任务继续执行。

并发是针对单核 CPU 提出的，而**并行**则是针对多核 CPU 提出的。多核 CPU 的每个核心都可以独立地执行一个任务，而且多个核心之间不会相互干扰。在不同核心上执行的多个任务，是真正地同时运行，这种状态就叫做并行。

http://c.biancheng.net/view/9486.html
并发与并行的区别 —— C语言中文网


## 库函数和系统调用

系统调用是为了方便使用操作系统的接口，而库函数则是为了人们编程的方便。库函数调用与系统类型无关，不同的系统，调用库函数，库函数会针对系统调用不同的底层函数实现，因此可移植性好。

glibc是linux下面c标准库的实现，即GNU C Library。  
printf函数、glibc库和系统调用在系统中关系图如下：
<img src="./images/linux_5.jpg" width="100%">

## main()函数的参数

C 编译器允许main()函数没有参数，或者有两个参数（有些实现允许更多的参数，但这只是对标准的扩展）。这两个参数，一个是int类型，一个是字符串类型。第一个参数是命令行中的字符串数。按照惯例（但不是必须的），这个int参数被称为argc（argument count）。第二个参数是一个指向字符串的指针数组。命令行中的每个字符串被存储到内存中，并且分配一个指针指向它。按照惯例，这个指针数组被称为argv（argument value）。系统使用空格把各个字符串格开。一般情况下，把程序本身的名字赋值给argv[0]。

## 打印进程树
```
git clone https://github.com/NJU-ProjectN/os-workbench-2022 克隆仓库
git pull origin M1  下载分支
```

**POSIX**：可移植操作系统接口（Portable Operating System Interface of UNIX，缩写为 POSIX ）。POSIX是IEEE为要在各种 UNIX 操作系统上运行的软件而定义的一系列API标准的总称。这套标准涵盖了很多方面，比如Unix系统调用的C语言接口、shell程序和工具、线程及网络编程。

:memo: Linux 和 BSD 都是免费的，开源的，类Unix系统，许多在 Linux 上使用的软件同样也在 BSD 上使用。

**KISS原则**是英语 Keep It Simple, Stupid 的首字母缩略字，是一种归纳过的经验原则。KISS 原则是指在设计当中应当注重简约的原则。—— 中文Wiki

**Everything is a file** is an idea that Unix, and its derivatives handle input/output to and from resources such as documents, hard-drives, modems, keyboards, printers and even some inter-process and network communications as simple streams of bytes exposed through the filesystem name space. —— Wiki

assert() 语句（**断言语句**）通常用于检查用户的输入是否符合规定，还经常用作程序初期测试和调试过程中的辅助工具。在程序运行时它计算括号内的表达式，如果表达式为假, 程序将报告错误，并终止执行；如果表达式为真，则继续执行后面的语句。

```
ctrl+P                  命令行重复上一条命令
gcc a.c && ./a.out      一键编译运行
```
:memo: Linux下 `/proc` 保存了系统信息，其中数字编号的文件夹对应的就是进程  

https://en.wikipedia.org/wiki/Procfs   
Linux /prof目录说明——Wiki

:memo: Linux 管道使用竖线 `|` 连接多个命令，这被称为管道符。当在两个命令之间设置管道时，管道符 `|` 左边命令的输出就变成了右边命令的输入。

:memo: 输出重定向 `>` `>>` 是指命令的结果不再输出到显示器上，而是输出到其它地方，一般是文件中。这样做的最大好处就是把命令的结果保存起来，当我们需要的时候可以随时查询。

## 操作系统：设计与实现 —— 南京大学

**操作系统上的程序**

:memo:怎么理解C语言程序是一个状态机?

- [x] C语言程序可以理解成一个状态机。程序的全局变量是每条指令可以共同访问的资源，PC(Program Counter,PC)用来存放当前欲执行指令的地址。状态机的初始状态，是全局变量初始化，PC在main的第一条语句上。指令每执行一次，PC和全局变量就会发生变化，就相当于状态机的状态发生一次转移。当遇到函数调用和函数返回就相当于进入和走出一个局部的指令列表。

:memo:怎么理解一个最小的HelloWorld程序?

- [x] C语言写的 `printf("HelloWorld")` 不是实现对应功能的最小程序，因为它链接了很多库代码用了更加底层的函数，实际上程序只要有能打印HelloWorld的系统调用(system call)就足够了。程序在执行main函数之前其实也发生很多事情。



**多核处理器编程**

:question: 个人电脑一般是多核单CPU的，往往在一个核上会运行单个进程间的多个线程，或是不同进程间的多个线程，单核上线程调度属于并发。`那么带着疑问，操作系统是如何帮助在单核上并发的？`

:memo:怎么理解并发程序的原子性、有序性和可见性？

- [x] 并发程序正确地执行，必须要保证原子性、可见性以及有序性。只要有一个没有被保证，就有可能会导致程序运行不正确。**原子性**：一个操作或多个操作要么全部执行完成且执行过程不被中断，要么就不执行（`比如两个线程，线程一要对共享变量操作，线程二在线程一操作中就参与进来，原子性丧失`)。**可见性**：当多个线程同时访问同一个变量时，一个线程修改了这个变量的值，其他线程能够立即看得到修改的值。（`线程二操作时，不知道线程一有没有修改共享变量，可见性丧失`）**有序性**：程序执行的顺序按照代码的先后顺序执行（`编译器和处理器会为了优化代码性能而重新对指令排序，有序性丧失`）。

**理解并发程序执行**

:memo:怎么理解单进程并发程序的执行过程？

- [x] 并发程序的基本单位是线程。并发程序可以看做是多个执行流，有共享内存，每一步并不确定哪个线程执行的状态机。实现两个线程间互斥的一个算法，Peterson算法（`厕所？举旗？贴纸？`）。

**并发控制：互斥**

