# 0 环境配置
环境中需要的包：  
- numpy pandas matplotlib(数据处理三剑客)   
- scipy(科学计算)  
- openpyxl(读取excel)   
- control slycot (与控制相关的包)

# 1 符号和定义

## 1.1 符号

$$\begin{array}{ll}
a & \text { 发动机模型参数, [-] } \\
b & \text { 翼展, [m] } \\
b & \text { 发动机模型参数, [-] } \\
\bar c & \text { 平均空气动力弦长, [m] } \\
g & \text { 重力加速度, [$m \cdot s^{-2}$] } \\
h & \text { 压力高度, [m] } \\
m & \text { 飞机质量, [$kg$] } \\
n & \text { 发动机转速, [$rpm$] } \\
P & \text { 发动机功率, [$N \cdot m / s$] } \\
p_z & \text { 发动机管道压力, [''Hg]} \\
S & \text { 机翼面积, [$m^2$] } \\
t & \text { 时间, [s] } \\
T & \text { 大气温度, [K]} \\
V & \text { 真实空速, [$m \cdot s^{-1}$]} \\
W & \text { 飞机重力, [N] } \\
\end{array}$$

$$\begin{array}{ll}
C_l，C_m，C_n & \text { 绕$X_B$，$Y_B$，$Z_B$轴力矩的无量纲力矩系数, [-] } \\
C_X，C_Y，C_Z & \text { 沿$X_B$，$Y_B$，$Z_B$轴力的无量纲力系数, [-] } \\
F_B，F_E，F_S & \text { 机体坐标系，地面坐标系，稳定坐标系 } \\
F_x, F_y, F_z & \text { 沿$X_B$，$Y_B$，$Z_B$方向的总力, [$N$] } \\
I_x，I_y，I_z & \text { 沿$X_B$，$Y_B$，$Z_B$方向的惯性矩, [$kg \cdot m^{2}$] } \\
J_{xy}，J_{xz}，J_{yz} & \text { 在$X_B-Y_B$，$X_B-Z_B$，$Y_B-Z_B$平面的惯性积, [$kg \cdot m^{2}$] } \\
L，M，N & \text { 总滚转力矩，总俯仰力矩，总偏航力矩, [$N \cdot m$] } \\
L_{a}，M_{a}，N_{a} & \text { 气动滚转力矩，气动俯仰力矩，气动偏航力矩, [$N \cdot m$] } \\
L_{t}，M_{t}，N_{t} & \text { 由发动机操作产生的滚转力矩，俯仰力矩，偏航力矩, [$N \cdot m$] } \\
p，q，r & \text { 滚转角速度，俯仰角速度，偏航角速度, [$rad \cdot s^{-1}$] } \\
P_{l}, P_{m}, P_{n}, P_{p p}, P_{p q}, P_{p r}, P_{q q}, P_{q r}, P_{r r} & \text { 滚转角速度(p)方程中使用的惯性参数 }\\
Q_{l}, Q_{m}, Q_{n}, Q_{p p}, Q_{p q}, Q_{p r}, Q_{q q}, Q_{q r}, Q_{r r} & \text { 俯仰角速度(q)方程中使用的惯性参数 }\\
R_{l}, R_{m}, R_{n}, R_{p p}, R_{p q}, R_{p r}, R_{q q}, R_{q r}, R_{r r} & \text { 偏航角速度(r)方程中使用的惯性参数 }\\
u，v，w & \text { 真实速度沿$X_B$，$Y_B$，$Z_B$的分量, [$m \cdot s^{-1}$]} \\
X_{e}，Y_{e}，Z_{e} & \text { 飞机沿$X_B$，$Y_B$，$Z_B$(高度)方向的位移, [$m$]} \\
X_{a}，Y_{a}，Z_{a} & \text { 气动力沿$X_B$，$Y_B$，$Z_B$方向的分量, [$N$]} \\
X_{t}，Y_{t}，Z_{t} & \text { 由于发动机操作产生的力沿$X_B$，$Y_B$，$Z_B$方向的分量, [$N$]} \\ 
X_{gr}，Y_{gr}，Z_{gr} & \text { 重力沿$X_B$，$Y_B$，$Z_B$方向的分量, [$N$]} 
\end{array}$$

$$\begin{array}{ll}
\alpha, \beta, \gamma & \text { 攻角，侧滑角，航迹角 [rad] } \\
\theta, \varphi, \psi & \text { 俯仰角，滚转角，偏航角 [rad] } \\
\delta_a, \delta_e, \delta_f, \delta_r & \text { 副翼，升降舵，襟翼，方向舵的偏转角 [rad] } \\
\end{array}$$


## 1.2 坐标系

这里我们引入三个坐标系，分别是机体坐标系，稳定坐标系以及地面坐标系。

**机体坐标系**

