# git

git version  查看版本
git config --global user.name "用户名" &emsp; 配置用户名  
git config --global user.email "邮箱名" &emsp; 配置邮箱名  

git init &emsp; 初始化  
git status &emsp; 更新状态  
git add 文件名 &emsp; 添加文件到 git 版本控制系统中  
git add .  &emsp; 添加当前目录下所有文件  
git commmit -m "提交说明" &emsp; 提交版本说明  
git log  &emsp; 查看提交到本地的版本信息  
git reset --hard 提交编号 &emsp; 回退到某一版本并删除后续版本  

``` markdown
代码上传远端五个必要命令 git status/git add/git commit/git pull/git push 
git init 命令会在当前目录创建一个 .git 的文件夹，文件夹中会保存每个 git 版本变化和记录！   
git status 命令显示哪些更改是被放到暂存区（staged）将会提交的,以避免错误提交！  
git add 命令把修改文件放入暂存区！
git commit 命令将把暂存区修改保存为一个版本，建议使用后跟 -m 的命令，否则会进入vim编译器    
git commmit -m "fix(test):change content" 是一个规范提交说明的例子，这里fix是修改，括号里test是文件名，冒号后面跟修改内容。 
```

git branch 分支名 &emsp; 创建分支  
git branch &emsp; 查看本地分支  
git branch -a &emsp; 查看所有分支  
git checkout 分支名 &emsp; 切换分支  
git checkout -b 分支名 &emsp; 创建并切换到一个新分支  
git merge 分支名 &emsp; 合并分支到当前分支  
git branch -m 分支名 &emsp;  修改当前分支名  
git branch -d 分支名 &emsp;  删除本地分支  

``` markdown
如果是想把最终敲定版本上传到远端，使用 git push 提交到远端分支！  
如果是想保存代码书写到了某个节点，使用 git add 和 git commit 提交版本！  
如果是想回退到曾经的某个代码版本，使用 git reset --hard 命令！  
如果是想书写并比对不同版本的代码，使用 git branch 创建本地分支！  
```

git remote add 远端名 仓库链接 &emsp;  设置远端链接  
git remote rm 远端名 &emsp; 删除远端链接  

git pull &emsp; 拉取远端代码与本地分支合并  
git push &emsp; 上传同名远端分支  
git push HEAD:\<branchname> &emsp; 上传远端分支  
git clone 仓库链接 . &emsp; 在目录下克隆远端的所有文件  
git remove -v &emsp; 查看仓库链接  
git fetch 远端名 &emsp; 获取远端代码更新本地  

## 通过克隆建立库和本地的关系  

先在 github 上创建一个仓库（或者github上已经有的仓库），再在本地空文件夹目录下使用 git clone 命令克隆这个仓库, 将跳过 git init 初始化命令生成 .git 文件夹，跳过 git remote 设置远端链接。  

## 远端代码与本地代码发生冲突  

可以 git branch 创建一个本地空分支，将远端代码用 git pull 拉取并合并到空分支当中！或者使用 git fetch 先把远端分支拉取下来，与本地主分支对比后，用 git merge 把两个分支部分合并！  

## 忽略管理  

在工作目录下找到 .gitignore 文件（没有就创建），用记事本打开后输入以下代码。
`/<foldername1>` 仅仅忽略项目根目录下名字为 foldername1 的文件
`<foldername2>` 忽略文件名为 foldername2 的文件和以 foldername2 为名的目录
`<foldername3>/` 忽略文件名为 foldername3 目录下所有文件，但如果当前目录有文件名为 foldername3 ，该文件不会被忽略
`* .[a]` 忽略所有以 .a 为扩展名结尾的文件

- [ ] vscode把 git 命令做了集成按钮，按钮意义是？
- [ ] git log 中的 log 是什么时候完成了更新？
- [ ] git 命令的查询网址链接？
