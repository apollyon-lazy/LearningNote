《大话数据结构》CSDN 比较全的笔记
https://blog.csdn.net/weixin_44571010/article/details/115677735
## 提纲
#### 数据结构绪论
1. 数据、数据元素、数据项、数据对象、数据结构
2. 数据结构分为逻辑结构和物理结构
3. 抽象数据类型
```
ADT 抽象数据类型名
Data 
	数据元素之间逻辑关系的定义
Operation
	操作1
		初始条件
		操作结果描述
	操作2
		……
	操作n
		……
endADT
```
#### 算法
1. 算法、算法的特性、算法设计的要求、算法效率的度量方法、函数的渐进增长
2. 时间复杂度、推导大O阶
- O($1$) < O($logn$) < O($n$) < O($nlogn$) < O($n^2$) < O($n^3$) < O($2^n$) < O($n!$) < O($n^n$)
3. 平均时间复杂度、最坏时间复杂度、空间复杂度
#### 线性表
1. 线性表
2. 顺序存储结构、链式存储结构（单链表）
3. 静态链表、循环链表、双向链表

```
ADT 线性表（List）
data 
	线性表的数据对象集合为{a1,a2,...,an}，每个元素类型为DataType。除第一个和最后一个元素之外，每个元素都有一个直接前驱元素和直接后继元素。数据元素之间是一对一的关系。
Operation
	InitList(*L):			初始化操作，建立一个空的线性表L
	ListEmpty(L):			若线性表为空，返回true，否则返回false
	ClearList(*L):  		将线性表清空
	GetElem(L, i, *e):		将表中第i个位置上的元素返回给e
	LocateElem(L, e):		在线性表中查找与e相等的值。查找成功，返回元素序号；否则返回0
	ListInsert(*L, i, e):	在第i个位置插入元素e
	ListDelete(*L, i, *e):	删除表中第i个元素，并用e返回值
	ListLength(L):			返回线性表中的元素
endADT
```

| | 顺序存储结构 | 链式存储结构（单链表） |
|:---:|:---:|:---:|
| 时间性能 | 查找：O(1)<br>插入和删除：O(n) | 查找：O(n)<br>插入和删除：再找出某位置的指针后，O(1) |
| 空间性能 | 需要预分配空间，分大了浪费，分小了容易发生上溢 | 不需要预分配空间，只要有就可以动态分配，元素个数不受限制 |
| 适用场合 | 频繁查找，很少插入和删除 | 频繁插入和删除，元素个数较大或者不确定 | 

#### 栈与队列
1. 栈(stack)、入栈(push)、出栈(pop)、后进先出(LIFO)
   - 栈的顺序存储结构、两栈共享空间
   - 栈的链式存储结构
   - 栈的应用：递归、四则运算表达式求值
   - 时间复杂度：入栈和出栈 O(1)、查找 O(n)
2. 队列(queue)、入队(enqueue)、出队(dequeue)、先进先出(FIFO)
   - 队列的顺序存储结构：循环队列
   - 队列的链式存储结构：链队列
   - 时间复杂度：入队和出队 O(1)、查找 O(n)
> 在高级语言中，线性表、树、图等是可以使用数组列表、链表集合、类等写法搭建的！

