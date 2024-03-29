## 操作系统上的程序


📝如何理解程序是一个状态机？

C语言程序可以理解成一个状态机。程序的全局变量是每条指令可以共同访问的资源，PC用来存放当前欲执行指令的地址。状态机的初始状态，是全局变量初始化，PC在main的第一条语句上。每执行一条指令，就相当于状态机的状态发生一次转移。当遇到函数调用和函数返回，相当于进入和离开一个局部的指令列表。

📝怎么理解一个最小的HelloWorld程序?

C语言写的 `printf("HelloWorld")` 不是实现相应功能的最小程序，因为链接的库 `stdio.h` 本身包含了许多不同的代码，增加了程序的体量。打印字符，也就是读取寄存器中的字符串，写入到标准输出的一个过程，用低级语言加 **系统调用(system call)** 完全可以写出不用链接打印字符串的程序。

## 多核处理器编程

🤔个人电脑一般是多核单CPU的，往往在一个核上会运行单个进程间的多个线程，或是不同进程间的多个线程，单核上线程调度属于 **并发(Concurrency)**。历史上操作系统是第一个并发程序，很多并发应用程序技术也来自于此。—— **OSTEP26**

📝怎么理解并发程序的原子性、有序性和可见性？

并发程序正确地执行，必须要保证原子性、可见性以及有序性。只要有一个没有被保证，就有可能会导致程序运行不正确。**原子性**：一个操作或多个操作要么全部执行完成且执行过程不被中断，要么就不执行（`以两个线程，都要对共享变量操作为例。操作可能是取内存值到寄存器，计算，写寄存器值到内存三步。线程二可能在中间操作，原子性丧失`)。**可见性**：当多个线程同时访问同一个变量时，一个线程修改了这个变量的值，其他线程能够立即看得到修改的值。（`线程二操作时不知道线程一状态，观察变量是否修改和修改变量是分开的两个操作，可见性丧失`）**有序性**：程序执行的顺序按照代码的先后顺序执行（`编译器和处理器会为了优化代码性能而重新对指令排序，有序性丧失`）。

## 并发控制：互斥

🤔多个线程同时进入 **临界区(critical section)** 可能会发生**数据竞争(race condition)**，所以需要保证线程 **互斥(mutual exclusion)** ，即只有一个线程在临界区执行。在硬件没有提供更多原子指令前有很多尝试 (Control Interrupts, Just using Loads/Stores, Peterson) ，后来有了 **自旋锁(spin lock)** 和 **互斥锁(mutux lock)**，通过在临界区加 **锁(lock)** 可以实现互斥。—— **OSTEP28**

📝如何理解自旋锁和互斥锁？

用不同的原子指令(Test-And-Set, Compare-And-Swap, Load-Linked and Store-Conditional, Fetch-And-Add)可以搭建自旋锁。自旋锁带来的性能问题有，处理器间缓存同步延迟增加；队列中多个线程争抢一把锁空转，或是操作系统将拿到锁的线程切换出去(处理I/O操作)锁再也拿不到的情况。在自旋锁的基础上，组合操作系统休眠线程和唤醒线程的系统调用，可以搭建互斥锁。没抢到锁的线程进入休眠，抢到锁的线程解锁时会判断是否有线程等锁，有则唤醒线程直接递交锁无则解锁。不同的操作系统都有对这种系统调用的支持(Linux中为futux)。

## 并发控制：同步

🤔很多情况下，线程要检查满足一定条件后才能继续执行，所以要保证线程间的**同步(synchronization)**，典型的同步问题有**生产者消费者问题(Producer/Consumer Problem)** (one-P/C；mutli-P/C；Covering Conditions)，**哲学家吃饭问题(The Dining Philosophers)** 等；解决同步的方法有 **条件变量(Condition Variables)** (wait, signal, broadcast) 和 **信号量(Semaphores)** (Locks/CVs)。—— **OSTEP30,31**

