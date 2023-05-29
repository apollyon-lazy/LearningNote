# 现代控制理论

[浙江大学 2020学年公开课 MOOC](https://www.bilibili.com/video/BV1T7411n7en?p=1&vd_source=1a6b23698d4fda944b87ec43a41c4c5f)

## 绪论

1. 经典控制理论 和 现代控制理论的差别？
   | | 经典控制理论 | 现代控制理论 |
   | :---: | :---: | :---: |
   | 理论基础 | 时域分析、根轨迹法、频域分析等 | 状态空间等 |
   | 数学工具 | 拉普拉斯变换等 | 线性代数、微分方程、泛函分析等 |
   | 研究对象 | 线性定常系统 | 多变量、非线性、时变、连续和离散 |
   | 特点 |只关心系统的输入与输出，不关心系统运行时的内部状态 | 不仅关注系统的输入与输出，也关心系统运行时的内部状态 |

## 控制系统的状态方程

1. 状态变量、状态向量、状态空间、状态轨迹、状态空间表达式
   - 状态变量是相互独立的，从数学上来看是线性无关的；
   - 对同一个动态系统，在描述内涵精度相同的情况下，状态变量的个数是唯一确定的，但是状态向量的选取可以有无穷多种；
   - 对于一个实际的物理系统，通常状态变量个数等于系统中独立储能元件的个数；
   - 对于 n 个状态变量、 r 个输入、m 个输出的动态系统、状态空间表达式的一般形式为：  
   $\dot x = Ax + Bu$  
   $y = Cx + Du$  
   $\mu$是输入，x是状态变量，y是输出  
   $A \in R^{nxn}$，表征了系统内部状态的联系，被称为**系统矩阵**  
   $B \in R^{nxr}$，表征了输入对状态的作用，称为**控制矩阵**  
   $C \in R^{mxn}$，表征了输出与状态变量的关系，称为**输出矩阵**  
   $C \in R^{mxr}$，表征了输出与输入的关系，称为**直接传输矩阵**  
2. 状态空间表达式的建立：**方框图法**、**机理法**、**实现问题**及其建模方法
   - 实现问题存在的条件是 m <= n  
   m 是传递函数分子的阶数，n 是传递函数分母的阶数
   当 m < n 时，输入输出之间不存在比例关系，直接传输矩阵 $D = 0$  
   当 m = n 时，输入输出之间存在比例关系，直接传输矩阵 $D \neq 0$  
   当 m > n 时，输出将含有输入信号的直接微分项，这在实际系统中是不被允许的  
   - 状态变量的选取
   方框图法：每一个积分器的输出选为状态变量  
   机理法：每一个独立储能元件，选一个变量作为状态变量  
   实现方法一：传递函数分母分之输入的拉氏反变换，及其各阶导数作为状态变量  
   实现方法二：系统输入。输出各阶导数的线性组合选作状态变量  
   `经典控制理论：拉式变换、传递函数、零点和极点`
3. 状态向量的非奇异线性变换、广义特征向量
   - 同一动态系统，描述系统动态过程的状态空间表达式有无穷多种，但反映系统本质特征的系统特征值是唯一的；
   - 同一动态系统，不同状态空间表达式之间，存在着一种非奇异线性变换关系；
   - 同一动态系统，不同状态空间表达式的系统矩阵是相似矩阵；
   - 不存在重根的系统，可变换为**对角规范型**，实现状态变量的完全解耦；
   - 存在重根的系统，**约当规范型**是可能达到的最简耦合形式。同一特征根，同一约当子块所对应的状态变量之间才存在耦合关系；
   `线性代数：特征矩阵、特征方程、特征多项式、特征值、特征向量、代数重数和几何重数、相似变换、可对角化、实对称矩阵、特征值分解`；
4. **传递函数矩阵**、由状态空间表达式导出传递函数矩阵、组合系统的状态空间表达式和传递函数矩阵：串联、并联、反馈
   - 对应于状态空间描述  
     $\dot x = Ax + Bu \quad x(0) = 0$  
     $y = Cx + Du$  
     其传递函数矩阵为：  
     $W(s) = C(sI - A)^{-1}B + D$  
   - 一个系统的状态空间表达式是非唯一的，但其传递函数矩阵是唯一的
5. 时间离散系统、线性时变系统、非线性系统状态空间的基本形式

## 控制系统状态方程组的解

1. 零输入响应、零状态响应、叠加原理、**矩阵指数函数**及其计算方法：根据定义直接计算、化为对角标准型和约当标准型、拉氏变换法、凯拉-哈迷尔顿定理
   - **线性定常系统齐次状态方程**  
   $\dot x = Ax,x(0)=x_0, \quad t \geq 0$
   的解，即系统的零输入响应 $x_{0u}(t)$ 为：  
   $x_{0u}(t) = e^{At}x_0,t \geq 0$，  
   式中， $e^{At}$ 为系统矩阵A的矩阵指数函数：  
   $e^{At} \triangleq I + At + \frac{1}{2!}A^2t^2 + ... = \sum_{k=0}^{\infty} \frac{1}{k!}A^kt^k $
   - **凯拉-哈迷尔顿定理**  
   设 $A \in R^{nxn}$，其特征多项式为  
   $D(\lambda) = |\lambda I - A| = \lambda^n + a_{n-1}\lambda^{n-1} + ... + a_1\lambda + a_0 = 0$，  
   则矩阵A必满足其特征多项式，即  
   $A^n + a_{n-1}A^{n-1} + ... + a_1A + a_0I = 0$
   - **线性定常系统非齐次状态方程**  
   给定初始状态为零的线性定常系统
   $\dot x = Ax + Bu,x(0)=x_0, \quad t \geq 0$  
   其中，x为n维状态向量，u为r维输入向量，A和B分别为nxn和nxr常阵  
   那么系统的零状态响应可表示为：
   $x_{0u}(t) = \int_{0}^t e^{A(t-\tau)Bu(\tau)}x_0, \quad t \geq 0$  
2. **状态转移矩阵**：分解性、可逆性、传递性、倍时性、微分性和交换性、唯一性
3. 线性定常系统和线性时变系统状态方程的解析表达式
   - $x(t) = \Phi(t-t_0)x(t_0) + \int_{t_0}^t \Phi(t- \tau)Bu(\tau)d\tau, \quad t \geq t_0$
   - $x(t) = \Phi(t,t_0)x(t_0) + \int_{t_0}^t \Phi(t- \tau)B(\tau)u(\tau)d\tau, \quad t \in [t_0,t_\alpha]$

## 线性控制和系统的能控性和能观性

1. 能控、完全能控、不完全能控、线性定常系统的能控性的判别
   - **Gram（格拉姆）矩阵判据**  
   线性定常系统： $\dot x = Ax + Bu,x(0) = x_0, \quad t \geq 0$  
   是完全能控的充分必要条件为  
   存在时刻 $t_1 > 0$使如下定义的Gram矩阵  
   $W_c[0,t_1]=\int_0^{t_1}(e^{-At}B)(e^{-At}B)^Tdt$ 为非奇异
   - **秩判据**
   线性定常系统完全能控的充要条件是  
   秩判别矩阵 $M=[B\ AB\ ...\ A^{n-1}B]$ 的秩 $rankM = n$  
   其中，n为系统矩阵A的维数
   - **PBH判据**  
   线性定常系统完全能控的充要条件是  
   对系统矩阵的所有特征值 $\lambda_i(i=1,2,...n)$:均成立：  
   $rank[\lambda_iI-A,B]=n, \quad i=1,2,...,n$
   - **规范型判据**  
   线性定常系统完全能控的充要条件为：  
     1. 当系统矩阵A的特征值为两两互异时，系统状态方程经线性变换导出的对角规范型：(公式难显示，略)

      式中， $\bar B_i \neq 0,i=1,2,...,n$ ,即控制矩阵中不包含元素全为零的行
     2. 当系统矩阵A的特征值存在重根时，系统状态方程经线性变换导出的约当标准型：(公式难显示，略)

      设特征根 $\lambda_i$的代数重数为 $\sigma_i$。几何重数为 $\alpha_i$， $\lambda_i$对应的第k个约当子块的维数为 $r_{ik}$  
         - 若 $\sigma_i = 1$，则 $\lambda_i$对应的输入矩阵 $\tilde B_i$ 不全为0；
         - 若 $\sigma_i > 1,\alpha_i = 1$，则 $\lambda_i$对应的输入矩阵$\tilde B_i$的最后一行不全为0；
         - 若 $\alpha_i > 1$，则 $\lambda_i$对应的每一个约当子块最后一行对应的输入矩阵行组成的矩阵 $[\bar b_{r_{i1}}\ \bar b_{r_{i2}}\  \cdots  \bar b_{r_{i\alpha_i}} ]^T$ 均为行线性无关。
2. 能观、完全能观、不完全能观、线性定常系统的能观性的判别
   - Gram（格拉姆）判据
   - 秩判据
   - PBH秩判据
   - 规范型判据
3. 线性时变系统的能控性和能观性的判别
   - Gram（格拉姆）判据
   - 秩判据
   - Gram（格拉姆）判据
   - 秩判据
4. 线性时变对偶系统、线性定常对偶系统、线性时变系统对偶原理、线性定常系统对偶原理
5. 能控标准I型、能控标准II型、能观标准I型、能观标准II型
   - 能控性与能观性的不变性  
   在任意非奇异线性变换下，线性定常系统  
   $\dot x = Ax + Bu\ y = Cx$
   的能控性和能观性不变
   - **能控标准I型**变换
   对于完全能控的单输入单输出线性定常系统，存在线性非奇异变换 $x = T_{C1}\bar x$，其中：(公式难显示，略)。$a_i(i=0,1,...,n-1)$ 为系统特征多项式 $|\lambda I-A|= \lambda^n + a_{n-1}\lambda^{n-1} + ... + a_1\lambda +a_0 = 0$的系数。能够使状态空间表达式化成如下形式的能控标准型（I型）：(公式难显示，略) $\dot {\bar x} = \bar A \bar x + \bar b \bar u  \ \bar y = \bar C \bar x$  

6. 线性定常系统的能控性分解、能观性分解

## 李雅普诺夫定理

1. 平衡状态、孤立的平衡状态、李雅普诺夫意义下的稳定、一致稳定、渐进稳定、大范围渐进稳定、李雅普诺夫意义下的不稳定、李雅普诺夫第一法：外部稳定（输出稳定）、内部稳定（状态稳定）
   - 系统的稳定性是相对系统的平衡状态而言的
   - 李雅普诺夫意义下的渐进稳定等于工程意义下的稳定
   - 线性系统的李亚普诺夫主判据、辅助判据，不稳定判据均是充分条件；线性系统的李雅普诺夫方程判据是充要条件
   - 构建李雅普诺夫函数没有统一的方法，雅可比矩阵法和变量梯度法也只适用于一些特定的系统
2. 李雅普诺夫第二法
   - 李雅普诺夫稳定性主判据：  
   设系统的状态方程为： $\dot x = f(s)$  
   若存在一个具有连续一阶导数的标量函数 $V(x)$且满足  
      1. $V(x)$是正定的；
      2. $\dot V(x)$是负定的；
   则系统在平衡状态 $x_e = 0$ 是渐进稳定的。
      3. 除满足条件(1)(2)外，若 $||x||\rightarrow \infty$，则系统在平衡状态 $x_e = 0$ 是大范围渐进稳定的
   - 李雅普诺夫稳定性辅助判据
   - 李亚普诺夫不稳定性判据
3. 李雅普诺夫在线性系统中的应用、李雅普诺夫在非线性系统中的应用：雅克比矩阵法（克拉索夫斯基法）、变量梯度法
   - 线性定常系统的渐进稳定性判据
   对于给定的没有外界输入的线性定常系统 $\bar x = Ax,x(0) = x_0,t \geq 0$  
   在平衡状态 $x_e = 0$渐进稳定的充要条件为：对于任意给定的一个实正定对称矩阵Q，必存在唯一的实正定对称矩阵P，满足如下李亚普诺夫方程：$$A^TP + PA = -Q$$
   - 线性时变系统的渐进稳定性判据
   - 雅克比矩阵法（克拉索夫斯基法）
   - 变量梯度法
`线性代数：标量函数、正定、半正定、负定、半负定、不定、二次型函数、主子行列式`

## 线性定常系统的综合

1. 系统的综合、状态反馈控制、输出反馈控制、极点配置问题、镇定问题、解耦问题、跟踪问题
   - 闭环系统的能控与能观性
   状态反馈不改变系统的能控性，但可能改变系统的能观性  
   输出反馈不改变系统的能控性和能观性
2. 状态反馈的极点配置问题、状态反馈极点可配置的条件、单输入单输出系统状态反馈极点配置的两种算法、输出反馈的极点配置问题
3. 状态反馈的镇定问题、状态反馈可镇定的条件、状态反馈镇定的算法
`经典控制理论：稳定性、线性定常系统稳定的充要条件、劳斯稳定判据、系统误差、稳态误差（先判定稳定）、三种典型输入（阶跃、斜坡、加速度）对于三种典型系统（0型、I型、II型）的稳态误差`

## 思考

- [x] ~~控制理论的内容晦涩，结合题目示例理解会更加透彻~~
  - [x] 晦涩表明还是没有理解透彻，带有实例的讲解视频会更容易理解 
- [x] ~~Github markdown 涉及矩阵公式无法显示 建议使用图片~~
  - [x] Markdown原生不支持图片，建议有公式的笔记还是手写合适(纸质拍照PDF)
- [x] 2020-9-6 16:40