机体坐标系 $F_B$ 是一个右手正交坐标系 $O_BX_BY_BZ_B$ （见图 0.2）。坐标系的原点 $O_B$ 位于飞机的重心位置。$X_BO_BZ_B$ 平面与飞机的对称面重合。$X_B$ 轴正方向指向机头前方，$Y_B$ 轴正方向指向飞机右侧。

**稳定坐标系**

稳定坐标系 $F_S$ 是一个特殊的机体坐标系，常用在给定的标准飞行条件下，研究小扰动对飞机的影响。坐标系 $F_S$ 和 $F_B$ 的区别在于 $X_S$ 的方向。在对称标准飞行条件下，$X_S$ 的方向平行于真实空速 $V$。在非对称标准飞行条件下，$X_S$ 的方向平行于真实空速 $V$ 在飞机对称面的投影。

**地面坐标系**

地面坐标系 $F_E$ 是一个右手正交坐标系 $O_EX_EY_EZ_E$。原点的位置原则上是可以设置在任意的位置，但经常我们取飞机飞行测试开始的重心位置。$X_E$ 垂直向下，方向平行于当地重力加速度。 $S_E$指向北方，$Y_E$指向东方。

![[p1.jpg]]

<center>图1.1：测量坐标系和机体坐标系</center>

# 2 海狸飞机的动力学模型

## 2.1 引言
这一章节将给出用 Python 代码写好的海狸飞机动力学模型。海狸飞机的动力学模型包括飞机运动模型，力与力矩模型，修正模型，大气模型。飞机的运动方程是普遍的，但力和力矩模型依赖于飞机本身的特性。

## 2.2 飞机的运动模型
我们可以用一组微分方程（ODEs）来表示飞机的运动。飞机的运动与外部所受到的力和力矩有关，力和力矩根据产生情况可以分为几类。这里只考虑气动，发动机，重力，非稳定大气的贡献。在这一节，将给出飞机的运动方程，以及计算不同力和力矩的关系式。

### 2.2.1 一般的非线性运动方程
非线性运动方程一共12个，6个方程涉及力和力矩，6个方程确定飞机姿态和位置。有关飞机平动的方程是用飞机的真实空速 $V$，攻角 $\alpha$，侧滑角 $\beta$ 来表示的，也有使用真实空速在机体坐标系下的分量 $u$，$v$，$w$ 来表示的。这些方程仅仅在以下假设成立时有效：

1. 考虑的飞机在整个过程中视为刚体；
2. 飞机的重量不会随仿真时间的变化而改变，即始终是恒定的常数；
3. 地球在空间中是固定不变的，即忽略地球的自转影响；
4. 地球的曲率是忽略的，即平整地球假设。

计算真实空速、攻角，和侧滑角的微分方程：  

$$\begin{array}{l}
\dot{V} = \frac{1}{m} \left[ F_{x} \cos \alpha \cos \beta + F_{y} \sin \beta + F_{z} \sin \alpha \cos \beta\right]\\
\dot{\alpha} = \frac{1}{m \cdot V \cos \beta} \left[ -F_{x} \sin \alpha + F_{z} \cos \alpha\right]+q-(p \cos \alpha+r \sin \alpha) \tan \beta\\
\dot{\beta}=\frac{1}{m \cdot V} \left[- F_{x} \cos \alpha \sin \beta + F_{y} \cos \beta - F_{z} \sin \alpha \sin \beta \right]+P \sin \alpha-R \cos \alpha
\end{array}$$

计算体坐标系下旋转角速度的微分方程：

$$\begin{array}{l}
\dot{p} = P_{p q} \cdot p q  +P_{q r} \cdot q r  +P_{n} \cdot N +P_{l} \cdot L \\
\dot{q} = Q_{p p} \cdot p^{2}  +Q_{p r} \cdot p r  +Q_{r r} \cdot r^{2}  +Q_{m} \cdot M \\
\dot{r} = R_{p q} \cdot p q  +R_{q r} \cdot q r  +R_{n} \cdot N  +R_{l} \cdot L \\
\end{array}$$


$$\begin{array}{l}
P_{p q}=\frac{\left(I_{x}-I_{y}+I_{z}\right) \cdot J_{x z}}{I_{r r}}, P_{q r}=\frac{\left[\left(I_{y}-I_{z}\right) \cdot I_{z}-J_{x z}^{2}\right]}{I_{r r}}, P_{n}=\frac{J_{x z}}{I_{r r}}, P_{l}=\frac{I_{z}}{I_{r r}}, Q_{p p}=\frac{-J_{x z}}{I_{y}}, \\
Q_{p r}=\frac{\left(I_{z}-I_{x}\right)}{I_{y}}, Q_{r r}=\frac{J_{x z}}{I_{y}}, Q_{m}=\frac{1}{I_{y}}, R_{p q}=\frac{\left[\left(I_{x}-I_{y}\right) \cdot I_{x}+J_{x z}^{2}\right]}{I_{r r}}, R_{q r}=\frac{\left(I_{y}-I_{z}-I_{x}\right) \cdot J_{x z}}{I_{r r}}, \\
R_{n}=\frac{I_{x}}{I_{r r}}, R_{l}=\frac{J_{x z}}{I_{r r}} \text { and } I_{r r}=\left(I_{x} I_{z}-J_{x z}^{2}\right) .
\end{array}$$