📝信号量和条件变量如何选用？

条件变量使用 boardcast 时性能低，但不使用容易出错。信号量当成锁和信号量使用时很简洁，但在管理多种资源时并不好用。提供三种线程，能够分别打印 `< > _` ，对这些线程进行同步，使得打印出的序列总是 `<><` 和 `><>`并中间间隔有 `_` 的 '小鱼'图案组合 。在这个问题中使用条件变量 Covering Conditions 要比使用信号量更好。

## 操作系统的状态机模型

📝计算机按下操作按钮到操作系统运行发生了什么？

计算机按下电源按钮后，会给硬件资源一个重置信号，硬件的初始状态由硬件开发的厂商决定(可在手册上查阅)。处理器初始化后，PC一般指向**ROM**（只读存储器 Read-Only Memory），ROM存储了厂商提供的**固件（firmware**）。这样的固件有**BIOS**（基本输入输出系统 Basic Input Output System）和**UEFI**（统一可扩展固件接口，Unified Extensible Firmware Interface），UEFI正逐步替代传统的BIOS以满足硬件高速发展的需求。固件程序首先硬件自检，出现问题主板会蜂鸣报警终止启动；接着固件按照外部储存设备(磁盘、U盘等断电数据不丢失的设备)启动顺序，读取第一个储存设备的第一个扇区(512个字节)到内存中，也叫**MBR**(主引导记录 Master boot record)；根据MBR可以逐步找到操作系统储存的位置，或者运行**启动管理器**(boot loader)(Linux中是Grub)，由用户选择启动哪一个操作系统；操作系统获得控制权后，内核载入内存，产生第一个进程（Linux是init）。

## 可执行文件

📝可执行文件是什么(分析静态链接的可执行文件)？

分析**静态链接**的可执行文件。到第一条指令 `_start` 时，操作系统会把PC(寄存器rip)指定好，初步分配好地址空间。寄存器大部分初始值在ABI(Application Binary Interface)规范中有规定，操作系统负责设置；地址空间初始值由可执行文件(二进制文件)和ABI共同决定。`可执行文件(二进制文件)本质上是程序的初始状态(作为execve的输入)和迁移的数据结构。` Linux中的She-bang指令 `!#` 可以偷换execve的第一个参量。解析可执行文件工具是GNU binutils，查看执行时的运行状态有GDB，遵循DWARF调试标准。可重定向文件因为没有链接，并不知道调用函数的第一条指令具体地址在哪，这时候ELF中就会存储约束信息帮助计算地址偏移量，由**链接器**来补全代码。可以看出，ELF文件数据结构是因不同需求而逐渐变得复杂的(文件头，程序头等)，那么一个简洁的只满足编译链接需求的可执行文件信息数据结构也是可以想象出来的。

## 可执行文件的加载

📝可执行文件如何被操作系统加载？

Linux的**加载器**在操作系统内，它解析ELF文件数据结构，并把允许加载到内存的部分复制到内存当中(进程的栈遵循ABI标准)，然后跳转到程序的第一条指令(Boot loader加载操作系统也是遵循标准的)。

📝如何理解动态链接/动态加载(分析动态链接的可执行文件)？

设计**动态链接**的可执行文件基本要求有，能够加载动态链接库(对应ld-linux-x86-64.so文件功能)，能够加载外部符号(链接)，能够为动态库导出符号(被链接)。动态链接的可执行文件到加载时才知道要链接的文件地址在哪里，基本原理是查ELF文件中符号表，就有了GOT(Global Offset Table)和PLT(Procedure Linkage Table)，对于链接文件中的数据，加载器会保证数据在所有程序中只有一个副本。

## 虚拟化内存

