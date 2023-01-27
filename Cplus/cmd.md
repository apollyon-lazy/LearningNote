
```
文件目录管理：
    cd              切换目录 
    ls              查看目录中所有文件 
    pwd             显示当前工作路径
    mkdir rmdir     新建目录 删除空目录
    touch           创建文件及修改文件时间戳 
    cp rm           复制文件和目录 删除文件或文件夹    
    mv              移动或重命名文件和目录 
    file            查看文件类型
    tree            树状查看目录(需下载)
文本处理：
    cat             连接合并文件内容
    head tail       显示文件开头内容 显示文件结尾内容
    less            查看文件内容
    grep            查找文件内容
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
    objdump readelf     反汇编 读取ELF文件
    code .              链接到vscode并打开
毫无用处：
    cmatrix         符号雨(需下载)
```

``` 
gcc：
    gcc hello.c -o hello && ./hello         编译链接运行
    gcc -E hello.c -o hello.i               C转预处理 (Pre-Processing)
    gcc -S hello.i -o hello.s               预处理转汇编 (Compiling)
    gcc -c hello.s -o hello.o               汇编转机器 (Assembling)
    gcc hello.c -o hello_static --static    编译链接(静态) (Linking)
    -Wall                                   产生更多警告
    -Werror                                 所有警告当错误
    -O1 -O2                                 逐级优化代码
    -l                                      添加头文件搜索目录
    -L                                      添加库文件搜索目录
    -pthread                                链接POSIX线程库

```

```
man：
    /<string>                               查找字符串(支持正则表达式)
    n                                       移步下一个匹配字符串
    N                                       移步上一个匹配字符串
```

```
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

```
vim:
Command-mode:
    :wq             保存并退出
    q!              强制退出不保存
    set nu          显示行号            
    set nonu        取消显示行号
```

``` 
gdb:
    gcc a.c -g          编译时加入调试信息
    gdb -tui a.out      gdb图形界面tui调试程序
    b <line>            在行号处设置断点
    d                   删除断点
    p                   打印内部变量值
    r                   运行程序
    start               从main函数开始运行
    starti              从_start函数开始运行
    s                   单步执行进入函数调用
    n                   单步执行不进入函数调用
```

```
    strace <file> &| vim -  跟踪系统调用并导入vim
```