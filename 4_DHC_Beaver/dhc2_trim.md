# 3 稳定状态配平飞行

这一章节将给出配平程序，可以生成一组稳定状态飞行的初始状态值，输入到开环模型当中。


## 3.1 稳定状态飞行的定义

一般的刚体飞机的非线性动力运动方程，可以写作一组微分方程（ODEs）。用 $\mathbf{x}$ 表示微分方程计算的12个变量组成的向量，后文称作状态向量，用 $\mathbf{u}$ 表示除此之外的气动操纵面，发动机参数等变量组成的向量，后文称作控制向量。新的一般形式的微分方程组表示为：

$$\begin{array}{c}
\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x}(t), \mathbf{u}(t), t)
\end{array}$$

再进一步的一般形式，是把状态向量分成了两部分。第一组是需要保持不变的状态变量，它们的导数要恒等于 0。第二组是要在配平程序中进行不断调整的状态变量，以维持前者的平衡。

$$\begin{array}{c}
\mathbf{f}(\dot{\mathbf{x}}(t), \mathbf{x}(t), \mathbf{u}(t), t)=0
\end{array}$$

一个自动的（没有外部控制输入），时变的系统的一个奇异点，或者叫平衡点是这样定义的：

$$\begin{array}{c}
\mathbf{f}(\dot{\mathbf{x}}, \mathbf{x}, \mathbf{u})=0, \text { with: } \dot{\mathbf{x}} \equiv 0 ; \mathbf{u}\equiv 0 \text { or const. }
\end{array}$$

稳定状态飞行可以定义为一种状态，它的状态变量为常数或者为零，并且所有的加速度分量均为零。如果考虑了平整地球假设和飞机定质量假设，那么稳定水平飞行和稳定转弯飞行的配平是稳定状态飞行。如果忽略配平程序中大气密度随高度的变化，那么稳定爬升和稳定转向也是稳定状态飞行。因为关于 $x_e$ $y_e$ 和 $H$ 的方程不与其他运动方程耦合，所以在配平中先不考虑。

综上，稳定状态飞行可以用剩下的 9 个变量定义：

$$\begin{array}{c}
\dot{p}, \dot{q}, \dot{r}, \dot{V}, \dot{\alpha}, \dot{\beta}=0, \quad n， p_z， \delta_f =\text { const. }
\end{array}$$

特殊的飞行状态还需要考虑一些额外的约束。这里考虑的飞行状态有：稳定水平飞行，稳定转弯飞行，稳定拉升或下降，稳定滚转四种稳定状态飞行。按照上面的定义，它们的约束表示为：

$$\begin{array}{lllll}
\text { steady wings-level flight: } & \varphi, \dot{\varphi}, \dot{\theta}, \dot{\psi}=0 & (\therefore p, q, r \pm 0) \\
\text { steady turning flight: } & \dot{\varphi}, \dot{\theta}=0, & \dot{\psi} \equiv \text { turn rate } \\
\text { steady pull-up: } & \varphi, \dot{\varphi}, \dot{\psi}=0, & \dot{\theta}=\text { pull-up rate } \\
\text { steady roll: } & \dot{\theta}, \dot{\psi}=0, & \dot{\varphi} \equiv \text { roll rate }
\end{array}$$

## 3.2 爬升率约束和协调转弯约束

飞行过程中的航迹角满足下面关系式：

$$\begin{array}{l}
\sin \gamma=a \sin \theta-b \cos \theta \\
a=\cos \alpha \cos \beta \\
b=\sin \varphi \sin \beta+\cos \varphi \sin \alpha \cos \beta
\end{array}$$

考虑爬升率约束可以得到：

$$\begin{array}{c}
\tan \theta=\frac{a b+\sin \gamma \sqrt{a^{2}-\sin ^{2} \gamma+b^{2}}}{a^{2}-\sin ^{2} \gamma}, \quad \theta \neq \pm \frac{\pi}{2}
\end{array}$$

如果同时考虑爬升率约束和协调转弯约束：

$$\begin{array}{c}
\tan \varphi=G \frac{\cos \beta}{\cos \alpha} \frac{\left(\tilde{a}-\tilde{b}^{2}\right)+\tilde{b} \tan \alpha \sqrt{\tilde{c}\left(1-\tilde{b}^{2}\right)+G^{2} \sin ^{2} \beta}}{\tilde{a}^{2}-\tilde b^{2}\left(1+\tilde{c} \tan ^{2} \alpha\right)} \\
\tilde{a} = 1-G \tan \alpha \sin \beta \\
\tilde{b} = \frac{\sin \gamma}{\cos \beta} \\
\tilde{c} = 1+G^{2} \cos ^{2} \beta \\
G = \frac{\dot{\psi} V}{g_{0}}
\end{array}$$

