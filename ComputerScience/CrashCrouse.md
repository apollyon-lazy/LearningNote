# Crash Crouse


[Crash Course Computer Science Github Chinese](https://github.com/1c7/Crash-Course-Computer-Science-Chinese)

| Concept | Translation |
| :--- | :--- |
| relay  | 继电器 |
| vacuum tube | 真空管 |
| transistor | 晶体管 |

| Concept | Translation |
| :--- | :--- |
| binary | 二进制 |
| Boolean algebro| 布尔代数 |
| NOT/AND/OR | 非/与/或 |
| XOR | 异或 |
| bit/byte | 位/字节 |

| Concept | Translation |
| :--- | :--- |
| integer |整数|
| floating point numbers| 浮点数(IEEE754) |
| ASCII | 美国信息交换标准代码 |
| Unicode | 统一码 |

|Concept | Translation |
| :--- | :--- |
| half adder | 半加器 |
| full adder | 全加器 |
| 8-bit ripple carry adder | 8位行波进位加法器 |
| overflow | 溢出 |
| carry-load-ahead adder | 超前进位加法器 |
| Arithmetic & Logic Unit | 算术逻辑单元(ALU) |

- 目前计算机中使用的加法器是超前进位加法器
- **ALU** 计算逻辑单元，计算机中负责运算的组件，处理数字/逻辑运算的最基本单元

|Concept | Translation |
| :--- | :--- |
| AND-OR latch | 与-或 锁存器 |
| gated latch | 门锁 |
| 8-bit register | 8位寄存器 |
| multiplexer | 多路复用器
| 16 x 16 latch matrix | 16x16门锁矩阵 |
| Random Access Memory | 随机存取存储器(RAM) |
| Central Processing Unit | 中央处理单元(CPU) |

- 锁存器的作用是存储一位数字
- 门锁的作用是用一根线控制数据的输入
- 寄存器的作用是并排使用门锁，储存多位数字
- **RAM** 随机存取存储器，由一系列矩阵以及电路组成的器件，可根据地址来写入、读取数据。

| Concept | Translation |
| :--- | :--- |
| instruction | 指令 |
| opcode+register/address in memory | 操作码+寄存器/内存地址 |
| instruction register | 指令寄存器 |
| instruction address register | 指令地址寄存器 |
| fetch/decode/execute | 读指令/解码/执行 |
| clock | 时钟 |
| clock speed | 时钟速度 |
| overlocking/underclocking | 超频/降频 |

- **CPU** 中央处理单元，负责执行程序。通常由寄存器/控制单元/ALU/时钟组成。与 RAM 配合，执行计算机程序。CPU 和 RAM 之间用“地址线”、“数据线”和“允许读/写线”进行通信。

|Concept | Translation |
| :--- | :--- |
| complexity-for-speed tradeoff | 复杂度速度权衡 |
| bus | 总线 |
| cathe | 缓存 |
| cathe hit/cathe miss | 缓存命中 缓存未命中 |
| dirty bit | 脏位 |
| instruction pipelining | 指令流水线 |
| out-of-order execution | 乱序执行 |
| speculation execution | 推测执行 |
| pipelined superscalar CPU | 流水线超量CPU |
| multi-core processors | 多核处理器 |
| multiple independent CPUs | 多独立CPU |
| Von Neumann Architecture | 冯诺依曼结构 |

- **缓存** 为了不让 CPU 空等数据（从 RAM 到 CPU 的数据传输有延迟），在 CPU 内部设置了一小块内存，称为缓存**
- **缓存命中** 想要的数据已经在缓存里 **缓存未命中** 想要的数据不在缓存里
- **脏位** 于检测缓存内的数据是否与 RAM 一致
- 高端CPU使用乱序执行解决**数据依赖性**问题，使用推测执行解决**跳转程序**的问题
- **冯诺依曼计算机**的标志是，一个处理器(有算术逻辑单元)+数据寄存器+指令寄存器+指令地址寄存器+内存

|Concept | Translation |
| :--- | :--- |
| pseudo-code | 伪代码 |
| assembler | 汇编器 |
| compiler | 编译器 |
| syntax | 语法 |
| assignments/ifs/loops | 赋值 条件 循环 |
| function | 函数 |
| library | 库 |

|Concept | Translation |
| :--- | :--- |
| algorithm | 算法 |
| sorting | 排序 |
| selection sort | 选择排序 O(n) |
| merge sort | 归并排序 O(n\*logn) |
| graph search | 图搜索 |
| dijkstra algorithm | 迪杰斯特拉算法 O(n^2)->O(n\*logn+1) |

| Concept | Translation |
| :--- | :--- |
| data structure | 数据结构 |
| array/list/vector | 数组 列表 矢量 |
| pointer/struct/node/linked list | 指针 结构体 节点 链表 |
| queue/stack | 队列 栈 |
| FIFO/LIFO | 先进先出 后进先出 |
| enqueue/dequeue | 入队 出队 |
| push/pop | 入栈 出栈 |
| tree/root/leaves/parent/children | 树 根节点 叶节点 父节点 子节点 |
| binary tree/graph | 二叉树 图 |

|Concept | Translation |
| :--- | :--- |
| Turing machine | 图灵机 |
| the halting problem | 终止问题 |
| Turing test | 图灵测试 |
| captcha | 验证码 |

- **图灵机** 只要有足够的规则，状态和纸带，图灵机可以解决一切计算问题。和图灵机一样完备，叫做图灵完备。
- **终止问题** 判断任意一个 程序 是否能在有限的时间之内结束运行的问题。证明图灵机不能解决所有问题。
- **图灵测试** 向人和机器同时发信息，收到的回答无法判断哪个是人，哪个是计算机，则计算机达到了智能程度。

|Concept | Translation |
| :--- | :--- |
| software engineering | 软件工程 |
| Object Oriented Programming | 面向对象编程(OOP) |
| Application Programming Interface | 程序编程接口(API) |
| Integrated Development Enviroment | 集成开发环境(IDE) |
| coding/debug | 编码 调试 |
| document(readme)/comment | 文档 注释 |
| source control/version control | 源代码管理 版本控制(svn. git.) |
| Quality Assurance testing | 质量保证测试(QA) |
| alpha version/beta version | 内部版本 外部版本 |

|Concept | Translation |
| :--- | :--- |
| Intergrated Circuits | 集成电路(IC) |
| printed circuit boards | 印制电路板(PCB) |
| photolithography | 光刻 |
| Moore's law | 摩尔定律(光的波长 量子隧穿效应) |
| very-large-scale integration| 超大规模集成软件(VLSI) |

|Concept | Translation |
| :--- | :--- |
| operation system | 操作系统(OS)|
| peripheral | 外设 |
| device driver | 设备驱动 |
| multitasking/virtual/protested memory | 多任务处理 虚拟内存 内存保护 |
| kernal | 内核 |

- **操作系统** 是电脑运行的第一个软件，是软件和硬件之间的媒介
- UNIX 把操作系统分成两个部分，一个是操作系统的核心部分，如内存管理，多任务和输入/输出处理，这叫做**内核**，第二部分是一堆有用的工具，比如程序和运行库。

|Concept | Translation |
| :--- | :--- |
| solid state drive/disk | 固态硬盘 |
| hard disk drive | 机械硬盘 |

| Abbr. | Capacity | Price | Velocity | Principle | Noise/Vibration/Recovery |
| :--- | :--- | :--- | :--- | :--- | :--- |
| SSD | small | high | fast | IC | small good hard |
| HHD | big | low | slow | electromagnetism | big bad easy |

| Concept | Translation |
| :--- | :--- |
| file format | 文件格式 |
| metadata/header | 元数据 文件头|
| flat file system | 平面文件系统 |
| directory file | 目录文件 |
| created/deleted/modified | 增 删 改 |
| fragmentation | 碎片 |
| hierarchical file system | 分层文件系统 |
| root directory | 根目录 |

- **目录文件** 泛指储存文件信息的文件
- **根目录** 是相对子目录而言的最顶层目录文件，例如安装软件选择的目录是软件运行根目录
- 增删改会引起文件的碎片化，移动仅改变目录文件的记录，因此存在恢复数据的可能

|Concept | Translation |
| :--- | :--- |
| compression | 压缩 |
| Run-length encoding | 游程编码 |
| dictionary coders | 字典编码 |
| lossless compression | 无损压缩 |
| perceptual coding | 感知编码 |
| lossy compression | 有损压缩 |

|Concept | Translation |
| :--- | :--- |
| QWERTY | 键盘布局 |
| commond line interface | 命令行界面 |
| terminal | 终端 |

|Concept | Translation |
| :--- | :--- |
| cathhode ray tube | 阴极射线管(CRT) |
| vector scaning | 矢量扫描 |
| raster scaning | 光栅扫描 |
| liquid crystal displays | 液晶显示屏(LCD) |
| pixel | 像素 |
| chracter generator | 字符生成器 |
| screen buffer | 屏幕缓冲区 |

- **字符生成器** 相比于像素，为了减少内存，人们更喜欢使用字符，计算机需要额外硬件，来从内存读取字符，转换成光栅图形 这样才能显示到屏幕上个硬件叫 "字符生成器"，基本算是第一代显卡。它内部有一小块只读存储器，简称 ROM，存着每个字符的图形，叫"点阵图案"
- **屏幕缓冲区** 为了显示，"字符生成器" 会访问内存中一块特殊区域 这块区域专为图形保留，叫 屏幕缓冲区，程序想显示文字时，修改这块区域里的值就行。

|Concept | Translation |
| :--- | :--- |
| graphical user interface | 图形用户界面(GUI) |
| mouse | 鼠标 |
| desktop metaphor | 桌面隐喻 |
| windows icons menus pointer | WIMP界面 |
| button checkboxes sliders tabs | 按钮 打勾框 滑动条 标签页 |
| event-driven programming | 事件驱动编程 |
| cut copy paste | 剪切 复制 粘贴 |
| start/menu taskbar/Windows explorer file manager | 开始菜单 任务栏 文件管理器 |

|Concept | Translation |
| :--- | :--- |
| wireframe rendering | 线框渲染 |
| orthographic projection | 正交投影 |
| perspective projection | 透视投影 |
| polygons | 三角形(3D图形学) |
| mesh | 网格 |
| scanline rendering | 扫描线渲染 |
| antialiasing | 抗锯齿 |
| painter's algorithm | 画家算法 |
| Z-buffering | 深度缓冲算法 |
| Z-fighting | 闪烁效应 |
| back-face culling | 背面剔除 |
| flat shading | 平面着色 |
| Gouraud shading/Phong shading | 高洛德着色 冯氏着色 |
| textures | 纹理 |
| graphics processing unit | 图形处理单元(GPU) |

- **Z Fighting** 采用深度缓冲算法，哪个图形在前将会变化
- **back-face culling** 由于游戏角色的头部或地面，只能看到朝外的一面，所以为了节省处理时间，会忽略多边形背面，这很好,但有个bug是，如果进入模型内部往外看，头部和地面会消失

|Concept | Translation |
| :--- | :--- |
| sneakernet | 人力传递网络 |
| Local Area Networks | 局域网(LAN) |
| Ethernet | 以太网 |
| Media Access Control address | 媒体访问控制地址(MAC address) |
| Carrier Sense Multiple Access | 载波侦听多路访问(CSMA) |
| Exponential Backoff | 指数退避 |
| Collision Domain | 冲突域 |
| Network Switch | 网络交换机 |
| routing | 路由 |
| Circuit Switching | 电路交换 |
| Message Switching | 报文交换 |
| hop count | 跳数 |
| Hop Limit | 跳数限制 |
| Internet Protocol | 互联网协议（IP） |
| packets | 数据包 |
| Network routers | 路由器 |
| congestion control | 阻塞控制 |
| Packet Switching | 分组交换 |
| internet of things | 物联网 |

- **局域网（LAN）** 是计算机近距离构成的小型网络。以太网是经典的局域网
- **媒体访问控制地址（MAC）** 用于确认局域网和WiFi传输的对象
- **载波侦听多路访问（CMSA）** 是指多台电脑共享一个传输媒介。共享媒介又称载体（carrier），如WiFi的载体是空气，以太网的载体是电线。载体传输数据的速度叫带宽（bandwidth），
- **冲突域** 是指载体和其中的设备总称为，为了避免冲突，可以用交换器
- **报文交换** 报文的具体格式简称**IP**，每一个电脑都会有一个IP地址。当报文比较大的时候，会堵塞线路。解决方法是 将大报文分成很多小块，叫**数据包**，来进行运输，这叫**分组交换**。路由器会平衡与其他路由器之间的负载  以确保传输可以快速可靠，这叫**阻塞控制**

|Concept | Translation |
| :--- | :--- |
| Wide Area Network | 广域网(WAN) |
| Internet Service Provider | 互联网服务提供商(ISP) |
| backbone of the internet | 互联网主干 |
| User Datagram Protocol | 用户数据报协议(UDP) |
| port number | 端口号 |
| checksum | 校验和 |
| Transmission Control Protocol | 传输控制协议(TCP) TCP/IP |
| sequential numbers | 序列号 |
| acknowledgement | 确认码 |
| Domain Name System | 域名系统（DNS） |
| Message Switching | 报文交换 |
| Top Level Domains | 顶级域名（TLD）.com .gov |
| second level domains | 二级域名 google.com  |
| subdomains | 子域名 images.google.com |
| Physical Layer | "物理层" |
| Data link layer | "数据链路层" |
| Network Layer | "网络层" |
| Transport layer | "传输层" |
| Session Layer | "会话层" |
| Presentation Layer | "表示层" |
| Application Layer | "应用程序层" |
| the Open System Interconnection | 开放式系统互联通信参考模型（OSI） |

- **传输控制协议 TCP**
  - 控制发送的文件按顺序到达
  - 要求接收方确认无误后发送确认码（ACK），确认码的成功率和来回时间可以用来推测网络的拥堵程度，TCP可以根据这个调整传输率。由于这个特点，TCP对时间要求高的程序不适用。
- **开放式系统互联通信参考模型（OSI）**
  - **物理层** 线路里的电信号，以及无线网络里的无线信号
  - **数据链路层** MAC,碰撞检测，指数退避和其他底层协议
  - **网络层** 各种报文转换和路由
  - **传输层** UDP,TCP等协议
  - **会话层** 用UDP,TCP创造连接，传递信息，然后关闭连接

|Concept | Translation |
| :--- | :--- |
| World Wide Web | 万维网(WWW) |
| hypertext | 超文本 |
| hyperlinks | 超链接 |
| web browsers | 网页浏览器 |
| Uniform Resource Locator | 统一资源定位器（URL） |
| DNS lookup | DNS查找 |
| web server | 网页服务器 |
| Hypertext Transfer Protocol | 超文本传输协议（HTTP） |
| GET request | GET请求 |
| status codes | 状态码 200. 404. |
| Hypertext Markup Language | 超文本标记语言（HTML) |
| Cascading Style Sheets| 层叠样式表(CSS) |
| search engines | 搜索引擎|
| web crawler | 爬虫  |
| ever enlarging index | 搜索算法 |
| backlinks | 反向链接 |
| Net Neutrality | 网络中立性 |
| Throttled | 节流 |

