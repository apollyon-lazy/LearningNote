# 图

## 无向图的邻接表

![[graph1.png]]
## 有向图的邻接表

![[graph2.png]]

## 图的建立（邻接表）

``` Python
class VertexNode(object):   #顶点表节点  
    def __init__(self,vertexname,visited=False,p=None):
        self.vertexName =vertexname #节点名字
        self.Visited=visited        #此节点是否被访问过
        self.firstNode = p          #指向所连接的边表节点的指针（EdgeNode）
```

``` Python
class EdgeNode(object):     #边表节点
    def __init__(self,index,weight,p=None):
        self.Index =index   #尾节点在边表中对应序号
        self.Weight=weight  #边的权值   
        self.Next = p       #链接同一头节点的下一条边
```

``` Python
class Adgraph(object):
    def __init__(self, vcount=0):
        self.vertexList = []  # 用list链接边表
        self.vertexCount = vcount # 顶点个数

    def initlist(self, data):  # 初始化
        for da in data:
            A = VertexNode(da)
            self.vertexList.append(A) # 初始化顶点表
        self.vertexCount = len(data) # 初始化顶点个数 

    def GetIndex(self, data):  # 获取指定名称的节点的序号
        for i in range(self.vertexCount):
            temp = self.vertexList[i].vertexName
            if (temp != None) and (data == temp):
                return i
        return -1

    def AddEdge(self, startNode, endNode, weight):  # 添加边的信息
        i = self.GetIndex(startNode)
        j = self.GetIndex(endNode)
        if i == -1 or j == -1:
            print("不存在该边")
        else:
            weight = float(weight)
            temp = self.vertexList[i].firstNode
            if temp == None:  # 若边表下无顶点信息
                self.vertexList[i].firstNode = EdgeNode(j, weight)
            else:  # 若边表下已有顶点信息
                while (temp.Next != None):
                    temp = temp.Next
                temp.Next = EdgeNode(j, weight)
```

## 图的遍历（深度优先）

从起点顶点沿着边表出发，发现有没访问的顶点，就沿着这个顶点的边表往前走，把走过的顶点设为已访问，走不了就退回上一个访问的顶点继续走。

## 图的遍历（广度优先）

图的广度优先遍历类似于二叉树的层序遍历，从根节点开始，先把这一个节点加入一个先进先出的队列，然后沿着此节点的边表访问其链接的没被访问的节点并加入队列，然后此节点退队,再取队首元素边表逐一访问，如果发现队列为空，则演算终止。

``` Python
def DFS(self, i):  # 深度优先搜索递归
    self.vertexList[i].Visited = True
    result = self.vertexList[i].vertexName+'\n'
    p = self.vertexList[i].firstNode
    while (p != None):
        if self.vertexList[p.Index].Visited == True:
            p = p.Next
        else:
            result += self.DFS(p.Index)
    return result

def DFStravel(self, start):  # 深度优先搜索入口
    i = self.GetIndex(start)
    if i != -1:
        for j in range(self.vertexCount):
            self.vertexList[j].Visited = False
        DFSresult = self.DFS(i)
    return DFSresult

def BFStravel(self,start):  #广度优先搜索
    BFSresult=''
    i=self.GetIndex(start)
    if i!=-1:
        for j in range(self.vertexCount):
            self.vertexList[j].Visited=False 
        self.vertexList[i].Visited=True
        BFSresult+=self.vertexList[i].vertexName+'\n'
        GList=[i]                   #记录遍历顺序(用list代替队列)
        while(GList!=[]):
            j=GList.pop(0)
            p=self.vertexList[j].firstNode
            while p!=None:
                k=p.Index
                if (self.vertexList[k].Visited==False):
                    self.vertexList[k].Visited=True
                    BFSresult+=self.vertexList[k].vertexName+'\n'
                    GList.append(p.Index)
                p=p.Next
    return BFSresult
```

## 最小生成树(Prim算法、Kruskal算法)

**Prim算法思路**：所有结点分成两个group，一个为已经选取的Select，一个为未选的Candidate。
首先将已给的一个结点加入到Select，然后遍历头结点在Select、尾结点在Candidate的边，选取符合这个条件的边里面权重最小的边，加入到最小生成树，选出的边的尾节点加入到Select，并从Candidate删除。重复此操作直到Candidate中没有节点。需要注意的是，循环开始前要保证所有节点都有边连接，否则可能会有节点一直在Candidate中，导致死循环。

**Kruskal算法思路**：先对边按权重从小到大排序，初始每个结点都是一个单独的连通分量。先选取权重最小的一条边，如果该边的两个节点处于不同的连通分量，则该边可以加入到最小生成树，并将这两个连通分量合并（节点放入一个列表），否则计算下一条边（判断新边的两个节点是否在同一列表中，若在同一列表中表明两节点在同一连通分量中），直到遍历完所有的边。