知道了约束关系式后，就可以写一般的飞机配平算法了。

## 3.3 稳定状态飞行配平算法

解非线性方程的稳定状态飞行的配平算法要使一组状态变量的导数均为零。这里采用一种数值算法，通过最小化一个代价函数 $J$ 值来实现配平。这个代价函数写为：

$$\begin{array}{c}
J=c_{1} \dot{V}^{2}+c_{2} \dot{\alpha}^{2}+c_{3} \dot{\beta}^{2}+c_{4} \dot{p}^{2}+c_{5} \dot{q}^{2}+c_{6} \dot{r}^{2}
\end{array}$$

这里的 $c_i,i \in {1,2,...,6}$是权重系数。首先，设置飞行条件。配平程序将对独立的状态变量做一个初始猜测，并对其他变量进行配平调整。接着，最小化程序。最小化程序将找到使得代价函数最小的一组输入变量。每个迭代步只根据约束更新一次状态变量。程序的停止条件是两次迭代步之间代价函数的差值。同样使用 scipy.fmin 函数寻优，也对最大迭代步数做出了限制，保证在程序无最小值的时候停止。

##### 函数 accost

```Python
def accost(vtrim, ctrim, rolltype, turntype, gammatype):
	[x, u] = acconstr(vtrim, ctrim, rolltype, turntype, gammatype)
	xDot = beaver(x, 0, u)
	J = xDot[0] ** 2 + 2 * (xDot[1] ** 2 + xDot[2] ** 2) + 5 * (xDot[3] ** 2 + xDot[4] ** 2 + xDot[5] ** 2 )
	return J
	
```

##### 函数 acconstr

```Python
def acconstr(vtrim, ctrim, rolltype, turntype, gammatype):
    '''
    该函数计算，在协调转弯和爬升率的约束下
    俯仰角 θ、滚转角 φ、飞机绕体坐标系轴的角加速度 p q r
    '''
    # print(rolltype, turntype, gammatype) # 稳态水平飞行: b c m

    if gammatype == 'f':
        [alpha, beta, delt_e, delt_a, delt_r, pz] = vtrim
        [V, H, psi, gamma, g, psiDot, thetaDot, phiDot, delt_f, n, phi] = ctrim
    elif gammatype == 'm':
        [alpha, beta, delt_e, delt_a, delt_r, gamma] = vtrim
        [V, H, psi, pz, g, psiDot, thetaDot, phiDot, delt_f, n, phi] = ctrim
    else:
        print('Wrong: Invalid input in acconstr !')

    # 计算滚转角 φ，考虑协调转弯约束 
    if turntype == 'c':
        a = 1 - g * sin(alpha)/cos(alpha) * sin(beta)
        b = sin(gamma)/cos(beta)
        c = 1 + (g * cos(beta)) ** 2
        num = cos(beta) * ((a - b ** 2) + b * tan(alpha) * sqrt(c * (1 - b ** 2)+ g ** 2 * sin(beta) ** 2))
        den = cos(alpha) * (a ** 2 - b ** 2 * (1 + tan(alpha) ** 2))
        phi = atan(g * num / den)
    
    # 计算俯仰角 θ，考虑爬升率约束
    a = cos(alpha) * cos(beta)
    b = sin(phi) * sin(beta) + cos(phi) * sin(alpha) * cos(beta)
    num = a * b + sin(gamma) * sqrt(a ** 2 - sin(gamma) ** 2 + b ** 2)
    den = a ** 2 - sin(gamma) ** 2
    theta = atan(num/den)

    # 计算角速度 p q r，考虑滚转角和俯仰角
    p = phiDot * cos(alpha) - sin(theta) * psiDot
    q = cos(phi) * thetaDot + sin(phi) * cos(theta) * psiDot
    r = -sin(phi) * thetaDot + cos(phi) * cos(theta) * psiDot + sin(alpha) * phiDot

    states = [ctrim[0], vtrim[0], vtrim[1], p, q, r, ctrim[2], theta, phi, 0.0, 0.0, ctrim[1]]
    params = [delt_e, delt_a, delt_r, delt_f, n, pz, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    
    return states, params
    
```

##### 函数 trim_steady_wings_level

