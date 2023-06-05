# packages

包含在 anaconda 中的重要的包有 
- numpy(数值运算库) 
- pandas(数据处理库) 
- matplotlib(基础可视化库)  
- scipy(科学计算库)
- seaborn(高级可视化库) 
- scikit-learn(流行的机器学习库)
- sympy(科学计算库) 

Python标准库 中常用的还有
- re(正则表达式库)
- datatime(基本日期与时间库)
- math(数学计算库)
- os(操作系统库)
- time(时间访问转换库)
- json(josn编码解码库)
- unittest(测试用例库)

其余还用过的有：  
- control(控制领域库) —— DHC2-beaver项目
- tqdl(进度条库) wandb(轻量级观测平台库) —— 深度学习项目  


# brief introduction

- Numpy 是最为流行的机器学习和数据科学包，Numpy包支持在多维数据上的数学运算，提供数字支持以及相应高效的处理函数，很多更高级的扩展库（包括Scipy、Matplotlib、Pandas等库都依赖于Numpy库）；
- Scipy 包用于科学计算，提供矩阵支持，以及矩阵相关的数值计算模块，其功能包含有最优化、线性代数、积分、插值、拟合、信号处理和图像处理以及其他科学工程中常用的计算；
- Pandas 用于管理数据集，强大、灵活的数据分析和探索工具，其带有丰富的数据处理函数，支持序列分析功能，支持灵活处理缺失数据等；
	- Pandas基本的数据结构是Series和DataFrame；
	- Series就是序列，类似一维数组；
	- DataFrame相当于一张二维的表格，类似二维数组，它的每一列都是一个Series；
	- 为了定位Series中的元素，Pandas提供了Index对象，每个Series都会带有一个对应的Index，用来标记不用的元素；
	- DataFrame相当于多个带有同样Index的Series的组合（本质是Series的容器）；
- Matplotlib 库用于数据可视化，强大的数据可视化工具以及作图库，其主要用于二维绘图，也可以进行简单的三维绘图；
- Seaborn 库是基于Matplotlib的高级可视化库；
- Scikit-learn 库包含大量机器学习算法的实现，其提供了完善的机器学习工具箱，支持预处理、回归、分类、聚类、降维、预测和模型分析等强大的机器学习库，近乎一半的机器学习和数据科学项目使用该包。