计算欧拉角的微分方程:

$$\begin{array}{l}
\dot{\psi} = (q \sin \varphi + r \cos \varphi ) / cos \theta \\
\dot{\theta} = q \cos \varphi - r \sin \varphi \\
\dot{\varphi} = p  + q \sin \varphi \tan \theta  + r \cos \varphi \tan \theta \\
\end{array}$$



计算飞机位置的微分方程：

$$\begin{array}{l}
\dot{X}_{\mathrm{e}} = \{u \cos \theta + (v \sin \varphi+w \cos \varphi) \sin \theta\} \cos \psi 
-(v \cos \varphi-w \sin \varphi) \sin \psi \\
\dot{Y}_{\mathrm{e}} = \{u \cos \theta + (v \sin \varphi+w \cos \varphi) \sin \theta\} \sin \psi 
+(v \cos \varphi-w \sin \varphi) \cos \psi \\
\dot{Z}_{\mathrm{e}} = -u \sin \theta  + (v \sin \varphi + w \cos \varphi) \cos \theta
\end{array}$$

真实空速在机体坐标系的分量计算公式：

$$\begin{array}{l}
u = V \cdot \cos\alpha \cdot \cos\beta \\
v = V \cdot \sin\beta \\
w = V \cdot \sin\alpha \cdot \cos\beta \\
\end{array}$$

方程中也用到了海狸飞机的一些基本参数，涉及到的参数会在下表中给出（表2.1）。

***
$$\begin{array}{ll}
I_x & = 5368.39 kgm^2 \\
I_y & = 6928.93 kgm^2 \\
I_z & = 11158.75 kgm^2 \\
J_{xz} & = 117.64 kgm^2 \\
m & = 2288.231 kg  \\
\end{array}$$
***

<center>表2.1：海狸飞机的一些基本参数</center>

```Python
import numpy as np
import matplotlib.pyplot as plt
from math import sin,cos,tan,pi,atan,sqrt
from scipy.optimize import fmin

Ix = 5368.39
Iy = 6928.93
Iz = 11158.75
Jxz = 117.64
m = 2288.231
b = 14.63 # wing span
c = 1.5875 # aerodynamic chord
S = 23.23 # wing aera

Irr = (Ix * Iz - Jxz ** 2)
Ppq = ((Ix - Iy + Iz) * Jxz) / Irr
Pqr = ((Iy - Iz) * Iz - Jxz ** 2) / Irr
Pn = Jxz / Irr
Pl = Iz / Irr
Qpp = -Jxz / Iy
Qpr = (Iz - Ix) / Iy
Qrr = Jxz / Iy
Qm = 1 / Iy
Rpq = ((Ix - Iy) * Ix + Jxz ** 2) / Irr
Rqr = ((Iy - Iz - Ix) * Jxz) / Irr
Rn = Ix / Irr
Rl = Jxz / Irr

```

##### 函数 runge_kutta
我们使用四阶龙格库塔数值积分(RK4)的方法求解微分方程。

输入变量一共有5个，分别是常微分方程函数 odes_fun、时刻 T、状态量 X、输入量 U、时间步长 dT。输入量类型为元组，时间步长带有默认值。输入是时刻 T 的状态量，输出是 T+dT 时刻的状态量。

注意：输入的 常微分方程函数 要保持统一的形式！

```Python
def runge_kutta(odes_fun, T, X, U:tuple, dT=0.02):
	"""
	Input:
		X: states variables, T
		U: input variables
		T: time
		dT: time step
		odes_fun: ODEs function
	Output:
		X: states variables, T+dT
	e.g.
		States equations:
			XDot = A X + B U
			Y = C X + D U
	"""
	k1 = dT * odes_fun(X, T, U)
	k2 = dT * odes_fun(X + 0.5 * k1, T + 0.5 * dT, U)
	k3 = dT * odes_fun(X + 0.5 * k2, T + 0.5 * dT, U)
	k4 = dT * odes_fun(X + k3, T + dT, U)
	
	return X + (k1 + 2 * k2 + 2 * k3 + k4) / 6
	
```

##### 函数 dynamic_model
这里的函数 dynamic_model 包含12个微分方程的公式。但是我们从输入参数上看，它作为 rk4_run 中的 f，还多了不少输入参数。由于随着仿真时间的变化，12个微分方程中的力和力矩也是在随着飞机姿态变化而变化，所以力和力矩的更新计算还需要额外的关系式。

函数名 dynamic_model，输入变量有4个，依次分别是状态变量 States、力与力矩变量 FMtots、重力加速度 g、时间 t，输出是状态变量的导数 dStates。这里如果力与力矩设置为常数，重力加速度也取定值，适当修改RK4函数，是完全能够绘制出12个状态变量的时间变化图的。

