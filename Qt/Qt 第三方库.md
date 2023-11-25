# Qt Dll调用

[(10条消息) Qt：56---QT创建和使用动态链接库（.dll）_qt生成dll文件_董哥的黑板报的博客-CSDN博客](https://blog.csdn.net/qq_41453285/article/details/100087495) CSDN dll 参考调用教程

![[qt_share1.jpg]]

在Qt Creator中按照 “New File or Project”->“Library”->"C++ Library" 可以创建库文件工程，工程名起名为MyShareLib(需要在存放Qt所有项目的文件夹中新建一个文件夹，也起名为MyShareLib并作为工程创建的位置)。这样存放的目的在于Qt会把不同组件配置(组件暂时选择Desktop Qt 5.14.2 MinGW 64-bit)不同模式(Debug和Release)的文件夹，放在和工程文件夹同一目录下，方便统一管理(有趣的是，每个编译生成的新的项目文件夹中都有debug和release子文件夹，但是在debug版本中只有debug子文件夹中有内容，在release版本中只有release子文件夹中有内容)。

在定义项目细节时，Qt提供了Shared Library，Statically Link Library，Qt Plugin三种类型(本节教程默认选择Shared Library 即**共享库**)，按照默认工程配置走下来，最终会创建带有两个头文件 mySharedlib.h  MySharedLib_global.h 和一个源文件 mysharedlib 的工程。

`Windows和Linux下的动态链接库文件后缀区别(从Linux对文件的分类上来说，gcc -c 编译后会生成.o后缀的可重定位文件，它和.so的共享目标文件和.out的可执行文件三类文件同属于ELF文件，即可执行与可链接文件，本质上都是二进制文件，Linux中后缀并非强制只是默认如此；从程序预处理编译链接再到执行的角度看，Linux上的.o后缀的文件就是我们说的编译完未进行链接操作的目标文件；在Windows中，MinGW输出为.a和.dll，MSVC输出为.lib和.dll，在Linux中，对应为.a和.so)？`
`静态链接和动态链接的区别(先从Linux的gcc使用上看，静态链接的.a文件本质是.o文件的集合，再与其他文件静态链接生成可执行文件也是往集合中增加目标文件，故最终可执行文件大，不需要加载库文件，才执行速度快；动态链接文件不在最终可执行文件内，需要使用-l指定库文件名，-L指定库文件的搜索路径，故最终可执行文件小，需要加载库文件，才执行速度慢；延伸到Windows上，区别也是在程序运行过程中需不需要加载库文件)？`

```C++
// MySharedLib_global.h
#ifndef MYSHAREDLIB_GLOBAL_H
#define MYSHAREDLIB_GLOBAL_H

#include <QtCore/qglobal.h>

#if defined(MYSHAREDLIB_LIBRARY)
#  define MYSHAREDLIB_EXPORT Q_DECL_EXPORT
#else
#  define MYSHAREDLIB_EXPORT Q_DECL_IMPORT
#endif

#endif // MYSHAREDLIB_GLOBAL_H
```

分析MySharedLib_global.h文件，其中关键代码是这么写的，如果定义了**MYSHAREDLIB_LIBRARY**宏，就把**MYSHAREDLIB_EXPORT**作为Q_DECL_EXPORT**宏**的别名，否则作为Q_DECL_EXPORT**宏**的别名(注意加粗的两个量是不一样的)。MYSHAREDLIB_LIBRARY这个宏是在.pro文件中定义的，如果定义了表示当前是在**编译**共享库的源文件，Q_DECL_EXPORT用来标记需要从共享库中导出的符号；如果没定义表示当前是在**使用**共享库的源文件，Q_DECL_IMPORT用来标记需要从共享库中导入的符号。Q_DECL_EXPORT和Q_DECL_IMPORT会根据使用平台选择合适的关键字替代。

`计算机领域中常说不同平台是指什么(不同平台常指不同的处理器架构，不同的操作系统，不同的开发环境和架构等，平台的差异会影响应用程序的编译，链接，部署和运行方式)？`

`怎么理解共享库的导入导出？`

![[qt_share2.jpg]]

注意到我们在MySharedLib类和add函数前面都加了MYSHAREDLIB_EXPORT宏，并且在add函数宏前还加了extern "C"，这是因为C++增加的函数重载命名空间等新特性导致对链接的规则与C不同。

![[qt_share3.jpg]]

因为选择的MinGW编译，所以会生成MyShareLib.dll和libMySharedLib.a(这里的.a是提供动态链接用的函数声明和链接，不包含实际的代码)两个文件，其中MyShareLib.dll在运行程序时调用，mySharedLib.dll 在隐式调用动态链接库时使用。采用debug和release不同模式生成的文件只能在应用程序的debug和release模式下编译或调用。
[为什么动态链接.dll和.lib都需要(详解静、动态链接库)_链接需要dll吗_代码乌龟的博客-CSDN博客](https://blog.csdn.net/weixin_43744293/article/details/117283686)

`动态链接中的lib文件是静态库lib么(不是，动态库lib文件中只包括函数声明和链接，没有实际的代码)？`

## 隐式调用

先说**隐式调用**，首先，在需要动态库的项目中建议先创建一个目录，专门用来存放头文件(比如起名为inc)，把需要的两个头文件 mySharedlib.h  MySharedLib_global.h 复制到该目录(其实头文件和源文件都应当在Qt工程中各分属在一个文件夹)。然后，把动态库lib文件(MinGW下是.a，MSVC下是.lib)复制到目录中。最后，把动态库dll文件(这个文件要先在动态库工程对应版本下编译生成)放在对应版本文件目录下。

![[qt_share4.jpg]]

这里需要动态库的工程起名为MyProject，工程文件夹下创建inc子文件夹，用来存放 mysharedlib.h MySharedLib_global.h libMySharedLib.a(这是debug版本下的动态lib文件)，debug版本的MyProject中加入MySharedLib.dll文件。

`为什么这里Release和Debug版本需要用-d后缀区分(因为debug版本的动态库lib只能在debug版本中运行，release版本的动态库lib只能在release版本中运行，但两个动态lib库在生成时具有相同名字，所以需要用后缀区分)？`

![[qt_share5.jpg]]

选择"Add Library"->"External library"到达当前页面，这里选择Library file为之前创建的inc子文件夹中的动态库lib文件 libMyShardeLib.a，include path会自动选择该子文件夹。

`这里为什么会默认动态库lib文件和外部头文件在同一目录下(换个角度，这样可以在Qt工程中单独文件夹放第三方库)？`

![[qt_share6.jpg]]

最后会在工程.pro文件中自动生成以上代码(这里的代码还是通过Qt软件添加生成好，自己配置很容易出错)，这里分析一下这段代码含义。在Windows平台的Release模式下，将目录 `$$PWD/inc/` 作为头文件搜寻目录 `-L` ，将**MySharedLib**文件作为导入库；在Debug模式下，将目录 `$$PWD/inc/` 作为头文件搜寻目录 `-L` ，将**MySharedLibd**文件作为导入库。把 `$$PWD/inc/` 添加到头文件搜索路径，把`$$PWD/inc/` 添加到依赖项搜索路径。

`qmake中LIBS变量的作用(LIBS用于将特定的库文件添加到链接路径)？`
`qmake中INCLUDEPATH变量和的作用(INCLUDEPATH用于指定头文件的搜索路径)？`
`qmake中DEPENDPATH变量的作用(DEPENDPATH用于指定依赖文件的搜索路径)？`
`这里为什么LIBS,INCLUDEPATH,DEPENDPATH都是我们创建的inc同一子目录(因为这里dll文件，lib文件，h文件都存放在同一inc文件夹下，LIBS是dll文件的配置，lib文件是DEPENDPATH的配置，h是INCLUDEPATH的配置)？`

![[qt_share7.jpg]]

终于到了最后一步，首先，"Header"->"Add Existing Files"，找到inc目录下的mysharedlib.h和MySharedLib_global.h两个文件添加到工程，添加成功后会在.pro文件中增加如下代码。
``` C++
HEADER += \
	inc/MySharedLib_global.h \
	inc/mysharedlib.h
```
不难理解，是把头文件添加到了工程，这也是安全添加到工程的方法(会自动生成.pro的配置代码)。
然后添加头文件，编写代码，编译运行，就能够使用我们的动态库了(Output框中打印了Hello World!结果)。

**Qt中隐式调用的步骤**
- 首先准备一个动态库工程(示例中是在QtCreater中创建C++Library的项目，配置为64位MinGW的Debug版本)
- 准备动态库(.dll)动态导入库(.lib)和头文件(.h)都放在合适的位置(示例中都放在了inc文件夹中，lib要做版本区分)
- 在项目中添加动态库，在项目中添加头文件
## 显式调用

`如何把Qt工程中的源文件头文件UI文件资源文件在项目文件夹中分开？`
`显示调用和隐式调用的区别是(显示调用要保持DLL的加载状态)？`

