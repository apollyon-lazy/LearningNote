# 为自己的电脑安装双系统（Win10 + Linux）

1. 了解自己电脑的 BIOS 类型是不是 UEFI
2. 刻录 Ubuntu 镜像文件到一张空的U盘
3. 磁盘分区 分出足够空间给 Linux 系统
4. 安装 Ubuntu 并手动分区
网上分法不一，参考分区如下：

    | 目录 | 格式 | 建议大小 | 描述 |
    | :--- | :--- | :--- | :--- |
    | swap |  swap 逻辑分区 | 物理内存或物理内存的两倍（即本机RAM大小）| 交换空间相当于虚拟内存 |
    | /boot | 256M | ext4 逻辑分区 | Linux内核及其引导文件等 |
    | / | ext4 主分区 | 30%-50%的空间 | 相当于Windows下的C盘 |
    | /home | ext4 主分区 | 剩下所有空间 | 用户工作目录 |
5. 修正错乱的时间
Windows 下终端输入命令行：
`Reg add HKLM\SYSTEM\CurrentControlSet\Control\TimeZoneInformation /v RealTimeIsUniversal /t REG_DWORD /d 1`
Ubuntu 下终端输入命令行：
`timedatectl set-local-rtc 1 --adjust-system-clock`

光驱，光盘驱动器，是电脑读写光盘内容的机器。物理光驱有两个致命缺点，一个是读取速度慢，另一个是光驱寿命短。虚拟光驱是在计算机上通过软件模拟出一个光驱，它不是物理设备，无法放入光盘，也不能直接读取光盘，取而代之是加载存放在硬盘上的一个光盘镜像文件。像是一张游戏光盘放入物理光驱才能运行，虚拟光驱需要加入镜像文件才能使用。

## BIOS是什么？

BIOS是英文"Basic Input Output System"的缩略语，直译过来后中文名称就是"基本输入输出系统"。它的全称应该是ROM－BIOS，意思是只读存储器基本输入输出系统。

其实，它是一组固化到计算机内主板上一个ROM芯片上的程序，它保存着计算机最重要的基本输入输出的程序、系统设置信息、开机上电自检程序和系统启动自举程序。有人认为既然BIOS是"程序"，那它就应该是属于软件，感觉就像自己常用的Word或Excel。 但也很多人不这么认为，因为它与一般的软件还是有一些区别，而且它与硬件的联系也是相当地紧密。形象地说，BIOS应该是连接软件程序与硬件设备的一座"桥梁"，负责解决硬件的即时要求。主板上的BIOS芯片或许是主板上唯一贴有标签的芯片，一般它是一块32针的双列直插式的集成电路，上面印有"BIOS"字样。

## BIOS的作用?

BIOS的主要作用有以下几方面：

首先是自检及初始化程序:计算机电源接通后，系统将有一个对内部各个设备进行检查的过程，这是由一个通常称之为POST（Power On Self Test/上电自检）的程序来完成，这也是BIOS程序的一个功能。完整的自检包括了对CPU、640K基本内存、1M以上的扩展内存、ROM、主板、CMOS存贮器、串并口、显示卡、软硬盘子系统及键盘的测试。在自检过程中若发现问题，系统将给出提示信息或鸣笛警告。如果没有任何问题，完成自检后BIOS将按照系统CMOS设置中的启动顺序搜寻软、硬盘驱动器及CDROM、网络服务器等有效的启动驱动器，读入操作系统引导记录，然后将系统控制权交给引导记录，由引导记录完成系统的启动，你就可以放心地使用你的宝贝了。

其次是硬件中断处理：计算机开机的时候，BIOS会告诉CPU等硬件设备的中断号，当你操作时输入了使用某个硬件的命令后，它就会根据中断号使用相应的硬件来完成命令的工作，最后根据其中断号跳会原来的状态。再有就是程序服务请求：从BIOS的定义可以知道它总是和计算机的输入输出设备打交道，它通过最特定的数据端口发出指令，发送或接收各类外部设备的数据，从而实现软件应用程序对硬件的操作。

## .iso文件是？

ISO文件其实就是光盘的镜像文件，刻录软件可以直接把ISO文件刻录成可安装的系统光盘，ISO文件一般以iso为扩展名，其文件格式为iso9660。

英文全称Isolation，镜像文件的后缀名，通过特定的压缩方式，将大量的数据文件统一为一个后缀名为ISO的镜像文件，让后在将这些ISO镜像文件刻录到光盘中去，实际上ISO文件可以理解为从光盘中复制出来的数据文件，所以ISO镜像文件需要使用虚拟光驱才能打开，或者将ISO文件刻录到光盘中后，使用光驱来进行读取。

## 镜像文件是？

镜像文件是无法直接使用的，需要利用一些虚拟光驱工具进行解压后才能使用。虚拟光驱的原理跟物理光驱一样，比如说你买了一张游戏光盘，那么把游戏光盘加入物理光驱你就能顺利进行游戏，而虚拟光驱中需要加入的是镜像文件（iso文件，相当于游戏光盘），当你装载完虚拟光驱以后，你的电脑里面多了一个光驱，那就是虚拟光驱。接着载入镜像文件，以便完成游戏的安装，如果安装完以后那么就可以再载入它要求的镜像进入游戏。

## 虚拟光驱是？

虚拟光驱是一种模拟(CD-ROM)工作的工具软件，具有和计算机上所安装的光驱一样的功能。工作原理是先虚拟出一部或多部虚拟光驱，将光盘上的应用软件镜像存放在硬盘上，生成一个虚拟光驱的镜像文件，然后就可以将此镜像文件放入虚拟光驱中来使用。当以后要启动此应用程序时，不必将光盘放在光驱中，也就无需等待光驱的缓慢启动，只需要单击虚拟光驱盘符，虚拟光盘立即装入虚拟光驱中运行，快速又方便。
