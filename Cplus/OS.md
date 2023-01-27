# 操作系统：设计与实现 南京大学

## 目录

[操作系统上的程序](#操作系统上的程序)   
[多核处理器编程](#多核处理器编程)   
[并发控制:互斥](#并发控制互斥)  
[并发控制:同步](#并发控制同步)
[操作系统的状态机模型](#操作系统的状态机模型)
[操作系统上的进程](#操作系统上的进程)
[进程的地址空间](#进程的地址空间)
[附录](#附录)   

## 操作系统上的程序


:thinking: C语言程序可以理解成一个状态机。程序的全局变量是每条指令可以共同访问的资源，PC用来存放当前欲执行指令的地址。状态机的初始状态，是全局变量初始化，PC在main的第一条语句上。每执行一条指令，就相当于状态机的状态发生一次转移。当遇到函数调用和函数返回，相当于进入和离开一个局部的指令列表。

:memo:怎么理解一个最小的HelloWorld程序?

- [x] C语言写的 `printf("HelloWorld")` 不是实现相应功能的最小程序，因为链接的库 `stdio.h` 本身包含了许多不同的代码，增加了程序的体量。打印字符，也就是读取寄存器中的字符串，写入到标准输出的一个过程，用低级语言加 **系统调用 system call** 完全可以写出不用链接打印字符串的程序。



## 多核处理器编程

:thinking: 个人电脑一般是多核单CPU的，往往在一个核上会运行单个进程间的多个线程，或是不同进程间的多个线程，单核上线程调度属于**并发(Concurrency)**。历史上操作系统是第一个并发程序，很多并发应用程序技术也来自于此。

:memo:怎么理解并发程序的原子性、有序性和可见性？

- [x] 并发程序正确地执行，必须要保证原子性、可见性以及有序性。只要有一个没有被保证，就有可能会导致程序运行不正确。**原子性**：一个操作或多个操作要么全部执行完成且执行过程不被中断，要么就不执行（`以两个线程，都要对共享变量操作为例。操作可能是取内存值到寄存器，计算，写寄存器值到内存三步。线程二可能在中间操作，原子性丧失`)。**可见性**：当多个线程同时访问同一个变量时，一个线程修改了这个变量的值，其他线程能够立即看得到修改的值。（`线程二操作时不知道线程一状态，观察变量是否修改和修改变量是分开的两个操作，可见性丧失`）**有序性**：程序执行的顺序按照代码的先后顺序执行（`编译器和处理器会为了优化代码性能而重新对指令排序，有序性丧失`）。

## 并发控制：互斥

:thinking:多个线程同时进入 **临界区(critical section)** 可能会发生**数据竞争(race condition)**，所以需要保证线程 **互斥(mutual exclusion)** ，即只有一个线程在临界区执行。在硬件没有提供更多原子指令前有很多尝试 (Control Interrupts, Just using Loads/Stores, Peterson) ，后来有了 **自旋锁(spin lock)** 和 **互斥锁(mutux lock)**，通过在临界区加 **锁(lock)** 可以实现互斥。

:memo:如何理解自旋锁和互斥锁？

- [x] 用不同的原子指令(Test-And-Set, Compare-And-Swap, Load-Linked and Store-Conditional, Fetch-And-Add)可以搭建自旋锁。自旋锁带来的性能问题有，处理器间缓存同步延迟增加；队列中多个线程争抢一把锁空转，或是操作系统将拿到锁的线程切换出去(处理I/O操作)锁再也拿不到的情况。在自旋锁的基础上，组合操作系统休眠线程和唤醒线程的系统调用，可以搭建互斥锁。没抢到锁的线程进入休眠，抢到锁的线程解锁时会判断是否有线程等锁，有则唤醒线程直接递交锁无则解锁。不同的操作系统都有对这种系统调用的支持(Linux中为futux)。

## 并发控制：同步

:thinking:很多情况下，线程要检查满足一定条件后才能继续执行，所以要保证线程间的**同步(synchronization)**，典型的同步问题有**生产者消费者问题(Producer/Consumer Problem)** (one-P/C；mutli-P/C；Covering Conditions)，**哲学家吃饭问题(The Dining Philosophers)** 等；解决同步的方法有 **条件变量(Condition Variables)** (wait, signal, broadcast) 和 **信号量(Semaphores)** (Locks/CVs)。

:memo:怎么理解信号量和条件变量的使用？
条件变量使用 boardcast 时性能低，但不使用容易出错。信号量当成锁和信号量使用时很简洁，但在管理多种资源时并不好用。提供三种线程，能够分别打印 `< > _` ，对这些线程进行同步，使得打印出的序列总是 `<><` 和 `><>`并中间间隔有 `_` 的 '小鱼'图案组合 [fish.c](#fish)。在这个问题中使用条件变量 Covering Conditions 要比使用信号量更好。

## 操作系统的状态机模型

:thinking:计算机按下电源按钮后，会给硬件资源一个重置信号，硬件的初始状态由硬件开发的厂商决定(可在手册上查阅)。处理器初始化后，PC一般指向ROM（只读存储器 Read-Only Memory），ROM存储了厂商提供的固件（firmware）。这样的固件有BIOS（基本输入输出系统 Basic Input Output System）和UEFI（统一可扩展固件接口，Unified Extensible Firmware Interface），UEFI正逐步替代传统的BIOS以满足硬件高速发展的需求。固件程序首先硬件自检，出现问题主板会蜂鸣报警终止启动；接着固件按照外部储存设备(磁盘、U盘等断电数据不丢失的设备)启动顺序，读取第一个储存设备的第一个扇区(512个字节)到内存中，也叫MBR(主引导记录 Master boot record)；根据MBR可以逐步找到操作系统储存的位置，或者运行启动管理器(boot loader)，由用户选择启动哪一个操作系统（Linux中是Grub）；操作系统获得控制权后，内核载入内存，产生第一个进程（Linux是init）。

## 操作系统上的进程

:thinking:Shell 接收到命令后，在操作系统中使用 fork() 创建一个新的进程。在子进程中使用 execve() 加载 a.out。操作系统内核中的加载器识别出 a.out 是一个动态链接文件，做出必要的内存映射，从 `ld-linux-x86-64.so`（负责动态链接库的加载，没有它就无法加载像libc的动态库）的代码开始执行，把动态链接库映射到进程的地址空间中，然后跳转到 a.out 的 _start执行（由名为 `crt*.o` 等文件提供，这些文件包含C运行时环境的启动代码等），初始化 C 语言运行环境，最终开始执行 main。程序运行过程中，如需进行输入/输出等操作 (如 libc 中的 putchar)，则会使用特殊的指令 (例如 x86 系统上的 int 或syscall) 发出系统调用请求操作系统执行。典型的例子是 printf 会调用 write 系统调用，向编号为 1 的文件描述符写入数据。

:memo:如何理解操作系统中的C程序，裸机上的C程序？
C程序要经过预处理，编译，汇编，链接才能得到可执行文件。操作系统中的C程序过程往往是，Shell得到命令后，操作系统先fork()再execve()再用加载器识别文件，做出内存映射，执行ld-linux-x86-64.so执行_start函数最后执行main。裸机上的C程序可以认为是CPU Reset后，Firmware读取MBR中的Boot loader，接着执行'kernel'程序的_start函数执行(操作系统也是一个C程序)。综上，只要知道main函数之前初始化好了C程序环境并能够使用一点库函数足矣。

:memo:系统调用fork，execve，mmap的作用？
操作系统运行起来，创建第一个进程init，然后用它创建出更多进程。系统调用fork复刻一个新进程，系统调用execve初始化进程状态，系统调用mmap映射进程空间。fork和execve之间可以是改变程序运行环境的代码，这为shell提供了便利。
## 进程的地址空间


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