```Python
def dynamics_model(States, FMtots):
	"""
	Input:
		States
		FMtots
	Output:
		dStates
	p.s.
		States = [V, alpha, beta, p, q, r, psi, theta, phi, x, y, h]
		FMtots = [X, Y, Z, L, M, N]
	"""
	
	# States Map In
	Va = States[0]
	alpha = States[1]
	beta = States[2]
	P = States[3]
	Q = States[4]
	R = States[5]
	psi = States[6]
	theta = States[7]
	phi = States[8]
	Xe = States[9]
	Ye = States[10]
	Ze = States[11]
	
	# FMtots Map In
	X = FMtots[0]
	Y = FMtots[1]
	Z = FMtots[2]
	L = FMtots[3]
	M = FMtots[4]
	N = FMtots[5]
	
	VaDot = (X * cos(alpha) * cos(beta) + Y * sin(beta) + Z * sin(alpha) * cos(beta)) / m
	alphaDot = (-X * sin(alpha) + Z * cos(alpha)) / (m * Va * cos(beta)) + Q - (P * cos(alpha) + R * sin(alpha)) * tan(beta)
	betaDot = (-X * cos(alpha) * sin(beta) + Y * cos(beta) - Z * sin(alpha) * sin(beta)) / (m * Va) + P * sin(alpha) - R * cos(alpha)
	
	psiDot = (Q * sin(phi) + R * cos(phi)) / cos(theta)
	thetaDot = Q * cos(phi) - R * sin(phi)
	phiDot = P + Q * sin(phi) * tan(theta) + R * cos(phi) * tan(theta) 
	
	PDot = Ppq * P * Q + Pqr * Q * R + Pn * N + Pl * L
	QDot = Qpp * P * P + Qpr * P * R + Qrr * R * R + Qm * M
	RDot = Rpq * P * Q + Rqr * Q * R + Rn * N + Rl * L
	
	U = Va * cos(alpha) * cos(beta)
	V = Va * sin(beta)
	W = Va * sin(alpha) * cos(beta) 
	
	XeDot = (U * cos(theta) + (V * sin(phi) + W * cos(phi)) * sin(theta)) * cos(psi) - (V * cos(phi) - W * sin(phi)) * sin(psi)
	YeDot = (U * cos(theta) + (V * sin(phi) + W * cos(phi)) * sin(theta)) * sin(psi) + (V * cos(phi) - W * sin(phi)) * cos(psi)
	ZeDot = - U * sin(theta) + (V * sin(phi) + W * cos(phi)) * cos(theta)
	
	# States Map Out
	dStates = np.array(States)
	dStates[0] = VaDot
	dStates[1] = alphaDot
	dStates[2] = betaDot
	dStates[3] = PDot
	dStates[4] = QDot
	dStates[5] = RDot
	dStates[6] = psiDot
	dStates[7] = thetaDot
	dStates[8] = phiDot
	dStates[9] = XeDot
	dStates[10] = YeDot
	dStates[11] = ZeDot
	
	return dStates

```

## 2.3 力和力矩模型
这里考虑三种对产生力和力矩的情况：
1. 气动力和气动力矩；
2. 由于发动机的操作产生的力和力矩；
3. 重力产生的力。

### 2.3.1 气动力和力矩模型
气动力和气动力矩的系数可以写成非线性多项式的形式。忽略空气的压缩性，空速假定足够低（这对海狸飞机也是合理的假设）。海狸飞机的气动模型可以用体坐标系下的无量纲力和力矩系数组成的多项式表示：

