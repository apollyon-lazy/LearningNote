### 1、seaborn包中的一些用法
| Function | Syntax | Description | Return |
| :--- | :--- | :--- | :--- |
| sns.set_theme() | | 设置matplotlib和seaborn绘图风格 |
| sns.countplot() | sns.countplot(x,y,order,orient) |用条形图展示每个分类的观察值数 返回Axes对象 |

### 2、Pillow包中的一些用法
| Function | Syntax | Description | Return |
| :--- | :--- | :--- | :--- |
|Image.open()| | 打开并识别文件类型 | Image对象 |

### 3、torchvision的一些用法
- torchvision 支持 PIL image 和 Tensor image 这里使用PIL库处理图片    
A Tensor Image is a tensor with (C, H, W) shape, where C is a number of channels, H and W are image height and width.    
A batch of Tensor Images is a tensor of (B, C, H, W) shape, where B is a number of images in the batch.
| Function | Syntax | Description | Return |
| :--- | :--- | :--- | :--- |
| transforms.Compose(transforms) || 组合一系列图像变换但不支持torchscript    

### 4、wandb的使用
- wandb login 登录wandb<br>
- wandb login --relogin 重新登录wandb<br>

| Function | Description | 
| :--- | :--- |
| wandb.init(project,name,config) | 初始化远端返回一个Run对象,在本地目录保存记录和文件<br>project:工程名 name:试验名 config:配置字典 |
| wandb.config() | 保存超参数组成的字典,例如学习率和模型类型,以方便管理排序结果 |
| wandb.log({xxx}) | 记录一次循环后的指标,例如精度或损失<br>每次调用会为history对象进行一次增加 为summary对象进行一次更新 |
| wandb.image()| 图像的显示 |
| wandb.watch(nn.module)| 连接到torch收集梯度和网络<br>nn.module:网络模型 |
| wandb.finish()|结束远端 |

- history 一组类似字典的数组 会随次数跟踪指标 次数序列在UI中显示为折线图
- summary 默认返回指标最终值 可设置更改为中间过程最优值 同样可以对不同项目最终精度进行比较
- 自动记录的信息有： **系统指标** CPU GPU利用率等 **命令行** 标准输出(stdout)错误(stderr) **代码和依赖文件(.txt等)** 可设置上传<br>
- 需要调用函数记录的信息有：**样本数据**  **梯度**(直方图) **配置信息**  **指标**<br>


```python

```
