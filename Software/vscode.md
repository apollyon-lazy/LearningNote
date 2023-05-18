# Vscode trick

## Shortcuts

<kbd>ctrl</kbd> + <kbd>,</kbd> 打开 Settings 页面
<kbd>ctrl</kbd> + <kbd>`</kbd> 打开(返回)终端
<kbd>ctrl</kbd> + <kbd>P</kbd> 查找文件
<kbd>ctrl</kbd> + <kbd>shift</kbd> + <kbd>P</kbd> 命令行工具

<kbd>ctrl</kbd> + <kbd>K</kbd> <kbd>V</kbd> 打开预览窗口
<kbd>ctrl</kbd> + <kbd>L</kbd> 选中当前行

<kbd>ctrl</kbd> + <kbd>/</kbd> 单行注释
<kbd>alt</kbd> + <kbd>shift</kbd> + <kbd>A</kbd> 多行注释

<kbd>ctrl</kbd> + <kbd>K</kbd>，<kbd>ctrl</kbd> + <kbd>J</kbd> 展开所有代码
<kbd>ctrl</kbd> + <kbd>K</kbd>，<kbd>ctrl</kbd> + <kbd>0</kbd> 折叠所有代码

<kbd>alt</kbd> + <kbd>MouseL</kbd> 插入多个光标
<kbd>alt</kbd> + <kbd>Up</kbd>/<kbd>Down</kbd> 移动当前整行
<kbd>alt</kbd> + <kbd>shift</kbd> + <kbd>Up</kbd>/<kbd>Down</kbd> 复制当前整行

## User and Workspace Settings

当你打开一个工作空间（Workspace），你至少会看到两个作用域：  
User Settings: 全局地作用于任何 VScode 打开的实例；  
Workspace Settings: 工作空间设置保存在工作空间内，并只作用于打开的工作空间。  

每个设置的齿轮图标（gear icon）都提供了重置设置（Reset Setting）到默认值的选项。

设置同步（Setting Sync）使你能够共享设置，比如键盘快捷键（keyboard shortcuts），安装的扩展插件设置等等。使能设置同步，在你登录 Microsoft 账号或是 Github 账号后都会持续自动的同步你的偏好（perferences）。


## Workspace

在同一工作空间下（Workspace）可以包含多个相关项目的文件（Multi-root Workspace），当然如果只有一个文件夹的的话没必要使它成为一个工作空间（Single-folder Workspace）。当保存工作空间后，会创建一个`.code-workspace`文件，这个文件可以添加适用于工作空间中所有文件夹的设置。设置中`"folder"`对应工作空间中每个文件夹的名字`"name"`及其相对路径`"path"`。`"setting"`影响整个工作空间，不支持的设置语句会灰色报错显示。
