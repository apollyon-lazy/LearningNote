## Anaconda
Anaconda 包括 Conda、Python 以及一大堆安装好的工具包，比如 numpy 和 pandas等。安装 anaconda 的好处主要为以下几点：
1. 包含conda
conda是一个环境管理器，其功能依靠conda包实现，该环境管理器与pip相似。可以认为 conda 和 pip 分别是 python 和 anaconda 的包管理工具。这里需要对 conda install xxx 命令和 pip install xxx 进行区别。

- **conda install xxx**
这种方式安装的库都会放在 `anaconda3/pkgs` 目录下，这样的好处就是，当某个环境下已经下载好了某个库，再在另一个环境中还需要这个库时，就可以直接从 pkgs 目录下将该哭复制到新环境而不用重复下载。

- **pip install xxx**
分两种情况，一种情况是当前 conda 环境中的 python 是 conda 安装的，和系统的不一样，那么xxx会被安装到 `anaconda3/envs/current_env/Lib/site-packages` 文件夹中，如果当前 conda 用的是系统的 python，那么 xxx 会通常被安装到系统 python 文件夹中。

2. 安装大量工具包
anaconda 会自动安装一个基本的 python ,该 python 的版本与 anaconda 的版本有关。该 python 下已经安装好了一大堆工具包，对于科学计算分析是易达便利。

3. 可以创建、使用和管理多个不同的 python 版本管理
在 anaconda prompt 命令提示符下(Windows环境)：
`conda --version` 查看 python 版本
`python -- version` 查看 anaconda 中基础 python 版本
`conda` `conda list` `conda info` 可以用于检查安装是否正确
`conda config --show-sources` 查看已添加的镜像源
`conda env list` `conda info -e` 产看当前存在的虚拟环境
`conda create -n \<envname> python=X.X` 创建虚拟环境
 