```Python
def trim_steady_wings_level():
	"""稳定水平飞行
	飞行状态：
		其中 rolltype = 'b'
		其中 turntype = 'c'
		其中 gammatype = 'm'/'f'
	输入参数：
		V 速度 [m/s]
		H 高度 [m]
		ψ 偏航角 [deg]
		pz 发动机压差 [Hg] (γ 航迹角 [deg])
		n 发动机转速 [rpm]
		δf 襟翼角 [deg]
	"""
	
	print('配平飞行状态: 稳态水平飞行')
	
	V = float(input('输入期望速度 V [m/s]，默认值为 45:') or 45.0)
	H = float(input('输入初始高度 H [m]，默认值为 0:') or 0.0)
	psi = float(input('输入初始偏航角 psi [deg]，默认值为 0:') or 0.0) * pi / 180
	
	ok = 0
	while ok != 1:
		gammatype = input('给定压差配平航迹角<m> 或 给定航迹角配平压差<f>, 默认值为 m:') or 'm'
		if gammatype == 'm':
			ok = 1
		elif gammatype == 'f':
			gamma = float(input('输入初始航迹角 [deg]，默认值为 0:') or 0.0) * pi / 180
			ok = 1
		else:
			print('无效输入，请输入 m 或者 f !')
	
	rolltype = 'b'
	turntype = 'c'
	
	n = float(input('输入发动机转速 n [rpm]，默认值为 1800:') or 1800.0)       
	delt_f = float(input('输入襟翼角 delt_f [deg]，默认值为 0:') or 0.0)
	
	if gammatype == 'm':
		pz = float(input('输入发动前后压差 pz [Hg]，默认值为 20:') or 20.0)
	elif gammatype == 'f':
		pz = float(input('输入粗略估计的发动机前后压差 pz [Hg]，默认值为 20:') or 20.0)
	else:
		print('未知错误 !')
	
	psiDot = 0
	thetaDot = 0
	phiDot = 0
	
	g = psiDot * V / 9.80665
	phi = 0
	
	if gammatype == 'f':
		ctrim = np.array([V, H, psi, gamma, g, psiDot, thetaDot, phiDot, delt_f, n, phi])
		vtrim = np.array([0, 0, 0, 0, 0, pz])
	else:
		ctrim = np.array([V, H, psi, pz, g, psiDot, thetaDot, phiDot, delt_f, n, phi])
		vtrim = np.array([0, 0, 0, 0, 0, 0])
		
	xopt, _, iter, funcalls, warnflags = fmin(accost, vtrim, args=(ctrim, rolltype, turntype, gammatype), xtol = 1e-10, maxfun = 5000, disp=1, maxiter = 3000, full_output=1)
	
	if warnflags == 1 or warnflags == 2:
		print('Maximum number of iterations was exceeded!')
		print('number of function evaluations:',funcalls)
		print('number of iterations:',iter)
	else :
		print('Converged to a trimmed solution...')
	
	[states, params] = acconstr(xopt, ctrim, rolltype, turntype, gammatype)
	
	return states, params

```


##### 函数 trim_steady_roll