$$\begin{array}{l}
No. & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7  \\
C_{X_{\mathrm{a}}} =& C_{X_{0}} & + C_{X_{\alpha}} \cdot \alpha& +C_{X_{\alpha^{2}}} \cdot \alpha^{2} & + C_{X_{\alpha^{3}}} \cdot \alpha^{3} & + C_{X_{q}} \cdot \frac{q \bar{c}}{V} & + C_{X_{\delta_{r}}} \cdot \delta_{\mathrm{r}} & + C_{X_{\delta_{f}}} \cdot \delta_{\mathrm{f}} & + C_{X_{\alpha \delta f}} \cdot \alpha \cdot \delta_{\mathrm{f}} \\
C_{Y_{\mathrm{a}}} =& C_{Y_{0}} & + C_{Y_{\beta}} \cdot \beta & + C_{Y_{p}} \cdot \frac{p b}{2 V} & + C_{Y_{r}} \cdot \frac{r b}{2 V} & +
C_{Y_{\delta_{a}}} \cdot \delta_{\mathrm{a}} & + C_{Y_{\delta_{\mathrm{r}}}} \cdot \delta_{\mathrm{r}}& +C_{Y_{\delta_{\mathrm{r}} \alpha}} \cdot \delta_{\mathrm{r}} \alpha & + C_{Y_{\dot \beta}} \cdot \frac{\dot{\beta} b}{2 V}\\
C_{Z_{\mathrm{a}}} =& C_{Z_{0}} & + C_{Z_{\alpha}} \cdot \alpha& +C_{Z_{\alpha^{3}}} \cdot \alpha^{3}& +C_{Z_{q}} \cdot \frac{q \bar{c}}{V} & + C_{Z_{\delta_{e}}} \cdot \delta_{\mathrm{e}} & + C_{Z_{\delta_{e} \beta^{2}}} \cdot \delta_{\mathrm{e}} \cdot \beta^{2} & + C_{Z_{\delta_{f}}} \cdot \delta_{\mathrm{f}} & + C_{Z_{\alpha \delta_{f}}} \cdot \alpha \cdot \delta_{\mathrm{f}}\\
C_{l_{\mathrm{a}}} =& C_{l_{0}}&+C_{l_{\beta}} \cdot \beta & + C_{l_{p}} \cdot \frac{p b}{2 V}&+C_{l_{r}} \cdot \frac{r b}{2 V}&+C_{l_{\delta_{a}}} \cdot \delta_{\mathrm{a}}&+C_{l_{\delta_{r}}} \cdot \delta_{\mathrm{r}}&+C_{l_{\delta_{a \alpha}}} \cdot \delta_{\mathrm{a}} \cdot \alpha\\
C_{m_{\mathrm{a}}} =& C_{m_{0}} &+ C_{m_{\alpha}} \cdot \alpha &+ C_{m_{\alpha^{2}}} \cdot \alpha^{2} & + C_{m_{q}} \cdot \frac{q \bar{c}}{V} & + C_{m_{\delta_{e}}} \cdot \delta_{\mathrm{e}} & + C_{m_{\beta^{2}}} \cdot \beta^{2}&+C_{m_{r}} \cdot \frac{r b}{2 V}&+C_{m_{\delta_{f}}} \cdot \delta_{\mathrm{f}} \\
C_{n_{\mathrm{a}}} =& C_{n_{0}} &+ C_{n_{p}} \cdot \beta &+ C_{n_{p}} \cdot \frac{p b}{2 V} & + C_{n_{r}} \cdot \frac{r b}{2 V} & + C_{n_{\delta_{a}}} \cdot \delta_{\mathrm{a}} & + C_{n_{\delta_{r}}} \cdot \delta_{\mathrm{r}}&+C_{n_{q}} \cdot \frac{q \bar{c}}{V}&+C_{n_{\beta^{3}}} \cdot \beta^{3}
\end{array}$$

由气动产生的力和力矩由下面无量纲气动系数计算的到：

$$\begin{array}{l}
X_{a}=C_{X_{a}} \cdot \frac{1}{2} \rho V^{2} S \\
Y_{a}=C_{Y_{a}} \cdot \frac{1}{2} \rho V^{2} S \\
Z_{a}=C_{Z_{a}} \cdot \frac{1}{2} \rho V^{2} S \\
L_{a}=C_{l_{a}} \cdot \frac{1}{2} \rho V^{2} S b \\
M_{a}=C_{m_{a}} \cdot \frac{1}{2} \rho V^{2} S \bar{c} \\
N_{a}=C_{n_{a}} \cdot \frac{1}{2} \rho V^{2} S b
\end{array}$$

##### 函数 aero_model
函数名 aero_model, 输入一共有两个，分别是状态变量 States、气动控制量 delt。输出返回气动产生的无量纲力和力矩系数 Ca。这里函数中要注意的是 AM j矩阵，这个矩阵储存着多项式模型的系数，而这个系数在变化的飞行状态下也是变化的，下面的仿真里会全部认为是定值。

```Python
def aero_model(States, delt):
	"""
	Input:
		States
		delt
	Output:
		Ca 
	p.s.
		States = [V, alpha, beta, p, q, r, psi, theta, phi, x, y, h]
		delt = [delt_e, delt_a, delt_r, delt_f]
	"""
	
	# delt Map In
	delt_e = delt[0]
	delt_a = delt[1]
	delt_r = delt[2]
	delt_f = delt[3]
	
	# States Map In
	V = States[0]
	alpha = States[1]
	beta = States[2]
	P = States[3]
	Q = States[4]
	R = States[5]
	
	x = np.array(
		[[1,    alpha,      alpha**2,   alpha**3,   Q*c/V,  delt_r,         delt_f,         alpha*delt_f],
		[1,     beta,       0.5*P*b/V,  0.5*R*b/V,  delt_a, delt_r,         delt_r*alpha,   0],
		[1,     alpha,      alpha**3,   Q*c/V,      delt_e, delt_e*beta**2, delt_f,         alpha*delt_f],
		[1,     beta,       0.5*P*b/V,  0.5*R*b/V,  delt_a, delt_r,         delt_a*alpha,   0],
		[1,     alpha,      alpha**2,   Q*c/V,      delt_e, beta**2,        0.5*R*b/V,      delt_f],
		[1,     beta,       0.5*P*b/V,  0.5*R*b/V,  delt_a, delt_r,         Q*c/V,          beta**3]]
	)
	
	Ca = np.zeros([1, 6])
	for i in range(0, 6, 1):
		Ca[0][i] = np.dot(AM[i], x[i])
	
	return Ca
	
```

