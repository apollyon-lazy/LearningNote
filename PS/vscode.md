# Vscode trick

## Workspace

在同一工作空间下（Workspace）可以包含多个相关项目的文件（Multi-root Workspace），当然如果只有一个文件夹的的话没必要使它成为一个工作空间（Single-folder Workspace）。当保存工作空间后，会创建一个`.code-workspace`文件，这个文件可以添加适用于工作空间中所有文件夹的设置。设置中`"folder"`对应工作空间中每个文件夹的名字`"name"`及其相对路径`"path"`。`"setting"`影响整个工作空间，不支持的设置语句会灰色报错显示。
