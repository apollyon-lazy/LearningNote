# 计算机网络 自顶向下

## 参考笔记

[计算机网络笔记-第一章-概述 - 欢迎来到我的博客~ (crwei996.github.io)](https://crwei996.github.io/2022/09/23/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C%E7%AC%94%E8%AE%B0-%E7%AC%AC%E4%B8%80%E7%AB%A0/)
[计算机网络（自顶向下方法）学习笔记_计算机网络自顶向下方法_头秃的程序员小王的博客-CSDN博客](https://blog.csdn.net/qq_39326472/article/details/88089747)
[计算机网络（自顶向下方法）读书笔记----吐血整理_wx60dc8ce39e154的技术博客_51CTO博客](https://blog.51cto.com/u_15290941/3277160)


## 计算机网络和互联网

### 什么是网络

**网络(network)** 是由边和节点组成的与大小形状无关的拓扑。**计算机网络(computer network)** 是联网的计算机构成的系统。**互联网(因特网，Internet)** 是由以TCP/IP为主的一簇协议支撑的网络。

从具体构成角度看，互联网的节点是 **主机/端系统(host/end system)** 和 **分组交换机(packet switch)** ，边是**通信链路(communication link)**。分组交换机两种重要的类型是工作在网络层(Network Layer)的 **路由器(router)** 和工作在链路层(Data link layer)的 **链路层交换机(link-layer switch)** 。

**协议(protocal)** 是对等层的实体在通信的过程中应该遵循的规则的集合，遵守同一协议的实体才能通信。**TCP(Transmission Control Protocol, 传输控制协议)** 和 **IP(Internet Protocol, 网际协议)** 是互联网中两个重要的协议。互联网标准(Internet standard)是以请求评论(Request for comments, RFC)的文档形式，在互联网工程任务组(Internet Engineering task Force, IETF)的网站上发布的。

从应用程序提供服务的基础设施的角度看，互联网包括 **分布式应用进程(distributed application)** 和向进程提供通信服务的基础设施。

### 网络边缘

互联网网络边缘是端系统，接入网是将端系统物理连接到其 **边缘路由器(edge router)** 的网络，边缘路由器是端系统到任何其他远程端系统的路径上的第一台路由器，网络核心是分组交换机和链路组成的网状网络。

应用进程之间通信的两种模式，**客户/服务器(client/sever)模式** (如Web浏览器/服务器)，**对等(peer-to-peer, P2P)模式** (迅雷首创的下载技术P2SP通过检索数据库把服务器资源和P2P资源整合到了一起)。

`思考：百度网盘为什么没有搜索功能(公开性问题)？我们上传网盘的资源最后去了哪里(云服务器)？网盘是如何搜索违禁资源的(哈希值，违禁词检测，AI扫描等)？P2P模式应用在了哪里？`

### 网络核心

通过网络链路和交换机移动数据有两种基本方法：**电路交换(circuit switching)** 和 **分组交换(packet switching)**。电路交换在两台主机要通信时，网络会在两台主机之间创建一条专用的 **端到端连接(end-to-end connection)**。电路交换通过 **频分复用(Frequency-Division Multiplexing, FDM)** 或 **时分复用(Time-Division Multiplexing, TDM)** 来实现的。分组交换在端系统间交换 **报文(message)**，长报文会划分为小的数据块，称为 **分组(packet)**。分组交换机在链路输入端使用 **存储转发传输(store-and-forward transimission)** 机制；每条相连的链路分组交换机具有一个 **输出缓存/输出队列(output buffer, output queue)**，用于存储路由器准备发往那条链路的分组。除了存储转发时延外，分组还要承受输出缓存的 **排队时延(queuing delay)**。因为缓存空间大小是有限的，分组到达缓存可能是没有空间的，这种情况下将出现 **分组丢失(包)(packet loss)**。分组交换按需分配链路使用，用可变长的排队时延和有可能出现的分组丢失的代价，获取了共享性。分组交换是一种统计多路复用，同样的网络资源下，允许更多用户使用网络！

`思考：路由(决定分组采用的源到目标的路径(路由算法))帮助转发(将分组从路由器的输入链路转移到输出链路(路由表))是如何配合的？那分组交换中如何实现类似电路交换的服务(多媒体的专用线路)？分组交换中虚电路(virtual circuit)和数据报(datagram)的方式区别在于(是否建立连接)？`

### 接入网和物理媒体

**因特网服务供应商(Internet Service Provider，ISP)** 起初利用已有的线路资源为住宅接入互联网，使用 **调制解调器(Modem，猫)** 将上网数据通过电话线传输(数据波形形似冲浪)，这种拨号上网的方式缺点是带宽窄，而且上网和打电话不能同时进行。 后来单根 **数字用户线(Digital Subscriber Line，DSL)** 线路按照不同频率编码分为电路呼叫和供互联网连接的上行和下行通道(FDM)，上行和下行带宽不对称叫做 **非对称数字用户线(Asymmetric Digital Subscriber Line，ADSL)**。除了DSL(电话公司)，住宅接入网络的形式还有电缆接入(有线电视公司)，**光纤到户(Fiber To The Home，FTTH)** 和 卫星链路。

计算机网络按照网络覆盖范围分为 **局域网(Local Area Network，LAN)** 和 **广域网(Wide Area Network)** 。企业(和家庭)接入使用LAN将端系统连接到边缘路由器，有线LAN技术 **以太网(Ethernet)** 或者 **WLAN(Wireless Local Area Nrtwork)** 技术 **Wifi (Wireless Fidelity)** 。无线接入还有广域无线接入(4G，5G等)。

传输信号的物理媒体分为 **导引型媒体(guided media)** 和 **非导引型媒体(unguided media)** 。导引型媒体，电波沿着固体媒体前行，如光缆、双绞铜线(电话网络)或同轴电缆(有线电视网络)；非导引型媒体，电波在空气或外层空间中传播，如无线局域网、无线广域网或卫星链路。

`思考：目前生活中用到的几种网络技术分类(插网线连接校园网属于有线LAN技术，手机流量上网属于无限WAN技术)？猫的背后有一个WAN和多个LAN口(供应商网线连WAN口，电脑网线连LAN口)？，通信中常用两种卫星，同步卫星(geostationary satellite)(始终在地球上方相同点，延迟高)和近地卫星(Low-Earth Orbiting, LEO)(马斯克的星链计划)？`

### Internet结构和ISP

![[net1.jpg]]
今天的互联网是一个网络的网络。较低层的ISP与较高层的ISP相连(涉及费用结算)，较高层的ISP彼此互联(不涉及费用结算)。除了第一层的ISP可以选择 **多宿(multi-home)** 即可以与两个或更多供应商ISP连接。第三方公司也会创建 **因特网交换点(Internet Exchange Point，IXP)** 帮助同一层ISP互联。**互联网内容提供商(INternet Content Provider，ICP)** 有些也会建立自己的专有网络(如谷歌分布全球的数据中心)，同时与各级互联。

`思考：数据中心通常离 ISP 很近，但有些建在海底和北极，为什么(省电)？`

### 分组延时、丢失和吞吐量

分组在沿途的每个节点经受几种不同的时延，包括 **节点处理时延(nodal processing delay)**，**排队时延(queuing delay)**，**传输时延(transmission delay)** 和 **传播时延(propagation delay)**，这些时延总体累加起来是 **节点时延(total nodal delay)**。令 $a$ 表示分组到达队列的平均速率(分组/秒，pks/s)，$R$是从队列中推出比特的速率(bps)，简单起见假定所有分组都是$L$比特组成的，则比特到达队列的平均速率是 $La$ bps，假定队列非常大能容纳无限量的比特，比率 $La/R$ 称为 **流量强度(traffic intensity)** (好比马路上容纳的车达到了它的容纳量就会发生堵车)。在流量工程中，设计系统时流量强度不能大于1。因为排队容量是有限的，随着流量强度接近1，排队时延并不会真正趋向无穷大，当到达的分组发现队列已满，路由器将丢弃(drop)该分组，分组将丢失(lost)。常用于网络诊断的 ping 和traceroute 命令是基于 **ICMP(Internet Control Message Protocol，互联网控制消息协议)** 实现的，是互联网协议族中重要的协议之一。吞吐量是源端和目标端之间传输的速率(数据量/单位时间)，有 **瞬时吞吐量(instantaneous throughput)** 和 **平均吞吐量(average throughput)**。

### 协议层次及服务模型

将网络复杂的功能分成功能明确的层次，每一层实现一个或一组功能，功能中包括向上一层提供的 **服务(service)** 。**协议(protocol)** 的目的是为了向上层提供更好的服务，协议是通过层间的接口访问下层所提供的的服务实现的。服务又分为面向连接的服务(Connection-oriented Service)(比如打电话，比如虚电路)和无连接的服务(Connectionless Service)(比如寄信件，比如数据报)。

![[net2.jpg]]

下层(Layer n)是 **服务用户(service user)**，上层(Layer n+1)是 **服务提供者(service provider)**，下层通过层间接口 **SAP(Service Access Point，服务访问点)** 向上层提供服务，服务的形式叫做 **原语(primitve)**。上层的的 SDU 要穿过 SAP 前端要加 ICI 形成 IDU， 送到下层的 SDU 按照下层的协议在前端加入下层的 Header 后形成下层的 PDU，对等层实体的信息交换是以 PDU 的形式实现的。

互联网的 **协议栈(protocol stack)** 由5个层次组成：物理层、链路层、网络层、运输层和应用层。物理层把帧中的 **比特/位(byte/bit)** 通过物理媒体从一个节点移动到下一个节点；链路层在物理层提供的服务基础之上，在相邻的两个节点之间传输以 **帧(frame)** 为单位的数据(PPP，802.11(wifi)，Ethernet)；网络层在链路层提供的点到点的服务基础之上，实现以 **分组(packet)** 为单位的端到端的数据传输(IP，路由协议)；传输层在网络层提供的端到端的服务基础之上，实现进程到进程之间 **报文段(segment)** 的交互(TCP，UDP)；应用层在传输层提供的进程与进程间服务基础上，以 **报文(message)** 的形式为人类应用或者其他应用进程提供网络应用服务(FTP，SMTP，HTTP，DNS)。**开放式系统互连通信参考模型(Open System Interconnect，OSI)** 定义了网络互连的七层框架：物理层(Physical Layer)，数据链路层(Data link layer)，网络层(Network Layer)，运输层(Transport layer)，会话层(Session Layer)，表示层(Presentation Layer)，应用层(Application Layer)。

`思考：会话层和表示层在互联网协议栈中有体现么(有，在应用层面)？在路由器和链路层交换机要经过几层封装(encapsulation)和解封装(三层和两层)？位，帧，分组和报文属于是各层次的(PDU)？SDU的传输存在一对一，一对多，多对一的复杂情况是怎么处理的？`

### 历史

1961-1972：早期分组交换概念(ARPAnet)；1972-1980：专用网络和网络互联(Cerf and Kaha 定义了今天的互联网体系结构)；1980-1990：体系结构变化，网络数量激增，应用丰富；1990-2005：商业化，Web，新的应用(好的互联网公司沉淀下来)；2005-现在(移动终端，物联网，5G，云服务等)...

`思考：如何看待互联网行业马太效应赢者通吃(监管局介入)？`

## 应用层