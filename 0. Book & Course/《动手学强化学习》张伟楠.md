[动手学强化学习 (boyuai.com)](https://hrl.boyuai.com/)动手学强化学习网站 张伟楠

序贯决策(sequential decision making)
强化学习(reinforcement learning)
智能体(agent)
环境的下一刻状态的概率分布由当前状态和智能体的动作共同决定
$\text{下一状态}\sim P(\cdot|\text{当前状态},\text{智能体的动作})$
回报(return)
回报的期望(value)
占用度量(occupancy measure)
状态动作对(state-action pair)

一般的监督学习关注寻找一个模型，使其在给定数据分布下得到的损失函数的期望最小
强化学习关注寻找一个智能体策略，使其在与动态环境交互的过程中产生最优的数据分布，即最大化该分布下一个给定奖励函数的期望

# 多臂老虎机

多臂老虎机(multi-armed bandit, MAB)
探索与利用(exploration vs. exploitation)

在多臂老虎机问题中，假设共有$K$个老虎机，每个老虎机服从伯努利分布，当$p$时视为中奖，奖励为1；当$1-p$时视为没中奖，奖励为0。决策使用$\epsilon$-贪心算法，当$\epsilon$时代表随机选择一个老虎机杆拉下，当$1-\epsilon$时选择过往期望值最高的老虎机杆拉下(这就要求在每次决策完，更新拉下老虎机的期望值，期望更新使用增量更新$Q_{k}=Q_{k-1}+\frac1k[r_k-Q_{k-1}]$，这样更新的所有老虎机的过往期望能够再次用到下一次决策上，这里初始期望设置为1)。动作完成后，更新老虎机的拉杆次数，记录下该次动作，更新懊悔函数。老虎机的目标是在$T$次拉杆后获得尽可能高的累计奖励。

因为假设每次拉一个老虎机，那也就是共有$K$种动作可以选择，动作空间表示为$\{a_{1},\ldots,a_{K}\}$，用$a_{t}\in\mathcal{A}$表示任意一个动作。拉下老虎机的奖励服从一定概率分布(这里假设是伯努利分布)，奖励概率分布表示为$\mathcal{R}(r|a)$，那多臂老虎机的目标最大化一段时间步内的累计奖励就表示为$\max\sum_{t=1}^Tr_t,r_t\sim\mathcal{R}\left(\cdot|a_t\right)$。

对于每一个动作都有其期望奖励$Q(a)=\mathbb{E}_{r\sim\mathcal{R}(\cdot|a)}\left[r\right]$(这里的期望奖励很容易用伯努利分布期望公式计算为$p$)
最优期望奖励表示为其中期望最高的老虎机的奖励期望$Q^{*}=\max_{a\in\mathcal{A}}Q(a)$。懊悔定义为当前拉杆的期望与最优期望的差值$R(a)=Q^{*}-Q(a)$，累计懊悔是一次完整$T$步决策后的懊悔总量$\sigma_R=\sum_{t=1}^TR(a_t)$。MAB问题的目标是最大化累计奖励，等价于最小化累计懊悔。

怎么理解最大化累计奖励等价于最小化累计懊悔？因为你要想容易中奖，其实就应该一直拉奖励期望高的老虎机，但是这样也会存在小概率你拉其他老虎机中奖次数比你拉期望最高的老虎机中奖次数高的情况，为了排除小概率做出了探索(使用衰减$\epsilon$-贪心算法，可以使得累计懊悔次线性收敛)。但这样就会造成懊悔，懊悔没有用最好的老虎机拉杆，这也能看出懊悔是一定会不断增加的(因为每次选择的老虎机不会比最好的老虎机更好)。这里老虎机的中奖假定为不变的伯努利分布，**但真实情况环境可能是未知分布的而且分布是受动作影响的**，懊悔可能就不能这样来计算。

上置信界(upper confidence bound, UCB)
霍夫不等式(Hoeffding's inequality)
一个从未被拉杆的老虎机不确定性很大，越具有探索的价值。
在上置信界算法中设置$p=\frac{1}{t}$，同一台老虎机的拉杆次数越多(经验奖励期望越接近真实期望)，概率越低。根据$\hat{U}_t(a)=\sqrt{\frac{\log t}{2(N_t(a)+1)}}$得到不确定性度量越低，期望奖励上界$\hat{Q}_{t}(a)+\hat{U}_{t}(a)$越接近真实期望，$Q_{t}(a)<\hat{Q}_{t}(a)+\hat{U}_{t}(a)$成功的概率$1-p$越高。

汤普森采样(Thompson sampling)
假设每根拉杆奖励服从一个特定的概率分布，然后根据拉杆的期望奖励进行选择，但是计算每根拉杆的期望奖励代价是比较高的，汤普森采样会对每个动作的奖励概率分布进行一波采样，得到奖励样本，从样本中选择奖励最大的动作(样本估计总体)，这是一种计算所有拉杆最高奖励概率的蒙特卡洛采样方法。

多臂老虎机问题和强化学习的区别在于其与环境的交互并不会改变环境，每次交互的结果和以往的动作无关，可以看做无状态的强化学习(stateless reinforcement learning)。

`多臂老虎机问题中智能体是人，环境是老虎机，动作是拉杆；每次动作后环境不会发生改变，环境也不会自发改变；奖励与动作完成后环境的状态有关；决策是选择哪个老虎机拉杆，受到环境中每个老虎机已经被拉下的次数和过往奖励期望影响，选择无非是选择期望最优的老虎机，或者选择期望非最优的老虎机，不同策略的ε值不同；目标是找到一段次数后的累计奖励最高的策略；这里展示的策略包括衰减ε-贪婪算法，上置信界算法和汤普森采样`
# 马尔科夫决策过程

马尔科夫决策过程(Markov decision process, MDP)
随机过程(stochastic process)
马尔科夫性质(Markov property)
马尔科夫过程(Markov process)马尔科夫链(Markov chain)
状态转移矩阵(state transition matrix)
终止状态(terminal state)
马尔科夫奖励过程(Markov reward process, MRP)

马尔科夫奖励过程中由 $\langle\mathcal{S},\mathcal{P},r,\gamma\rangle$ 构成，其中$\mathcal{S}$是 **有限** 状态的集合，$P$是状态转移矩阵，$r$是奖励函数，$\gamma$是折扣因子(discount factor)，取值为$[0,1)$。有时候我们希望能尽快获得奖励(尽快到达终止状态)，要对远期利益打折扣。从状态$S_t$到终止状态所有奖励衰减之和称为回报(return)$G_t$，计算如下$G_{t}=R_{t}+\gamma R_{t+1}+\gamma^{2}R_{t+2}+\cdots=\sum_{k=0}^{\infty}\gamma^{k}R_{t+k}$。一个状态的期望回报(从这个状态出发的未来累计奖励的期望)称作状态的价值(value)，所有状态的价值一起组成了价值函数(value funation)，价值函数的输入是状态，输出是这个状态的价值，记作$V(s)=\mathbb{E}[G_{t}|S_{t}=s]$，展开得到$V(s)=\mathbb{E}[R_{t}+\gamma V(S_{t+1})|S_{t}=s]$。式中第一部分是即时奖励的期望正是奖励函数的输出(这里奖励函数是每个状态对应了一个奖励值是离散的)，第二部分从状态的转移概率出发，最后得到$V(s)=r(s)+\gamma\sum_{s^\prime\in S}p(s^\prime|s)V(s^\prime)$，这是马尔科夫奖励过程中最有名的贝尔曼方程(Bellman equation)。写成矩阵形式化简最后得到$\mathcal{V}=(I-\gamma\mathcal{P})^{-1}\mathcal{R}$，这个解析解的计算复杂度是$O(n^3)$，$n$是状态个数，因此这种方法只适合很小的马尔科夫奖励过程，大规模的马尔科夫奖励过程中的价值函数，可以使用动态规划(dynamic programming)算法，蒙特卡洛算法(Monte-Carlo method)和时序差分(temporal difference)。

马尔科夫决策过程由 $\langle\mathcal{S},\mathcal{A},\mathcal{P},r,\gamma\rangle$ 构成，其中$\mathcal{S}$是状态的集合，$\mathcal{A}$是动作的集合，$\gamma$是折扣因子，$r(s,a)$是奖励函数，奖励函数可以同时取决于状态和动作，$P(s^{\prime}|s,a)$是状态转移函数。其中智能体的策略通(policy)常用$\pi$表示，策略分为确定性策略(deterministic policy)和随机性策略(stochastic policy)，用$V^\pi(s)$表示基于策略$\pi$的 **状态价值函数** ，定义为从状态$s$出发遵循策略$\pi$获得的期望回报，记作$V^{\pi}(s)=\mathbb{E}_{\pi}[G_{t}|S_{t}=s]$。由于动作的存在，定义 **动作价值函数** (action-value function)，记作$Q^{\pi}(s,a)=\mathbb{E}_{\pi}[G_{t}|S_{t}=s,A_{t}=a]$。状态价值函数和动作函数之间的关系满足(概率论中全概率公式)$V^\pi(s)=\sum_{a\in A}\pi(a|s)Q^\pi(s,a)$。推导得出 **贝尔曼期望方程** (Bellman expectation equation)，$V^\pi(s)=\sum_{a\in A}\pi(a|s)\left(r(s,a)+\gamma\sum_{s'\in S}p(s'|s,a)V^{\pi}(s')\right)$和$Q^\pi(s,a)=r(s,a)+\gamma\sum_{s^{\prime}\in S}p(s^{\prime}|s,a)\sum_{a^{\prime}\in A}\pi(a^{\prime}|s^{\prime})Q^{\pi}(s^{\prime},a^{\prime})$，价值函数和贝尔曼方程是强化学习的重要组成部分，后续很多算法据此推导而来。如果已知MDP和策略$\pi$，可以通过边缘化(marginalization)得到没有动作的MRP，奖励转换公式为$r^{\prime}(s)=\sum_{a\in\mathcal{A}}\pi(a|s)r(s,a)$，概率转移公式为$P^{\prime}(s^{\prime}|s)=\sum_{a\in\mathcal{A}}\pi(a|s)P(s^{\prime}|s,a)$，这样就构建了一个 $\langle\mathcal{S},P^{\prime},r^{\prime},\gamma\rangle$ 的MRP，再利用解析公式或者其他方法就可以得到状态价值函数。

大规模的马尔科夫过程计算状态价值函数可以使用蒙特卡洛方法，在策略$\pi$下采样若干条序列，计算每条序列的总回报。对于一个状态下的状态价值函数是所有从这个状态出发的序列的总回报的均值(大数定律)，也可以使用期望增量更新公式(相比期望定义公式计算更快)。

用$P_{t}^{\pi}(s)$表示采取策略$\pi$使得智能体在$t$时刻状态为$s$的概率，那么就有$P_{0}^{\pi}(s)=\nu_{0}(s)$，定义状态访问分布(state visitation distribution) 为$\nu^\pi(s)=(1-\gamma)\sum_{t=0}^\infty\gamma^tP_t^\pi(s)$。理论上要把一个状态无穷多个时刻的访问概率都和折扣因子的时间次方做乘积加起来，再乘上使概率为一的归一化因子，但是智能体和MDP交互的序列是有限的。定义占用度量为$\rho^{\pi}(s,a)=(1-\gamma)\sum_{t=0}^{\infty}\gamma^{t}P_{t}^{\pi}(s)\pi(a|s)$，性质有如果两个策略的占用度量相同，那么两个策略等价(占用度量是衡量特定状态动作对的)。

最优策略(optimal policy) 最优状态价值函数 最优动作价值函数
贝尔曼最优方程(Bellman optimality equation)
$V^*(s)=\max_{a\in\mathcal{A}}\{r(s,a)+\gamma\sum_{s^{\prime}\in\mathcal{S}}p(s^{\prime}|s,a)V^*(s^{\prime})\}$
$Q^{*}(s,a)=r(s,a)+\gamma\sum_{s^{\prime}\in S}p(s^{\prime}|s,a)\max_{a^{\prime}\in A}Q^{*}(s^{\prime},a^{\prime})$

`MRP引入了价值函数的概念，MDP引入了贝尔曼期望方程；环境变化的随机过程具有马尔科夫性质，动作影响状态的变化；奖励与动作和改变前环境的状态有关；MDP问题可以通过边缘化转化为MRP问题；大规模的马尔科夫过程的状态价值函数可以通过蒙特卡洛算法获得；占用度量是多个序列中每个时刻到达某一特定状态采取某一特定动作的概率，也需要蒙特卡洛近似估计；最优状态价值是选择最优动作价值最大的动作的状态价值

# 动态规划算法