### 2.3.2 发动机力和力矩模型
发动机产生的外部力和力矩，是受空速影响的，我们取变量 $dpt = \frac{\Delta p_t}{\frac{1}{2}\rho V^2}$。

$\Delta p_t$等于螺旋桨发动机前后压力差。对于海狸飞机来说，变量 $dpt$ 和空速 $V$ 和发动机功率满足关系：

$$\begin{array}{c}
dpt = \frac{\Delta p_{\mathrm{t}}}{\frac{1}{2} \rho V^{2}}=a+b \frac{P}{\frac{1}{2} \rho V^{3}} \\
with  \frac{P}{\frac{1}{2} \rho V^{3}}  in  \left|\frac{\mathrm{kW}}{\mathrm{kg} / \sec ^{3}}\right|, \quad a=0.08696  \quad and \quad b=191.18 .
\end{array}$$

发动机功率单位是[Nm/s]的计算式为：

$$\begin{array}{c}
P=0.7355 * \{-326.5 + [ 0.00412 \dot (p_{z}+7.4) \cdot (n+2010) + (408 - 0.0965 n) \cdot (1-\frac{\rho}{\rho_{0}})]\}
\end{array}$$

发动机模型的无量纲力和力矩系数可以用变量 dpt 来表示。计算关系式如下：

$$\begin{array}{l}
C_{X_{t}}=C_{X_{\Delta p_t}}\left(\frac{\Delta p_{t}}{\frac{1}{2} \rho V^{2}}\right)+C_{X_{\alpha \Delta p_{t}}} \cdot \alpha\left(\frac{\Delta p_{t}}{\frac{1}{2} \rho V^{2}}\right)^{2}\\
C_{Y_{t}}=0\\
C_{Z_{t}}=C_{Z_{\Delta p_{t}}}\left(\frac{\Delta p_{t}}{\frac{1}{2} \rho V^{2}}\right)\\
C_{l_{t}}=C_{l_{\alpha^{2} \Delta p_{t}}} \cdot \alpha^{2}\left(\frac{\Delta p_{t}}{\frac{1}{2} \rho V^{2}}\right)\\
C_{m_{t}}=C_{m_{\Delta p_{t}}}\left(\frac{\Delta p_{t}}{\frac{1}{2} \rho V^{2}}\right)\\
C_{n_{t}}=C_{n_{\Delta p_{t}}{ }^{3}}\left(\frac{\Delta p_{t}}{\frac{1}{2} \rho V^{2}}\right)^{3}
\end{array}$$

与气动模型一样，我们计算发动机产生的力和力矩：

$$\begin{array}{l}
X_{t}=C_{X_{t}} \cdot \frac{1}{2} \rho V^{2} S \\
Y_{t}=C_{Y_{t}} \cdot \frac{1}{2} \rho V^{2} S \\
Z_{t}=C_{Z_{t}} \cdot \frac{1}{2} \rho V^{2} S \\
L_{t}=C_{l_{t}} \cdot \frac{1}{2} \rho V^{2} S b \\
M_{t}=C_{m_{t}} \cdot \frac{1}{2} \rho V^{2} S \bar{c} \\
N_{t}=C_{n_{t}} \cdot \frac{1}{2} \rho V^{2} S b
\end{array}$$

##### 函数 engine_model
函数名 engine_model, 输入一共有四个，分别是状态变量 States、发动机前后压差 Pz、发动机转速 n、大气密度 $\rho$。输出返回发动机产生的无量纲力和力矩系数 Ct。这里函数中要注意的是 EM 矩阵，这个矩阵储存着发动机无量纲力和力矩计算关系式的系数，下面仿真中这个系数矩阵也视为定值。

```Python
def engine_model(States, Pz, n, rho):
	""" 
	Input:
		States
		Pz: manidold pressure (''Hg)
		n: engine speed (rpm)
		rho: density (kg/m3) 
	Output:
		Ct: propulsive force and moment cofficients 
	p.s.
		States = [V, alpha, beta, p, q, r, psi, theta, phi, x, y, h]
	"""
	# States Map In
	V = States[0]
	alpha = States[1]
	
	P = (-326.5 + (0.00412 * (Pz +7.4) * (n + 2010) + (408 - 0.0965 * n) * (1 - rho / 1.225))) * 0.7355 # KW
	dp = 0.08696 + 191.18 * (P / (0.5 * rho * V ** 3))
	x = [[dp, alpha * dp ** 2], [0, 0], [dp, 0], [alpha ** 2 * dp, 0], [dp, 0], [dp ** 3, 0]]
	
	Ct = np.zeros([1, 6])
	for i in range(0, 6, 1):
		Ct[0][i] = np.dot(EM[i], x[i])
	
	return Ct
    
```

