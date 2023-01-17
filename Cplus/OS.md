# 操作系统：设计与实现 南京大学

## 目录

[操作系统上的程序](#操作系统上的程序)
[多核处理器编程](#多核处理器编程)
[并发控制:互斥](#并发控制互斥)
[并发控制:同步](#并发控制同步)
[附录](#附录)

## 操作系统上的程序


:thinking: C语言程序可以理解成一个状态机。程序的全局变量是每条指令可以共同访问的资源，PC用来存放当前欲执行指令的地址。状态机的初始状态，是全局变量初始化，PC在main的第一条语句上。指令每执行一次，PC和全局变量就会发生变化，就相当于状态机的状态发生一次转移。当遇到函数调用和函数返回就相当于进入和走出一个局部的指令列表。

:memo:怎么理解一个最小的HelloWorld程序?

- [x] C语言写的 `printf("HelloWorld")` 不是实现对应功能的最小程序，因为它链接了很多库代码用了更加底层的函数，实际上程序只要有能打印HelloWorld的 **系统调用(system call)** 就足够了。



## 多核处理器编程

:thinking: 个人电脑一般是多核单CPU的，往往在一个核上会运行单个进程间的多个线程，或是不同进程间的多个线程，单核上线程调度属于**并发(Concurrency)**。历史上操作系统是第一个并发程序，很多并发应用程序技术也来自于此。

:memo:怎么理解并发程序的原子性、有序性和可见性？

- [x] 并发程序正确地执行，必须要保证原子性、可见性以及有序性。只要有一个没有被保证，就有可能会导致程序运行不正确。**原子性**：一个操作或多个操作要么全部执行完成且执行过程不被中断，要么就不执行（`以两个线程，都要对共享变量操作为例。操作可能是取内存值到寄存器，计算，写寄存器值到内存三步。线程二可能在中间操作，原子性丧失`)。**可见性**：当多个线程同时访问同一个变量时，一个线程修改了这个变量的值，其他线程能够立即看得到修改的值。（`线程二操作时不知道线程一状态，观察变量是否修改和修改变量是分开的两个操作，可见性丧失`）**有序性**：程序执行的顺序按照代码的先后顺序执行（`编译器和处理器会为了优化代码性能而重新对指令排序，有序性丧失`）。

## 并发控制：互斥

:thinking:多个线程同时进入 **临界区(critical section)** 可能会发生**数据竞争(race condition)**，所以需要保证线程 **互斥(mutual exclusion)** ，即只有一个线程在临界区执行。在硬件没有提供更多原子指令前有很多尝试 (Control Interrupts, Just using Loads/Stores, Peterson) ，后来有了 **自旋锁(spin lock)** 和 **互斥锁(mutux lock)**，通过在临界区加 **锁(lock)** 可以实现互斥。

:question:如何理解自旋锁和互斥锁？

:memo:用不同的原子指令(Test-And-Set, Compare-And-Swap, Load-Linked and Store-Conditional, Fetch-And-Add)可以搭建自旋锁。自旋锁带来的性能问题有，处理器间缓存同步延迟增加；队列中多个线程争抢一把锁空转，或是操作系统将拿到锁的线程切换出去(处理I/O操作)锁再也拿不到的情况。在自旋锁的基础上，组合操作系统休眠线程和唤醒线程的系统调用，可以搭建互斥锁。没抢到锁的线程进入休眠，抢到锁的线程解锁时会判断是否有线程等锁，有则唤醒线程直接递交锁无则解锁。不同的操作系统都有对这种系统调用的支持(Linux中为futux)。

## 并发控制：同步

:thinking:很多情况下，线程要检查满足一定条件后才能继续执行，所以要保证线程间的**同步(synchronization)**，典型的同步问题有**生产者消费者问题(Producer/Consumer Problem)** (one-P/C；mutli-P/C；Covering Conditions)，**哲学家吃饭问题(The Dining Philosophers)** 等；解决同步的方法有 **条件变量(Condition Variables)** (wait, signal, broadcast) 和 **信号量(Semaphores)** (Locks/CVs)。

:memo:怎么理解信号量和条件变量的使用？
条件变量使用 boardcast 时性能低，但不使用容易出错。信号量当成锁和信号量使用时很简洁，但在管理多种资源时并不好用。提供三种线程，能够分别打印 `< > _` ，对这些线程进行同步，使得打印出的序列总是 `<><` 和 `><>`并中间间隔有 `_` 的 '小鱼'图案组合 [fish.c](#fish)。在这个问题中使用条件变量 Covering Conditions 要比使用信号量更好。

## 操作系统的状态机模型

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

## 附录

<a id=fish>fish.C</a>

``` C
// fish.c
#include "thread.h"

#define LENGTH(arr) (sizeof(arr) / sizeof(arr[0]))

enum { A = 1, B, C, D, E, F, };

struct rule {
  int from, ch, to;
};

struct rule rules[] = {
  { A, '<', B },
  { B, '>', C },
  { C, '<', D },
  { A, '>', E },
  { E, '<', F },
  { F, '>', D },
  { D, '_', A },
};
// the first {<,>} thread come into fish_before determined the direct of fish
int current = A, quota = 1;

pthread_mutex_t lk   = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t  cond = PTHREAD_COND_INITIALIZER;

int next(char ch) {
  for (int i = 0; i < LENGTH(rules); i++) {
    struct rule *rule = &rules[i];
    if (rule->from == current && rule->ch == ch) {
      return rule->to;
    }
  }
  return 0;
}

void fish_before(char ch) {
  pthread_mutex_lock(&lk);
  while (!(next(ch) && quota)) {
    // can proceed only if (next(ch) && quota)
    // next(ch) return 0 if ch is not in {<,>,_}
    pthread_cond_wait(&cond, &lk);
  }
  quota--;
  pthread_mutex_unlock(&lk);
}

void fish_after(char ch) {
  pthread_mutex_lock(&lk);
  quota++;
  current = next(ch);
  assert(current);
  pthread_cond_broadcast(&cond);
  pthread_mutex_unlock(&lk);
}

const char roles[] = ".<<<>>___";
// all threads may be producers, may be consumers, may neither
// so we don't know how many producers and consumers are
// every threads (role in roles) just print one specific char

void fish_thread(int id) {
  char role = roles[id];
  while (1) {
    fish_before(role);
    putchar(role); // can be long; no lock protection
    fish_after(role);
  }
}

int main() {
  setbuf(stdout, NULL);
  for (int i = 0; i < strlen(roles); i++)
    create(fish_thread);
}

```