🤔虚拟化内存不仅需要硬件支持进行**地址转换(address translation)**，也需要操作系统在关键时刻介入以便管理内存。总结一下硬件支持：硬件应该提供两种模式，**用户模式(user mode)** 和 **特权/内核模式(privileged mode/kernel mode)**；硬件CPU上还需提供**基址界限寄存器(base and bounds register)**，提供负责地址转换的**内存管理单元(Memory Management Unit，MMU)**；硬件还应提供在内核模式下的，用于修改基址界限寄存器的指令；最后在发生非法访问内存(越界访问)等情况时，CPU必须能够产生**异常(exception)**，停掉进程切换到操作系统，由操作系统执行相应的**异常处理程序(exception handler)**。总结一下操作系统作用：要为地址空间分配内存空间；在进程终止时，要回收内存空间；在上下文切换时，需要把基址界限寄存器中的内容保存在内存当中或者给基址界限寄存器中设置正确的值；最后还要提供异常处理程序。——**OSTEP 15**

🤔为了充分利用内存空间，可以引入多个基址界限寄存器进行**分段(sagmentation)** 。内存空间分配过程中会出现很多空闲小空间，很难分配新的大段空间的情况，这种问题称为**外部碎片(external fragmentation)**。解决这个问题的做法有，重新分配内存使得空间紧凑，或者利用**空闲列表(free list)** 管理算法(best-fit, worse-fit, first-fit, next-fit, segregated list, buddy allocation等)在管理上试图减少问题的产生。—— **OSTEP 16,17**

🤔容易实现的分配空间的想法是按照固定长度分段，这种想法叫做**分页(paging)**。预处理数据结构**页码表(page table)**，存储着虚拟地址到物理地址的转换信息，通常每个进程会有一个页码表。通过索引**虚拟页码(virtual page number, VPN)**，查找**页码入口(page-table entry, PTE)**，得到期望的**物理页码(physical frame number, PFN)**，每个PTE上还有许多不同功能的位(valid bit, protection bits, present bit, dirty bit, referce bit等)。为了快速加载地址转换的信息，硬件在处理器核心旁增加了像缓存一样的**地址转换旁路缓冲寄存器(translation-lookaside buffer, TLB)**，每有内存访问硬件先检查TLB有没有当前进程的转换信息，如果有就不必再到内存中找表。 —— **OSTEP 18 19**

## 虚拟化CPU

🤔虚拟化CPU用到的机制是**受限直接执行(limited direct execution，LDE)**。如果进程执行受限制的操作怎么办？在系统引导时(at boot time)，内核初始化 **陷阱表(trap table)**，CPU会记住位置以供后续使用。在进程运行时(when running a process)，使用 **陷阱(trap)** 指令陷入内核，执行完系统调用后通过 **陷阱返回(return-from-trap)** 指令，将控制权返还进程。如果是进程发生切换怎么办？协作方式是等待系统调用，非协作方式是操作系统通过 **时钟中断(time interrupt)** 重新获取控制权。进程的切换由操作系统的 **调度器(scheduler)** 决定，切换时存在**上下文切换(context switch)**。 —— **OSTEP 6**

:thinking:确定调度策略考虑的指标有 **周转时间(turnaround time)**(FIFO，SJF，STCF) 和 **响应时间(response time)**(RR)。为同时优化两种指标有**多级反馈队列(Multi-level Feedback Queue, MLFQ)** 调度策略，已被广泛用于多种操作系统当中。除此之外还有 **比例份额(proportional-share)** 调度策略，代表例子是**彩票调度(lottery scheduling)**。 —— **OSTEP 8 9**

## 存储1bit的数据

🤔持久保存数据需要容量大，速度快，可靠性好，价格便宜的持久存储介质。磁带(Magenetic Tape)，磁鼓(Magnetic Drum)，**机械硬盘(HDD，Hard Disk Drive)** 利用磁的原理存储数据，存在机械部件，损伤会导致数据损坏。读写磁道(track)上的一个扇区(sector)，先要把读写头(disk head)移动到对应的磁道(seek)，再将盘片(platter)绕轴(spindle)旋转到读写头的位置(rotation)，最后读写数据(transfer)。磁盘还能在缓存/调度(SSTF, Elevator, SPTF)等地方调优性能。**软盘(Floppy Disk)** 把读写头和盘片分开以实现数据移动，现在软件上保存按钮的图标就是当时软盘的形状，早先电脑的A，B盘符也是为软盘而预留，后来实用性上被 U 盘取代。—— **OSTEP 37**