### 2.3.3 重力模型
飞机重量分解到体坐标系上是用欧拉角计算得来的。重力沿坐标轴的关系如下：

$$\begin{aligned}
X_{g r} &=-W \cdot \sin \theta \\
Y_{g r} &=W \cdot \cos \theta \sin \varphi \\
Z_{g r} &=W \cdot \cos \theta \cos \varphi
\end{aligned}$$

##### 函数 gravity
函数名 gravity, 输入一共有两个，分别是状态变量 States、重力加速度 g。输出返回重力在体坐标轴上的三个分量。

```Python
def gravity(States, g):
	[theta, phi] = States[7:9]
	Fx = -m * g * sin(theta)
	Fy = m * g * cos(theta) * sin(phi)
	Fz = m * g * cos(theta) * cos(phi)
	return Fx, Fy, Fz

```

## 2.4 $\dot \beta$ 修正关系式
从上面提到的气动模型我们知道，气动力 $Y_a$ 是与 $\dot \beta$ 有关的。因为 $\dot \beta$ 只有在状态变量更新后才能得到，所以 $\dot \beta$ 是隐式的。尽管可以数值求解，但我们不推荐这样做，因为这样会降低计算速度。那么使用显示表达的 $\dot \beta$ 是合适的。我们选用最简单的一种修正方式：

$$\begin{array}{c}
\dot{\beta}=\frac{\dot{\beta}^{*}}{1-\frac{\rho S b}{4 m} \cdot C_{Y_{\dot \beta}} \cos \beta}
\end{array}$$

## 2.5 大气模型
在计算力和力和力矩的公式中，中其实已经多次出现了大气密度 $\rho$。对于出海狸飞机外的其他飞机，飞行在更高的高度要，考虑空气的可压缩性，此时力和力矩的计算会依赖于马赫数，这样就需要再计算一些额外的变量，比如当量空速、校正空速、雷诺数等参与到模型的计算当中。但因为海狸飞机主要飞行在大气对流层，即海平面到海平面0m到11000m之间，故这里建模也只考虑对流层。

在标准大气模型中，对流层温度随高度的变化而变化的公式为：

$$\begin{array}{c}
T=T_{0}+\lambda \cdot h \\
where \ T_{0}=288.15 \mathrm{~K} \ and \ \lambda=-0.0065 \mathrm{~K} / \mathrm{m} .
\end{array}$$

对流层的压力随高度变化公式为：

$$\begin{array}{c}
p=p_{O}\left[\frac{T_{0}}{T}\right]^{\frac{M_0 g_0}{R_{a} \lambda}}, p \text { in }[\mathrm{mb}] \\
with \ \mathrm{R}_{\mathrm{a}}=8314.32 \mathrm{~J} / \mathrm{K} . \mathrm{kmol}, \mathrm{P}_{\mathrm{0}}=1013.12 \mathrm{mb}, \mathrm{M}_{0}=28.9644 \mathrm{~kg} / \mathrm{kmol} \ and \ g_{0}=9.80665 \mathrm{~m} / \mathrm{s}^{2} .
\end{array}$$

对流层密度随高度变化公式为：

$$\begin{array}{c}
\rho=\rho_{0}\left[\frac{T_{O}}{T}\right]^{\frac{M_{0} g_{O}}{R_{a^{\lambda}}}+1}, \\
\rho \text { in }\left[\mathrm{kg} / \mathrm{m}^{3}\right]
with \ p_{0}=1.225 \mathrm{~kg} / \mathrm{m}^{3} .
\end{array}$$

##### 函数 StdAtpUS
函数名 StdAtpUS, 输入是海平面高度 h。输出返回大气温度 T、压力 p 和密度 ρ。这里其实重力加速度也是随高度变化的，这里可以取定值 9.80665 m/s^2 计算，结果差别不大。当程序输入高度超出平流层高度范围时，程序会报错。

