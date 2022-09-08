### torch框架中的一些基本用法
- **定义模型** 继承nn.Module类，构造自定义块，自定义顺序层
- **定义数据集** 集成继承data.dataset类，构造自定义数据集

#### 1、张量函数
| Function | Description | Return |
| :--- | :--- | :--- |
| Tensor.shape() |  访问张量沿每个轴的形状 |
| Tensor.size()\/numel() |  访问张量所有元素个数 |
| Tensor.reshape() | 重塑张量的形状 |
| Tensor.detach() | 分离参数为常数 |
| Tensor.clone(A) | 通过分配新内存将A的副本给B |
| Tensor.to(dtype, device) | 执行类型和设备转换 |
| Tensor.argmax(dim) | 返回张量a元素最大值下标 | tensor |

#### 2、张量运算
| Function | Description | Return |
| :--- | :--- | :--- |
| torch.tensor() | 创建一个张量 |
| torch.zeros/ones() |生成全零/一张量 |
| torch.randn() | 生成0-1高斯分布的随机张量 |
| torch.arange() |生成序列张量 |
| torch.exp() | 张量求指数 |
| torch.log() | 张量求自然对数 |
| torch.cut((X,Y),dim) | 张量连结<br> dim=0：以行为整体堆叠连结<br>dim=1：以列为整体拼接连结 |
| torch.zero_like(Y) | 生成一个形状相同的全零张量 |
| torch.numpy() | torch张量(tensor)转换为numpy张量(ndarray) |
| torch.sum(axis) | 张量求和降维<br>axis用法同dim |
| torch.dot(x,y) | 向量点积<br>按照元素乘积求和 |
| torch.mv(A,x) | 矩阵和向量积<br>矩阵每个列向量与行向量做点积 |
| torch.mm(A,B) | 矩阵乘法<br>矩阵向量积以列为整体拼接 |
| torch.matmul(A,B) | 张量相乘，如果维度不一致会使用广播机制 |
| torch.normal(miu,sigma,shape) | 生成正态分布的随机数 |
| torch.argmax(a) |返回张量a元素最大值下标 | tensor |
| torch.clamp(input,min,max) | 对数据进行上下界加窗 |
| torch.device('cpu'/'cuda'/'cuda:1') |分别表示CPU、GPU0、GPU1 |
| torch.save(obj,f) | 把obj保存到f 通常张量数据保存为.pt文件 |
| torch.load(path) | 加载path保存的模型或者参数 |

#### 3、张量初始化

| Function | Description | Return |
| :--- | :--- | :--- |
| nn.init.uniform_(tensor,a,b) | 用U(a,b)均匀分布填充张量 |
| nn.init.normal_(tensor,mean,std) | 用N(mean,std^2)正态分布填充张量 |
| nn.init.normal_(tensor,val) | 用变量val填充张量 |
| nn.init.xavier_uniform_(tensor) | 用Xavier均匀分布初始化张量(尽可能让方差保持不变)|
| nn.init.xavier_normal_(tensor) | 用Xavier正态分布初始化张量

#### 4、网络层

| Function | Syntax | Description |
| :--- | :--- | :--- |
| nn.Flatten() | | 展平层(默认前两维) |
| nn.Dropout() | nn.Dropout(dropout) | 暂退层 | 
| nn.Relu() | | Relu激活层 |
| nn.Linear() | nn.Linear(in_features,out_features,bias) |线性层 |
| nn.Conv2d() | nn.Conv2d(input_channel.output_channel,kernel_size,stride,padding) | 卷积层  |
| nn.MaxPool2d() | nn.MaxPool2d(kernel_size, stride padding) | 最大汇聚层<br>默认汇聚窗口与步幅大小相同 |
| nn.AvgPool2d() | nn.AvgPool2d(kernel_size, stride padding) | 平均汇聚层<br>默认汇聚窗口与步幅大小相同 |
| nn.Batchnorm() | nn.Batchnorm(num_features,num_dims) | 批量规范化层<br>训练和评估模式不一样，常用于深度卷积网络 |

| Function |  Description | Return |
| :--- |  :--- | :--- |
| nn.Module.to(device)  | 移动模型到device |
| nn.Module.apply(fn) | 递归给每个子模型使用函数fn，常用于参数初始化 |
| nn.Module.eval() | 设置模型为评估模式 |
| nn.Module.train() | 设置模型为训练模式 |
| nn.Module.state_dict() | 返回权重和偏差参数 | OrderedDict |
| nn.Module.load_state_dict(state_dict) | 把参数加载入模型 |
| nn.Module.modules() | 返回迭代器覆盖网络所有模型 |
| nn.Module.requires_grad_() | 打开参数的自动梯度更新 |
| nn.Module.parameter() | 返回迭代器覆盖所有变量，常用于传递参数给优化器 |

- P195  参数管理：参数是符合的对象，包含值、梯度和额外信息  
nn.Module.weight/bias(.data) 访问模型权重或偏差(的数据部分)

#### 5、损失函数

| Function | Syntax | Description | Return |
| :--- | :--- | :--- | :--- |
| nn.MSELoss() | nn.MSELoss(reduction) | 最小均方误差(MSE)指标默认求均值<br> reduction:sum默认平方后求均值 | class |
| nn.CrossEntropyLoss() | | 交叉熵损失<br>函数开头已经集成了softmax回归 |

#### 6、优化函数

| Function | Syntax | Description | Return |
| :--- | :--- | :--- | :--- |
| torch.optim.SGD() | SGD(net.parameters(),lr,weight_decay) | 随机梯度下降<br>net.parameters():传递模型参数  | 
| torch.optim.Adam() | Adam(net.parameters(),lr,weight_decay) | 和Adam算法<br>lr：学习率 weight_decay：权重衰退比例 |
| torch.optim.zero_grad() | |清零梯度 |
| torch.optim.step() | | 更新参数 |

#### 7、数据加载

| Function | Syntax | Description | Return |
| :--- | :--- | :--- | :--- |
| torch.utils.Dataloader() | Dataloader(data,batch_size,shuffle,num_workers) | 加载数据集 | class |
| --- | --- | data:数据 batch_size:批量大小 shuffle:是否打乱 num_workers:进程数 |