#### 字符串
1. 字符串、串的顺序存储结构、串的链式存储结构
2. 朴素的模式匹配法、KMP模式匹配算法
```
ADT 串(string)
Data 
	串中元素仅由一个字符组成，相邻元素具有前驱和后继的关系。
Operation 
	StrAssign(T, *chars): 生成一个其值等于字符串常量chars 的串T
	StrCopy(T, S): 串S存在，由串S复制给T
	ClearString(S): 将串清空
	StringEmpty(S): 判断是否为空
	StrLength(S): 返回串的元素个数
	StrCompare(S, T): 若S>T，返回值>0；若S=T，返回值等于0；若S<T，返回值<0；
	Concat(T, S1, S2): 用T返回由S1和S2连接形成的新串
	SubString(Sub, S, pos, len): 串S存在。1<= pos <= StrLength(S),且0 <= len <= StrLength(S) - pos + 1,用Sub返回串S的第pos个字符起长度为len的子串
	Index(S, T, pos): 串S、T存在，T是非空串，1 <= pos <= StrLength(S)。若主串S中存在和串T值相同的子串，则返回它在主串S中第pos个字符出现之后第一次出现的位置，否则返回0
	Replace(S, T, V):串S,T,V存在，T是非空串。用V替代主串S中出现所有与T相等的不重叠的子串
	StrInsert(S, pos, T): 串S，T存在，1 <= pos <= StrLength(S) + 1。在串S的第pos个字符前插入串T
	StrDelete(S, pos, len):串S存在，1 <= pos <= StrLength(S) -len + 1。从串S中删除第pos个字符起长度为len的子串
endADT
```
#### 树
1. 树(tree)、根结点(root)、叶结点(leaf)、度(degree)、孩子(child)、双亲(parent)、兄弟(sibling)、层次(level)、深度(depth)、森林(forest)
2. 二叉树(binary tree)、斜树、满二叉树、完全二叉树
- **二叉树的性质**
   - 在二叉树中的第 i 层上至多有 $2^{i-1}$ 个结点(i>=1)
   - 深度为k的二叉树至多有 $2^k-1$ 个结点
   - 对任何一棵二叉树T，如果其终端结点数为 n0 ，度为 2 的结点数为 n2，则 n0 = n2 + 1
   - 具有 n 个结点的完全二叉树的深度为 $[log_2n]+1$ ([x]表示不大于 x 的最大整数)
   - 如果对一棵有 n 个结点的完全二叉树的结点按层序编号，对任意结点 i 有
     - 如果 i=1，则i是二叉树的根，无双亲；如果 i>1，则双亲为 i/2 向下取整
     - 如果 2i>n，则结点i是叶子结点，否则其左孩子是结点 2i
     - 如果 2i+1>n， 则结点i是叶子结点，否则其右孩子为 2i+1
3. 二叉树的顺序存储结构（一般只用于完全二叉树）、二叉链表（双指针分别指向左右孩子）
4. 遍历二叉树（递归）：前序遍历、中序遍历、后序遍历、层序遍历
- **二叉树的遍历**
   - 前序遍历和中序遍历可以唯一确定一颗二叉树
   - 后序遍历和中序遍历可以唯一确定一颗二叉树
   - 前序遍历和后序遍历无法唯一确定一颗二叉树
5. 二叉树的建立（扩展二叉树）、线索二叉树、数与二叉树的互相转换、森林与二叉树的互相转换、遍历森林、霍夫曼树(无损压缩)

```
ADT 树(tree)
Data 
	树是由一个根结点和若干棵子树构成的。树中结点具有相同的数据类型及层次关系。
Operation
	InitTree(*T) :构造空树T
	DestroyTree(*T): 销毁树
	CreateTree(*T, definition):按definition中给出树的定义来构造树
	ClearTree(*T): 清空树
	TreeEmpty(*T): 空树返回true
	TreeDepth(*T): 返回T的深度
	Root(*T): 返回T的根结点
	Value(T, cur_e): cur_e是树T中的一个结点，返回此结点的值
	Assign(T, cur-e, value): 给树T的结点cur_e赋值为value
	Parent(T, cur_e): 若cur_e不是根结点，则返回它的双亲
	LeftChild(T, cur_e): 若cur_e是树T的非叶结点，则返回它的最左孩子，否则返回空。
	RightSibling(T, cur_e): 若cur_e有右兄弟，则返回右兄弟，否则返回空。
	InsertChild(*T, *p, i, c):其中p指向树T的某个结点，i为所指结点p的度加上1，若非空树c与T不相交，操作结果为插入c为树T中p指向结点的第i棵子树。
	DeleteChild(*T, *p, i): 其中p为指向树T的某个结点，i为所指结点p的度，操作结果为删除T中P所指向结点的第i棵子树。
endADT
```