:thinking:CD(Compact Disk)通过在反射平面上挖坑来存储数据，在实用性上被网络淘汰。基于闪存的 **固态硬盘(SSD，Solid State Drive)** 和U盘(USB Flash Disk)利用电的原理存储数据。不建议U盘上存储重要数据，是因为擦除次数有限存在**耗尽(wear out)** 问题。SSD上藏着各自厂商的小的计算机系统，有类似CPU，缓存甚至操作系统的部件在内，而SD卡因为没有严格的标准市面上不尽相同。

📝 如何建立一个基于闪存的SSD?

闪存芯片(falsh chip)支持三种底层操作，读取(read，以page为单位)，擦除(erase，以block为单位)，编程(program，以page为单位)。SSD能表现出以block为单位的读/写性能，是通过闪存翻译层(flash translation layer, FTL)把读/擦除/编程操作隐藏起来。大多FTLs是日志结构(log-structured)的，通过减少擦除/编程循环来减少写的开销，它的一个重要问题是无用单元回收(garbage collection)，这可能导致写入放大(write amplification，实际写入的数据比要写数据大)；另一个重要问题是映射表(mapping table)的大小，使用混合映射(hybrid mapping)或者缓存(caching)可能修补；最后一个问题是耗损均衡(wear leveling)，要迁移数据保证block有尽可能相同的擦除/编程负载。—— **OSTEP 44**

## 输入输出设备

![[os1.jpg]]
🤔如今**输入输出设备(I/O Device)** 的系统架构是物理限制和成本的迭代折中结果。I/O设备通常包括两部分，硬件接口(interface)和内部结构(internal stucture)。接口可以抽象为 Status，Command，Data 三种类型寄存器的集合；内部结构可以是实现功能的芯片，也可以是一个小的计算机系统(CPU, Memory等)。CPU连接 Memory 有 Memory Bus，连接一般的I/O设备有 I/O bus (像是GPU或其他高性能的设备上会用PCI或它的衍生)，连接外部设备(磁盘，鼠标，键盘等)有 peripheral bus (SCSI，SATA，USB等)。设备可以发送中断(interrupt)信号使CPU切换到OS执行中断程序，使用 **DMA(Dierct Memory Access)** 专门执行设备和内存间的数据传输以解放CPU的工作。图形显示器也是类似单独分离出来(打比方CPU负责生成怎么绘图的指令，那么GPU就负责按照指令执行绘图)。从NES的PPU要靠把马里奥中板栗的左右脚来回翻转实现运动，滚动卷轴式的截取背景图像等这些小技巧做游戏，到今天的GPU能够进行大量图形学中的矩阵运算(NVDIA CUDA)，GPU已经看成是计算密集型任务的另一台计算机(Pytorch和炼丹炉)。—— **OSTEP 36**

📝举几个例子来说明硬件是如何抽象被OS管理的？
比如串口(Universal Asynchronous Receiver/Transmitter, UART)芯片中围绕RX和TX的编程；键盘在CapsLock，NumLock按键按下后指示灯会受到控制亮起(可以由程序控制)；磁盘控制器的接口(ATA，SATA，eSATA存储接口的进化)；打印机(另一个带有CPU的设备)还有属于自己的编程指令 PostScript (PDF是这套指令的超集)。

## 设备驱动程序

