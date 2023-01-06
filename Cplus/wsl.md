## 安装 wsl 
https://www.bilibili.com/video/BV1aA411s7PJ/  
wsl 安装成功视频 —— b站 
https://learn.microsoft.com/en-us/windows/wsl/  
wsl 官方安装文档 —— 官网

## Terminal 和 VScode
在Microsoft store中安装Windows terminal，它是适用于**命令提示符**，**Powershell**，**wsl**等的终端应用程序。
```
wsl下的一些简单命令：
    mkdir <foldername>  新建空目录
    cd                  打开文件目录
    ls                  展示当前目录下所有文件
    pwd                 显示用户当前所在的目录
    cat <xxx>           查看目标文件内容
    code .              链接到vscode并打开
    ps                  显示当前进程的状态 (process status）
```
- [x] 这样就可以实现在Windows下编辑代码，在Linux下编译运行的效果

## Unix 和 Linux
http://c.biancheng.net/view/707.html  
Linux和Unix的关系及区别——C语言中文网 

UNIX 操作系统由肯•汤普森（Ken Thompson）和丹尼斯•里奇（Dennis Ritchie）发明。后来由芬兰人林纳斯·托瓦兹（Linus Torvalds）写了新的操作系统 Linux，它与 Unix 在外观和交互上类似，故也称是类 Unix 系统。Linux 开源后与缺少内核的 GNU 打包发布，故也称 GNU/Linux，后来大家省略 GNU 叫的 Linux 其实是类 Uinx 的内核和大量 GNU 开源软件的一个集合体。

<img src="./images/linux_1.jpg" width="100%">

Linux 发行版说简单点就是将 Linux 内核与应用软件进行一个打包，目前市面上知名的发行版有 Ubantu、CentOS 等等。Linux 下使用最广泛的 C/C++ 编译器是 gcc/g++，大多数的 Linux 发行版本都默认安装。

## 安装 gcc/g++（Ubantu）
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
- **GNU make** 是一个项目构建工具，即方便地编译、链接多个源代码文件，自动决定哪些源文件需要重新编译，从而高效地构建自己地项目。

- [x] 安装tldr有助于帮助更好的阅读文档；git有助于更好的版本管理；GNU make(怀疑就在bulid-essential包中)有助于高效的项目构建

## 配置自己的环境

- **Shell** 是一个应用程序，它连接了用户和 Linux 内核，让用户能够更加高效、安全、低成本地使用 Linux 内核，这就是 Shell 的本质。**bash**(**B**ourne **A**gain **Sh**ell)，由GNU开发的Shell，是各种Linux发行版标准配置的Shell。Fish（**F**riendly **I**nteractive **Sh**ell）最大特点就是方便易用，很多其他 Shell 需要配置才有的功能，Fish 默认提供，不需要任何配置。

    <img src="./images/linux_2.jpg" width="60%">

    Shell中输入的命令，有内置命令(cd,pwd等)，也有其他应用程序（一个程序就是一个命令），叫外部命令。
    
    ```
     echo $SHELL    查看当前使用的shell
     echo $0        查看当前使用的shell
     sudo apt install fish      安装 fish shell
     fish/bash      两种shell之间进行切换
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

- [x] C语言源代码写的HelloWorld可能不是实现对应功能的最小程序，因为其链接了很多库代码，实际上程序只要有能打印HelloWorld的系统调用(system call)就足够了，操作系统课(南大)上告诉我们程序在执行main函数之前其实发生很多事情。
- [x] 操作系统中常见的应用程序有Core Utilities (coreutils)（命令有cat，ls等）、系统/工具程序（bash,apt,vim,tmux,python等）、其他应用程序（浏览器、播放器等）

## 进程

**进程**是正在运行的程序的实例（Shell解释器进程中，执行一个命令就会创建一个子进程）。进程是系统资源分配的独立实体，每个进程都拥有独立的地址空间（查看进程linux中用ps命令，windows中用任务管理器）。

所谓**并发**，就是通过一种算法将 CPU 资源合理地分配给多个任务，当一个任务执行 I/O 操作时（I/O操作是相当耗时的），CPU 可以转而执行其它的任务，等到 I/O 操作完成以后，或者新的任务遇到 I/O 操作时，CPU 再回到原来的任务继续执行。

并发是针对单核 CPU 提出的，而**并行**则是针对多核 CPU 提出的。多核 CPU 的每个核心都可以独立地执行一个任务，而且多个核心之间不会相互干扰。在不同核心上执行的多个任务，是真正地同时运行，这种状态就叫做并行

http://c.biancheng.net/view/9486.html
并发与并行的区别 —— C语言中文网

<img src="./images/linux_4.jpg" width="100%">