- 当访问一个网站时，计算机会先做DNS查找。
- 查找到IP后，用TCP连接到这个IP，网页服务器的标准端口是80。
- 连接到服务器后，发送HTTP标准中的GET指令，以获取HTML(CSS,JavaScript)书写的网页源码，并返回状态码(200：成功获取；400-499：客户端出错)
- 最后网页浏览器会把源码渲染成页面，页面是万维网的最基本单位。

|Concept | Translation |
| :--- | :--- |
| secrecy integrity availability | 保密性 完整性 可用性 |
| threat model | 威胁模型分析 |
| authentication | 身份认证 |
| Access Control | 访问控制 |
| Permissions/Access Control Lists  | 权限/访问控制列表 |
| Read write execute | 读、写、执行(权限) |
| Bell-LaPadula model |Bell-LaPadula 模型(访问控制模型)<br>"不能向上读，不能向下写"  |
| Chinese Wall model/Biba model | 中国墙模型/比伯模型 |
| security kernel/trusted computing base | 安全内核/可信计算基础<br>一组尽可能少的操作系统软件 |
| Independent Verification and Validation | 独立安全检查和质量验证 |
| isolation | 隔离|
| "sandbox" applications | 沙盒程序  |
| Virtual Machines | 虚拟机 |

|Concept | Translation |
| :--- | :--- |
| White Hats/Black Hats | 白客/黑客 |
| Phishing | 钓鱼 |
| Pretexting | 假托 |
| Trojan Horses/malware | 木马/恶意软件 |
| ransomware | 勒索软件 |
| Exploit  | 漏洞利用 |
| Buffer Overflow | 缓冲区溢出  |
| Bounds Checking/canaries | 边界检查/金丝雀<br>（应对缓冲溢出） |
| Code Injection | 代码注入 |
| Zero Day Vulnerability | 零日漏洞<br>软件制造者不知道有新漏洞被发现|
| Worms | 计算机蠕虫 |
| Botnet | 僵尸网络 |
| Distributed Denial of Service | 拒绝服务攻击(DDoS)|

