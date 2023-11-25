![[qt_mvc.jpg]]

模型与视图
- 通常情况下重载的函数有 rowCount(传递父索引返回行数) columnCount(传递父索引返回列数) data(传递索引角色返回数据) index(传递行列和父索引返回子索引) parent(返回父索引) 
- QVector QMap QStringList用来存储我们想要保存的数据，而继承QAbstractItemModel抽象类则是通过重载五个纯虚函数来实现底层数据的层次关系，这样的关系可以是列表，表格或者是树
- 如果要对存储的底层数据修改，可以重载 setDate(传递角色索引和值) setHeaderDate(设置表头数据)
[QT模型视图MVC系列教程（2）-模型数据索引QModelIndex详解_暴躁的野生猿的博客-CSDN博客](https://blog.csdn.net/qq_31073871/article/details/113525678)


CH801将电脑路径中的文件信息用TreeView ListView TableView用三种视图展现了出来
- 使用了已有的Model(QDirModel)，重点放在Model/View的概述上
- 展示了View的setSelectionModel函数的用法
- 展示了treeView的doubleClicked(QModelIndex)的信号
- 展示了listView和tableView的setRootIndex能改变根节点索引的槽函数
CH802将QVector QMap QStringList中保存的数据存入模型并在TableView中显示
- Model/View中都有ModelIndex相关联，可以直接把模型放入视图，重点放在Model上
- 用Map建立键值对，将重复出现的字符串用数字标识化
- 重载data函数，根据ModelIndex和Role可以找到在QVector或QMap或QStringList中的数据
- 代码中并未存在给数据添加ModelIndex的操作，猜测是已经足够与视图关联

