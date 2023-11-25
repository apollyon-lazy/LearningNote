
## OpenGL

[主页 - LearnOpenGL CN (learnopengl-cn.github.io)](https://learnopengl-cn.github.io/) LearnOpenGL 中文版
[https://learnopengl.com/](https://learnopengl.com/)LearnOpenGL 英文版

OpenGL是一个由 Khronos 组织制定并维护的规范，也是一个跨平台的、开放源代码的图形库，也，它提供了一套API，用于开发二维和三维图形应用程序。Khronos组织是一个非营利性技术联盟，致力于开发和推广开放的、跨平台的标准和API，以促进图形、游戏和虚拟现实等领域的发展。
OpenGL在3.3版本及以后使用核心模式(Core-profile)开发，开发者有了更多对绘图细节的掌控。OpenGL本质是一个大的状态机，一种是改变上下文(Context)的状态设置函数(State-changeing Function)，一种是用于绘图的状态使用函数(State-using Function)。

## Unity

```C++
QString exePath = "./unity/Stewart.exe";
unityProcess = new QProcess(this);
unityProcess->start(exePath);
if(unityProcess->waitForStarted()){
    WId unityWid = (WId)FindWindow(L"UnityWndClass",L"运动平台数字孪生模型");
    QWindow *unityWindow = QWindow::fromWinId(unityWid);
    if (unityWindow) {
        QWidget *unityWidget = QWidget::createWindowContainer(unityWindow);
        plantform->setWidget(unityWidget);
        plantform->show();
    } else {
        qDebug() << "无法获取Unity窗口";
    }
} else {
    qDebug() << "无法启动Unity";
}
```
`WId和HWND是什么(WId是Qt框架中的窗口标识符，HWND是Windows操作系统中标识窗口的句柄类型)？`
`什么是句柄类型(计算机科学中用于标识和操作资源的一种抽象概念，比如HWND是用于标识和操作Windows操作系统的窗口，FILE*是用于标识和操作C语言中的文件流，QFile和QIODevice是Qt框架中表示和操作文件的句柄类型)？`

代码解读
`WId unityWid = (WId)FindWindow(L"UnityWndClass",L"运动平台数字孪生模型");`这里用`windows.h`头文件(Windows API)中的`FindWindow`函数找到窗口类名为`UnityWndClass`窗口标题名为`运动平台数字孪生模型`的窗口句柄`HWND`，再通过强制类型装换为Qt中的通用标识符`WId`；这里的`UnityWndClass`和`运动平台数字孪生模型`由Unity开发人员定义，L加字符串代表解释为宽字符字符串(Unicode编译模式下)，否则解释为窄字符字符串(ANSI编译模式下)