#### 图
1. 图
   - 图按照有无方向分为**无向图（Undirected graphs）**和**有向图（Directed graphs）**。无向图由**顶点（vertex）和边（Edge）** 构成，有向图由**顶点和弧（Arc）** 构成。
   - 图按照边或弧的多少分为**稀疏图**和**稠密图**。如果任意两个顶点之间都存在边叫做**完全图**，有向的叫**有向完全图**。若无重复边或顶点到自身的边则叫**简单图**。
   - 图中顶点之间有**邻接点**、**依附**的概念。无向图顶点的边数叫做**度（Degree）**，有向图顶点分为**入度（InDegree）** 和**出度（OutDegree）**。
   - 图上的边或弧上带**权（Weight）** 则称为**网（Network）**。
   - 图中顶点间存在**路径（Path）**，两顶点存在路径则说明是**连通**的，如果路径最终回到起始点称为**环（Cycle）**，当中不重复叫**简单路径**。若任意两顶点都是连通的，则图是**连通图（Connected Graph）**，有向则称**强连通图**。图中有子图，若子图极大连通则就是**连通分量**，有向则称**强连通分量**。
   - 无向图中连通且 n 个顶点 n-1 条边叫**生成树**。有向图中一顶点入度为 0 ，其余顶点入度为 1 的叫**有向树**。一个有向图由若干有向树构成**生成森林**。
2. 图的存储结构：邻接矩阵储存方式（由一个顶点数组和一个邻接矩阵组成（Adjacency Matrix））、邻接表（Adjacencty List）、十字链表（Orthogonal List）、邻接多重表、边集数组
3. **图的遍历**：深度优先遍历（Depth_First_Search, DFS）、广度优先遍历（Breadth_First_Search, BFS）
4. **最小生成树**（Minimum Cost Spanning Trees）:Prim算法、Kruskal算法
5. **最短路径问题**：Dijkstra算法、Floyd算法
6. 拓扑排序：AOV（Activity On Vertex Network）网、关键路径：AOE（Activity On Edge Network）网

```
ADT 图(Graph)
Data
    顶点的有穷非空集合和边的集合
Operation
    CreateGraph(*G, V, VR)：按照顶点集 V 和边弧集 VR 的定义构造图 G
    DestroyGraph(*G)：图 G 存在则销毁
    LocateVex(G, u)：若图 G 中存在顶点 u， 则返回图中的位置
    GetVex(G, v)：返回图 G 中顶点 v 的值
    PutVex(G, v, value)：将图 G 中顶点 v 赋值 value
    FirstAdjVex(G, *v)：返回顶点 v 的一个邻接顶点， 若顶点在 G 中无邻接顶点返回空
    NextAdjVex(G, v, *w)：返回顶点 v 相对于顶点 w 的下一个邻接顶点，若 w 是 v 的最后一个邻接点则返回空
    InsertVex(*G, v)：在图 G 中增添新节点 v
    DeleteVex(*G, v)：删除图 G 中顶点 v 及其相关的弧
    InsertArc(*G, v, w)：在图 G 中增点弧 <v, w>， 若 G 是无向图，还需要增添对称弧 <w, v>。
    DeleteArc(*G, v, w)：在图 G 中删除弧 <v, w>，若 G 是无向图，则还需要删除对称弧 <w, v>。
    DFSTraverse(G)：对图 G 中进行深度优先遍历，在遍历过程对每个顶点调用
    HFSTraverse(G)：对图 G 中进行广度优先遍历，在遍历过程对每个顶点调用
endADT

```

#### 查找
#### 排序
#### 思考
- [x] 排序和查找知识点多，后续有时间再展开