| Concept | Translation |
| :--- | :--- |
| Cryptography | 密码学 |
| encryption decryption | 加密 解密 |
| cipher | 加密算法 |
| dubstitution cipher | 替换加密 |
| permutation cipher | 移位加密 |
| symmetric encryption | 对称加密<br>双方用一样的密钥加密和解密信息 |
| key exchange | 密钥交换<br>只有具备双方私钥和公钥一起才能解密 |
| asymmetric encryption | 非对称加密<br>两个密钥，一个公开一个私有，一个加密一个解密 |

| Concept | Translation |
| :--- | :--- |
| machine learning | 机器学习 |
| classification | 分类 |
| classifier | 分类器 |
| feature | 特征 |
| laber | 标签 |
| decision boundaries | 决策边界 |
| confusion matrix | 混淆矩阵 |
| decision tree | 决策树 |
| support vector machines | 支持向量机 |
| artifical neural networks | 人工神经网络  |
| deep learning | 深度学习 |
| reinforcement learning | 强化学习 |
| weak AI/Narrow AI | 弱AI/窄AI |
| strong AI | 强AI |

| Concept | Translation |
| :--- | :--- |
| computer vision | 计算机视觉 |
| kernel/filter | 核/过滤器 |
| Prewitt operators | Prewitt算子(水平垂直边沿检测) |
| convolutional neural networks | 卷积神经网络 |
| emotion recognition algorithms | 情感识别算法 |

| Concept | Translation |
| :--- | :--- |
| Speech recognition | 语音识别 |
| Fast Fourier Transform | 快速傅立叶变换 |
| Phonemes | 音素(构成单词的声音片段) |
| Speech Synthesis | 语音合成 |

- 通过词性(Parts of speech)和短语结构规则(Phrase structure rules)构建分析树(Parse tree)，并结合语言模型(Language Model)来实现语音识别(Speech recognition)

| Concept | Translation |
| :--- | :--- |
| Computer Numerical Control | 数控机器(CNC) |
| negative feedback loop | 负反馈回路 |
| Proportional–Integral–Derivative controller | PID 控制器 |
| Three Laws of Robotics | 机器人三定律 |

| Concept | Translation |
| :--- | :--- |
| Usability | 易用度 |
| affordances | 直观功能<br>平板用来推，按钮用来按 |
| recognition vs recall | 认知和回想<br>填空题比选择题难 |
| computer-mediated communication | 以计算机为媒介沟通(CMC) |
| augmented gaze | 增强凝视<br>软件修正注视位 |
| uncanny valley | 恐怖谷<br>机器人在几乎像人类和是真的人类之间的曲线 |
| Human-Robot Interaction | 人机交互（HRI） |