```Python
def StdAtpUS(h):
	"""Standard Atmosphere
	Input: 
		h: altitude(m)
	Output: 
		rho: air density(kg/m3)
		ps: static pressure(N/m^2)
		T: temperature(K)
		mu: dynamic viscosity(kg/(m*s))
		g: acceleration of gravity(m/s^2)
	"""     
	
	if h <= 11000:
		T = 288.15 - 0.0065 * h
		g = 9.80665 * (6371020 / (6371020 + h)) ** 2
		p = 101325 * (T / 288.15) ** (g / 1.86584)
		mu = (1.458 * 10 ** (-6) * T ** 1.5) / (T + 110.4)
		rho = p / (287.053 * T)
	else:
		print('Error: the altitude should be less than 11000 m')
	return rho, p, T, mu, g  

```
##### 函数 beaver
函数名 beaver, 输入一共有三个，分别是状态变量 States，时间 t，参数 Params，输出返回状态变量的导数 dStates，这个函数用在数值积分中进行迭代求解。
```Python
def beaver(States, t, Params):
	"""
	Input:
		States
		t
		Params
	Output:
		dStates
	"""
	
	# Params Map In
	delt = Params[0:4]
	n = Params[4]
	pz = Params[5]
	
	# atmosphere model
	rho, _, _, _, g = StdAtpUS(States[11])
	
	# aero model
	Ca = aero_model(States, delt)
	
	# engine model
	Ct = engine_model(States, pz, n, rho)
	
	# calculate force and moment
	V = States[0]
	[Fx, Fy, Fz] = gravity(States, g)
	X = 0.5 * rho * V ** 2 * S * (Ct[0][0] + Ca[0][0]) + Fx
	Y = 0.5 * rho * V ** 2 * S * (Ct[0][1] + Ca[0][1]) + Fy
	Z = 0.5 * rho * V ** 2 * S * (Ct[0][2] + Ca[0][2]) + Fz
	L = 0.5 * rho * V ** 2 * S * b * (Ct[0][3] + Ca[0][3])
	M = 0.5 * rho * V ** 2 * S * c * (Ct[0][4] + Ca[0][4])
	N = 0.5 * rho * V ** 2 * S * b * (Ct[0][5] + Ca[0][5])
	
	FM = np.array([X, Y, Z, L, M, N])
	
	dStates = dynamics_model(States, FM)
	dStates[2] = dStates[2] / (1 - 0.25 * rho * S * b * cos(States[2]) * (-0.16) / m)
	
	return dStates

```

## 2.6 测试用例一：开环模型

基于上面模型函数，可以拼凑出一个开环模型。这个开环模型的输入包括有状态变量初值 state，气动控制量 delt，气动系数矩阵 AM，发动机系数矩阵 EM，发动机前后压差 Pz，发动机转速 n。在 fdc14 工具箱中该模型使用 simulink 表示如图 2.2。设置数值积分方法为定步长的 ode4(四阶rk4)方法，参数设置示意图如图 2.3。用给出的测试用例的仿真结果图如图 2.4。

![[p3.jpg]]
<center>图2.2：海狸飞机开环模型 Simulink 结构图</center>

![[p4.jpg]]
<center>图2.3：海狸飞机开环模型 Simulink 设置图</center>

![[p5.jpg]]
<center>图2.4：海狸飞机开环模型 Simulink 结果图</center>

目前程序可能还存在的问题有：
1. 程序之间计算先后顺序不同，数值精度出现微小不同（确定存在）    
2. 高度表现趋势相反（还未查明）

```Python
# states = [V, alpha, beta, p, q, r, psi, theta, phi, x, y, h]
# params = [delt_e, delt_a, delt_r, delt_f, n, pz, 0, 0, 0, 0, 0, 0]
states = np.array([35, 0.218893146156331, -0.0225956102215801, 0, 0, 0, 0, 0.218893146156331, 0, 0, 0, 609.600000000000])
params = np.array([-0.108711002857073, 0.00809466546101647, -0.0645833320683813, 0, 1800, 21.3996401314681, 0, 0, 0, 0, 0, 0])

AM = np.array(
    [[-3.554e-02,  2.920e-03,  5.459e+00, -5.162e+00, -6.748e-01,  3.412e-02,  -9.447e-02,  1.106e+00],
     [-2.226e-03, -7.678e-01, -1.240e-01,  3.666e-01, -2.956e-02,  1.158e-01,   5.238e-01,  0.000e+00],
     [-5.504e-02, -5.578e+00,  3.442e+00, -2.988e+00, -3.980e-01, -1.593e+01,  -1.377e+00, -1.261e+00],
     [ 5.910e-04, -6.180e-02, -5.045e-01,  1.695e-01, -9.917e-02,  6.934e-03,  -8.269e-02,  0.000e+00],
     [ 9.448e-02, -6.028e-01, -2.140e+00, -1.556e+01, -1.921e+00,  6.921e-01,  -3.118e-01,  4.072e-01],
     [-3.117e-03,  6.719e-03, -1.585e-01, -1.112e-01, -3.872e-03, -8.265e-02,   1.595e-01,  1.373e-01]]
)
EM = np.array([[0.1161, 0.1453], [0, 0], [-0.1563, 0], [-0.01406, 0], [-0.07895, 0], [-0.003026, 0]])

dt = 0.02
t_end = 200
results = np.array(states)
ts = np.arange(0, t_end, dt)
ylab = ['V', 'alpha', 'beta', 'P', 'Q', 'R', 'psi', 'theta', 'phi', 'Xe', 'Ye', 'Ze']

for t in ts:
    states = runge_kutta(odes_fun=beaver, T=t, X=states, U=params, dT=dt)
    results = np.row_stack((results, states))

fig = plt.figure(figsize=(20,20))
for plt_index in range(0, 12, 1):
    plt.subplot(4, 3, plt_index + 1)
    plt.plot(ts, results[:-1, plt_index])
    plt.xlabel('t')
    plt.ylabel(ylab[plt_index])

```