```Python
def trim_steady_roll():
	"""稳定滚转
	飞行状态：
		其中 rolltype = 'b'/'s'
		其中 turntype = 'c'
		其中 gammatype = 'f'/'m'
	输入参数：
		V 速度 [m/s]
		H 高度 [m]
		ψ 偏航角 [deg]
		pz 发动机压差 [Hg] γ 航迹角 [deg]
		thetaDot 拉升率 [deg/s] 
		n 发动机转速 [rpm]
		δf 襟翼角 [deg]
	"""
	
	print('配平飞行状态: 稳态滚转')
	
	V = float(input('输入期望速度 V [m/s]，默认值为 45:') or 45.0)
	H = float(input('输入初始高度 H [m]，默认值为 0:') or 0.0)
	psi = float(input('输入初始偏航角 psi [deg]，默认值为 0:') or 0.0) * pi / 180
	
	ok = 0
	while ok != 1:
		gammatype = input('给定压差配平航迹角<m> 或 给定航迹角配平压差<f>, 默认值为 m:') or 'm'
		if gammatype == 'm':
			ok = 1
		elif gammatype == 'f':
			gamma = float(input('输入初始航迹角 [deg]，默认值为 0:') or 0.0) * pi / 180
			ok = 1
		else:
			print('无效输入，请输入 m 或者 f !')
			
	psiDot = 0
	thetaDot = 0
	phiDot = float(input('输入滚转速率 [deg/s]，默认值为 0:') or 0.0) * pi / 180
	
	if phiDot != 0:
		ok = 0
		while ok != 1:
			rolltype = input('绕体坐标系<b> 或 绕稳定坐标系<s>, 默认值为 b:') or 'b'
			if gammatype == 'b' or gammatype == 'f':
				ok = 1
			else:
				print('无效输入，请输入 b 或者 s !')
	else:
		rolltype = 'b'
		
	turntype = 'c'
	
	n = float(input('输入发动机转速 n [rpm]，默认值为 1800:') or 1800.0)   
	delt_f = float(input('输入襟翼角 delt_f [deg]，默认值为 0:') or 0.0)
	
	if gammatype == 'm':
		pz = float(input('输入发动前后压差 pz [Hg]，默认值为 20:') or 20.0)
	elif gammatype == 'f':
		pz = float(input('输入粗略估计的发动机前后压差 pz [Hg]，默认值为 20:') or 20.0)
	else:
		print('未知错误 !')
	
	g = psiDot * V / 9.80665
	phi = 0.0 * pi /180
	
	if gammatype == 'f':
		ctrim = np.array([V, H, psi, gamma, g, psiDot, thetaDot, phiDot, delt_f, n, phi])
		vtrim = np.array([0, 0, 0, 0, 0, pz])
	else:
		ctrim = np.array([V, H, psi, pz, g, psiDot, thetaDot, phiDot, delt_f, n, phi])
		vtrim = np.array([0, 0, 0, 0, 0, 0])
		
	xopt, _, iter, funcalls, warnflags = fmin(accost, vtrim, args=(ctrim, rolltype, turntype, gammatype), xtol = 1e-10, maxfun = 5000, disp=1, maxiter = 3000, full_output=1)
	
	if warnflags == 1 or warnflags == 2:
		print('Maximum number of iterations was exceeded!')
		print('number of function evaluations:',funcalls)
		print('number of iterations:',iter)
	else :
		print('Converged to a trimmed solution...')
	
	[states, params] = acconstr(xopt, ctrim, rolltype, turntype, gammatype)
	
	return states, params
	
```

##### 函数 trim_steady_turning

```Python
def trim_steady_turning():
	"""稳定转向
	飞行状态：
		其中 rolltype = 'b'
		其中 turntype = 'c'/'v'
		其中 gammatype = 'm'/'f'
	输入参数：
		V 速度 [m/s]
		H 高度 [m]
		ψ 偏航角 [deg]
		pz 发动机压差 [Hg] (γ 航迹角 [deg])
		phiDot 转弯率 [deg/s] / R 转弯半径 [deg]
		n 发动机转速 [rpm]
		δf 襟翼角 [deg]
	"""
	
	print('配平飞行状态: 稳定转向')
	
	ok = 0
	while ok != 1:
		turntype = input('协调转弯<c> 或 不协调转弯<v>, 默认值为 c:') or 'c'
		if turntype == 'c' or turntype == 'v':
			ok = 1
		else:
			print('无效输入，请输入 c 或者 v !')
	
	V = float(input('输入期望速度 V [m/s]，默认值为 45:') or 45.0)
	H = float(input('输入初始高度 H [m]，默认值为 0:') or 0.0)
	psi = float(input('输入初始偏航角 psi [deg]，默认值为 0:') or 0.0) * pi / 180
	
	ok = 0
	while ok != 1:
		gammatype = input('给定压差配平航迹角<m> 或 给定航迹角配平压差<f>, 默认值为 m:') or 'm'
		if gammatype == 'm':
			ok = 1
		elif gammatype == 'f':
			gamma = float(input('输入初始航迹角 [deg]，默认值为 0:') or 0.0) * pi / 180
			ok = 1
		else:
			print('无效输入，请输入 m 或者 f !')
	
	ok = 0
	while ok != 1:
		answ = input('设置固定转弯率<t> 或 转弯半径<r>, 默认值为 t:') or 't'
		if answ == 't':
			phiDot = float(input('输入转弯率 [deg/s]，默认值为 0:') or 0.0) * pi / 180
			ok = 1
		elif answ == 'r':
			R = float(input('输入转弯半径 (>0)[m]，默认值为 水平直线飞行:')) or 's'
			if R != 's':
				psiDot = V/R
			else:
				psiDot = 0 
			ok = 1
		else:
			print('无效输入，请输入 t 或者 r !')
	
	thetaDot = 0
	psiDot = 0
	rolltype = 'b'
	
	n = float(input('输入发动机转速 n [rpm]，默认值为 1800:') or 1800.0)   
	delt_f = float(input('输入襟翼角 delt_f [deg]，默认值为 0:') or 0.0)
	
	if gammatype == 'm':
		pz = float(input('输入发动前后压差 pz [Hg]，默认值为 20:') or 20.0)
	elif gammatype == 'f':
		pz = float(input('输入粗略估计的发动机前后压差 pz [Hg]，默认值为 20:') or 20.0)
	else:
		print('未知错误 !')
	
	g = psiDot * V / 9.80665
	
	if turntype == 'v':
		phi = float(input('输入期望滚转角 phi [deg],默认值为 0') or 0.0 * pi / 180)
	else:
		phi = 0.0 * pi /180
	
	if gammatype == 'f':
		ctrim = np.array([V, H, psi, gamma, g, psiDot, thetaDot, phiDot, delt_f, n, phi])
		vtrim = np.array([0, 0, 0, 0, 0, pz])
	else:
		ctrim = np.array([V, H, psi, pz, g, psiDot, thetaDot, phiDot, delt_f, n, phi])
		vtrim = np.array([0, 0, 0, 0, 0, 0])
	
	xopt, _, iter, funcalls, warnflags = fmin(accost, vtrim, args=(ctrim, rolltype, turntype, gammatype), xtol = 1e-10, maxfun = 5000, disp=1, maxiter = 3000, full_output=1)
	
	if warnflags == 1 or warnflags == 2:
		print('Maximum number of iterations was exceeded!')
		print('number of function evaluations:',funcalls)
		print('number of iterations:',iter)
	else :
		print('Converged to a trimmed solution...')
	
	[states, params] = acconstr(xopt, ctrim, rolltype, turntype, gammatype)
	
	return states, params

```


