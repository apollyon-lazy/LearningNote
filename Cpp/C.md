# 《C primer plus》

[[#第13章 文件输入/输出]]

## 第13章 文件输入/输出

### 参考小节

- 13.1 与文件进行通信
- 13.2 标准I/O
- 13.4 文件I/O:fprintf(),fscanf(),fgets(),fputs()

### 知识点总结

- C 库函数 `void exit(int status)` 立即终止调用进程，`0` 或 `EXIT_SUCCESS` 代表程序正常退出，`EXIT_FAILURE`代表结束程序失败， 在 main 函数中等价于 `return`
- Unix 和 Linux 只有一种文件类型的系统，用文本模式和二进制模式打开的文件是一样的
- `FILE *fp` 文件指针并不指向实际的文件，它指向一个包含文件信息的数据对象，包含操纵文件I/O函数所用的缓冲区信息。

### 可查阅问题

Q: `fscanf()`,`fprintf()`,(格式化读取/打印一行);`fgets()`,`fputs()`（读取/打印一行）的用法？(P421-422)
Q: 如何理解EOF(End Of File Condition)?   [EOF是什么](http://ruanyifeng.com/blog/2011/11/eof.html)
