# cmd

命令行 是具体的一行命令；命令行工具 是有具体功能的一个命令集合；命令提示符是Windows系统下 cmd.exe 程序的中文名，也是Linux系统中命令前的符号表示。

## Linux

``` shell
Everying is a file:
    /root   管理员的主目录
    /home   存放用户主目录的文件夹
    
    /proc   系统内存的映射(虚拟目录即不在硬盘上)
```

## Shell

``` shell
文件目录管理：
    cd              切换目录 
    ls              查看目录中所有文件 
    pwd             显示当前工作路径
    mkdir rmdir     新建目录 删除空目录
    touch           创建文件及修改文件时间戳 
    cp rm           复制文件和目录 删除文件或文件夹    
    mv              移动或重命名文件和目录 
    file            查看文件类型
    tty             返回终端名
    tree            树状查看目录(需下载)

文本处理：
    cat             连接合并文件内容
    head tail       显示文件开头内容 显示文件结尾内容
    less            查看文件内容
    grep            查找文件内容
    echo            打印参数
    wget            网页上下载文件

系统管理：
    ps              显示当前进程的状态   
    pstree          打印进程树 
    top             实时监听进程运行状态
    jobs            查看暂停进程
    fg bg           放入前台 放入后台
    pmap            查看进程地址空间
    which           定位程序位置

特殊符号和快捷键：
    ctrl+Z          暂停进程放入后台
    ctrl+P          重复执行上一条命令
    ctrl+C          退出当前进程
    > | &           重定向 管道 后台执行

代码：
    code .              链接到vscode并打开

GNU Binutils:
    ld objdump readelf      链接器 反汇编 读取ELF文件

毫无用处：
    cmatrix         符号雨(需下载)
```

## Man

``` shell
man：
    /<string>               查找字符串(支持正则表达式)
    n                       移步下一个匹配字符串
    N                       移步上一个匹配字符串
```

## Apt

``` shell
apt/apt-get:
    sudo apt update                     列出所有可更新的软件清单命令
    sudo apt upgrade                    升级软件包
    sudo apt install <package_name>     安装指定软件命令
    sudo apt autoremove                 清理不再使用的依赖和库文件
```

## GCC

``` shell
gcc：
    gcc hello.c -o hello && ./hello         编译链接重命名并运行
    gcc -E hello.c -o hello.i               C转预处理 (Pre-Processing)
    gcc -S hello.i -o hello.s               预处理转汇编 (Compiling)
    gcc -c hello.s -o hello.o               汇编转机器 (Assembling)
    gcc hello.c -o hello_static --static    编译链接(静态) (Linking)
    -ffreestanding                          无依赖环境(无标准库)
    -Wall                                   产生更多警告
    -Werror                                 所有警告当错误
    -O1 -O2                                 逐级优化代码
    -l                                      添加头文件搜索目录
    -L                                      添加库文件搜索目录
    -pthread                                链接POSIX线程库
# gcc hello.c / gcc -E / gcc -S / gcc -c 
# 对应生成的默认文件是 a.out / hello.i / hello.s / hello.o
```

## Tmux

``` shell
tmux：
    tmux                            进入tmux窗口
    Ctrl+d                          退出tmux窗口

窗格操作：
    Ctrl+b %                        划分左右两个窗格
    Ctrl+b "                        划分上下两个窗格
    Ctrl+b <arrow key>              光标切换到其他窗格
    Ctrl+b Ctrl+<arrow key>         按箭头方向调整窗格大小
    Ctrl+b q                        显示窗格编号
    Ctrl+b x                        关闭当前窗格
```

## Vim

``` shell
vim:
Command-mode:
    :wq             保存并退出
    q!              强制退出不保存
    set nu          显示行号            
    set nonu        取消显示行号

    [range]s/{pattern}/{string}/[option]  替换字符串
    在[range]的每一行中搜索{pattern}并替换为[string]设置为[option]
    %s/:/\r/cg      搜索所有行(%)把(:)替换成(\r)(c)所有替换都询问(g)不止替换第一个
```

## GDB

``` shell
gdb:
    gcc a.c -g          编译时加入调试信息
    gdb -tui a.out      gdb图形界面tui调试程序

    layout asm          进入汇编
    layout src          进入源码
    b <line>            在行号处设置断点
    d                   删除断点
    p                   打印内部变量值($寄存器)
    r                   运行程序
    start               从main函数开始运行
    starti              从_start函数开始运行
    s                   单步执行进入函数调用
    n                   单步执行不进入函数调用
    info registers      查看寄存器
```

## Qemu

``` shell
    ctrl A + X             退出虚拟机
    ctrl A + C             控制台与监控器切换
monitor mode:
    info mem                显示虚拟内存映射
```

## Combo

``` shell
    strace <file> &| vim -  后台跟踪系统调用并导入vim
    env | grep PATH | vim - 抓取PATH环境变量并导入vim
    echo $PATH              查看环境变量
```