``` Python
def GetWeight(self,begin,end):      #获取两结点之间边的权值
    wei=10000 # 设置不存在的边的权值
    p=self.vertexList[begin].firstNode
    if p!=None:
        if p.Index==end:
            wei=p.Weight
        else:
            while p.Next!=None:
                p=p.Next
                if p.Index==end:
                    wei=p.Weight
    return wei
    
def MiniSpanTree_prim(self,vName):  #最小生成树-prim
    i=self.GetIndex(vName) 
    if i==-1:
        return None
    for i in range(self.vertexCount):       #判断是否有没有边链接的节点
        if vertexList[i].firstNode==None:
            return None
    wsum=0
    Spantree=[]                     #最小生成树
    Select=[]                       #已选择节点
    Candidate=[]                    #未选择节点
    for i in range(self.vertexCount):   #初始所有节点都在Candidate中
        Candidate.append(i)
    Select.append(i)                #将根节点移入Select
    Candidate.remove(i)
    
    while len(Candidate)>0:
        [begin,end,minweight]=[-1,-1,9999] # 不存在的边权值为10000
        for i in Select:
            for j in Candidate:
                if self.GetWeight(i,j)< minweight:  
                    minweight = self.GetWeight(i,j)
                    begin = i
                    end = j
        Spantree.append([begin, end, minweight])    #找出链接两节点集权值最小的边并加入
        wsum+=minweight
        Select.append(end)
        Candidate.remove(end)
    
    spanstr="最小生成树总权值："+str(wsum)+'\n'     #整理输出
    Spantree = Spantree[::-1] 
    for node in Spantree:
        spanstr+=self.vertexList[node[1]].vertexName+"->"
        spanstr+=self.vertexList[node[0]].vertexName+'\n'
        spanstr+="     weight:"+str(node[2])+'\n'
    return spanstr

def MiniSpanTree_kruskal(self):   #最小生成树-kruskal
    vertexSort=[]
    for i in range(self.vertexCount):               #整理出当前树的边集(i<j)
        for j in range(self.vertexCount-i):
            weight=self.GetWeight(i,i+j)
            if weight<9999:                         #利用GetWeight函数鉴定两节点间是否有边
                vertexSort.append([i,i+j,weight])   #生成边集数组[起点结点，终点结点，权重]
    vertexSort.sort(key=lambda a:a[2])              #对边集中的边进行排序
    
    Spantree=[]
    wsum=0
    trees = [[i] for i in range(self.vertexCount)]  #所有树的集合
    for edge in vertexSort:
        tree1=edge[0]               
        tree2=edge[1]
        for i in range(len(trees)):
            if tree1 in trees[i]:   #获取两节点分别所在的树
                tree1 = i
            if tree2 in trees[i]:
                tree2 = i
        if tree1 != tree2:          #若两结点不在同一棵树上，链接两棵树
            Spantree.append(edge)
            wsum+=edge[2]
            trees[tree1] = trees[tree1] + trees[tree2] # 边两结点合并到一个列表中，即放在一棵树上
            trees[tree2] = [] 
    
    spanstr="最小生成树总权值："+str(wsum)+'\n'         #整理输出
    for node in Spantree:
        spanstr+=self.vertexList[node[0]].vertexName+"->"
        spanstr+=self.vertexList[node[1]].vertexName+'\n'
        spanstr+="     weight:"+str(node[2])+'\n'
    return spanstr
```

## 最短路径：Dijkstra算法、Floyd算法

**Dijkstra算法** Dijkstra是一种贪心算法，是以图中一个点作为源点，该源点到其他各个点的最短路径的算法。源点是固定不动的，代码中用dst一维数组记录源点到第k个顶点的最短路径。每次找到离源点最近的一个顶点u，然后拿这个顶点u进行更新dst数组(即 $dst[k]=min(dst[k],dst[u]+edge[u][k])$ ，直至所有顶点被遍历。

**Floyd算法** Floyd算法是经典的动态规划算法，基本思想是递推产生一个邻接矩阵序列$A_1,A_2,.....,A_k,...,A_n$（图有n个节点），$A_k=(a_k(i,j))_{nxn}$。其中矩阵Ak第i行第j列表示从顶点vi到顶点vj的路径上经过的顶点序号不大于k的最短路径长度。$a_k(i,j)=min \{a_{k-1}(i,j),a_{k-1}(i,k)+a_{k-1}(k,j)\}$。如果需要记录路径，那么需要引入路由矩阵。路由矩阵$R_k=(r_k(i,j))_{nxn}$,用来记录两点之间路径的前驱后继的关系，其中$r_k(i,j)$表示从顶点vi到顶点vj的路径经过编号为$r_k(i,j)$的顶点。

Dijkstra算法解决了单源点到其余所有顶点的最短路径问题。
Floyd算法解决了多源点到其余所有顶点的最短路径问题。