🤔 为了让OS对大部分I/O设备保持中立，并隐藏I/O设备和OS子系统间的寄存器交互细节，在OS中底层机制上进行一层抽象，由名为 **设备驱动程序(device driver)** 的软件在工作。对I/O设备的操作首先是能从中读/写字节序列，其次要求OS能够完成对设备的各类操作，这样操作可以主要归结为从设备某个指定位置读出数据(read)，向设备某个指定位置写入数据(write)，读取/设置设备的状态(ioctl)等，这些属于通用的API接口(系统调用)。在Shell中输入指令会被Shell程序翻译成系统调用，系统调用会被设备驱动程序执行为对相应设备的I/O操作。Linux中有很多设备：`/dev/pts/[x]` 终端设备；`/dev/zero` 零设备；`/dev/null` NULL设备；`/dev/random` 随机数生成器等；不是所有的设备都有真正的实体，有可能只是一段代码的抽象。设备驱动程序是Linux内核中数量最庞大而且质量最低的代码(只有设备厂商知道设备驱动对通用API的翻译，Win和Linux都在不断试图把设备驱动从内核移到用户空间)。设备除开读/写还有数不清的控制功能都是ioctl系统调用实现的(比如多功能打印机，想想这个系统调用占据的代码量)。—— **OSTEP 36**

![[os2.jpg]]

以Linux文件系统为例，看设备驱动程序帮助OS设计和实现，应用(application)向一般块层(generic block layer)提出读/写块请求，经由正确的设备驱动程序，以隐藏特殊请求的细节；同样一些原始接口不经由文件系统(file system)执行读/写块操作，比如文件系统检查程序(file-system checker)，磁盘碎片整理(disk defragmentation)工具等。对比存储设备的抽象，终端是小数据量，直接流式传输(连续不间断像水流)；GPU是大数据量，是DMA方式传输。

## 总结

:memo:如何理解内核，shell，终端，操作系统，系统调用，libc，应用程序？

内核是应用程序和硬件的媒介。shell提供了用户和内核交互的接口以保护内核。终端是计算机的输入输出设备（Ctrl+C是中断信号）。操作系统是内核和一系列应用程序的组合，Linux操作系统主要使用汇编和C语言编写。系统调用是用户态进程主动切换到内核态的一种方式（软中断）。libc是计算和系统调用的封装；操作系统中的进程，输入输出对象（文件描述符）和功能函数（报错函数）等也都得到封装。C进一步可以封装C++的编译器，封装标准C++库发展C++；封装Python的解释器Cpython，封装标准Python库发展Python；当然不满足C也有人封装了Go。最后编程开发就是STFW,RTFM,RTFSC的事了。

:memo:如何理解操作系统中的C程序运行？

操作系统中的C程序是从Shell得到命令开始的，Shell解析命令是内置的还是外部的。如果是外部程序，使用操作系统的系统调用fork，execve帮助助创建进程。`系统调用是用户态进程主动切换到内核态的一种方式。` 操作系统内核中的加载器识别文件类型为动态链接文件后，做出必要的内存映射。先执行ld-linux-x86-64.so代码， 把动态库链接到地址空间中。`ld-linux-x86-64.so 负责动态链接库的加载，没有它就无法加载动态库像 libc。` 再执行_start函数，初始化 C 程序必须的环境。`crt*.o 等文件提供 C 程序运行所必须的环境等。` 最后才执行 main 函数。程序运行起来，如需进行输入输出等操作，则会使用特殊的指令发出系统调用请求操作系统执行。典型的例子是 printf 会调用 write 系统调用，向编号为 1 的文件描述符写入数据。

:memo:如何理解裸机(bare-metal)上的C程序(操作系统)运行?

裸机上的C程序是从CPU Reset后开始的，Firmware 先读取 MBR 中的 Boot loader，然后执行操作系统程序的_start函数(操作系统也是一个C程序)。操作系统运行起来，会创建第一个进程init，在此进程上创建出更多进程。综上，只要知道main函数之前(操作系统也是如此)初始化好了C程序环境并能够使用一些库函数足矣。

## 附录

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