##### 函数 trim_steady_pull_up

```Python
def trim_steady_pull_up():
	"""稳定拉升
	飞行状态：
		其中 rolltype = 'b'
		其中 turntype = 'c'/'v'
		其中 gammatype = 'f'
	输入参数：
		V 速度 [m/s]
		H 高度 [m]
		ψ 偏航角 [deg]
		pz 发动机压差 [Hg] γ 航迹角 [deg]
		thetaDot 拉升率 [deg/s] 
		n 发动机转速 [rpm]
		δf 襟翼角 [deg]
	"""
	
	print('配平飞行状态: 稳定拉升')
	
	V = float(input('输入期望速度 V [m/s]，默认值为 45:') or 45.0)
	H = float(input('输入初始高度 H [m]，默认值为 0:') or 0.0)
	psi = float(input('输入初始偏航角 psi [deg]，默认值为 0:') or 0.0) * pi / 180
	
	gammatype = 'f'
	gamma = float(input('输入初始航迹角 [deg]，默认值为 0:') or 0.0) * pi / 180
	
	phiDot = 0
	psiDot = 0
	thetaDot = float(input('输入拉升率 [deg/s]，默认值为 0:') or 0.0) * pi / 180
	
	rolltype = 'b'
	turntype = 'c'
	
	n = float(input('输入发动机转速 n [rpm]，默认值为 1800:') or 1800.0)   
	delt_f = float(input('输入襟翼角 delt_f [deg]，默认值为 0:') or 0.0)
	pz = float(input('输入粗略估计的发动机前后压差 pz [Hg]，默认值为 20:') or 20.0)
	
	g = psiDot * V / 9.80665
	phi = 0.0 * pi /180
	
	ctrim = np.array([V, H, psi, gamma, g, psiDot, thetaDot, phiDot, delt_f, n, phi])
	vtrim = np.array([0, 0, 0, 0, 0, pz])
	xopt, _, iter, funcalls, warnflags = fmin(accost, vtrim, args=(ctrim, rolltype, turntype, gammatype), xtol = 1e-10, maxfun = 5000, disp=1, maxiter = 3000, full_output=1)
	
	if warnflags == 1 or warnflags == 2:
		print('Maximum number of iterations was exceeded!')
		print('number of function evaluations:',funcalls)
		print('number of iterations:',iter)
	else :
		print('Converged to a trimmed solution...')
	
	[states, params] = acconstr(xopt, ctrim, rolltype, turntype, gammatype)
	
	return states, params

```

## 3.4 测试用例二：带配平的开环模型

```Python
# states = [V, alpha, beta, p, q, r, psi, theta, phi, x, y, h]
# params = [delt_e, delt_a, delt_r, delt_f, n, pz, 0, 0, 0, 0, 0, 0]
# states = np.array([35, 0.218893146156331, -0.0225956102215801, 0, 0, 0, 0, 0.218893146156331, 0, 0, 0, 609.600000000000])
# params = np.array([-0.108711002857073, 0.00809466546101647, -0.0645833320683813, 0, 1800, 21.3996401314681, 0, 0, 0, 0, 0, 0])
	
states, params = trim_steady_wings_level()
	
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