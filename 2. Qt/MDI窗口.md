两种把MDI子窗口添加到MDI区域的写法。
```C++
QMdiArea mdiArea;
// 写法一
QMdiSubWindow *subWindow1 = new QMdiSubWindow;
subWindow1->setWidget(internalWidget1);
subWindow1->setAttribute(Qt::WA_DeleteOnClose);
mdiArea.addSubWindow(subWindow1);
// 写法二
QMdiSubWindow *subWindow2 = mdiArea.addSubWindow(internalWidget2);
```
写法一
- `QMdiSubWindow *subWindow1 = new QMdiSubWindow;`创建新的MDI子窗口
- `subWindow1->setWidget(internalWidget1);`设置MDI子窗口的控件
- `subWindow1->setAttribute(Qt::WA_DeleteOnClose);`设置MDI子窗口关闭时释放
- `mdiArea.addSubWindow(subWindow1);`在MDI区域中添加MDI子窗口
写法二
- `QMdiSubWindow *subWindow2 = mdiArea.addSubWindow(internalWidget2);`在MDI区域添加子窗口或指定控件的子窗口

疑惑一：对象树的问题
- 写法一：当MDI子窗口被添加到MDI区域时，会把MDI区域作为子窗口的父亲，挂在对象树上(意味着在MDI区域释放时会释放MDI子窗口)；设置MDI子窗口的控件，会把控件的父对象设置为MDI子窗口(意味着在释放MDI子窗口时会释放内部控件)
- 写法二：MDI子窗口的控件并不是显式添加进去，控件的父对象保持原先值或者为空(意味着释放MDI子窗口不会释放内部控件)
疑惑二：MDI子窗口关闭时的问题

成功案例一
- 首先，准备一个存放不同MDI内部控件指针的数组`QVector<QWidget*>formGroup`，
- 当需要创建MDI时，遍历指针数组 **找到需要的MDI内部控件** 指针，否则为 **空**
- 遍历MDI区域内子窗口指针列表，如果 **内部控件不为空** 且 **内部控件指针存在于数组** ，获取这个MDI子窗口指针，否则子窗口指针为 **空**
- 如果MDI子窗口指针存在将其激活，如果不存在使用写法一，创建自定义MDI子窗口并设置内部控件

`这里判断MDI子窗口控件不为空的作用(若为空有可能子窗口存在但控件为空，所以不为空代表空间和子窗口都存在)？`
`这里判断MDI子窗口控件为数组中控件的作用(这代表当前MDI子窗口在MDI区域中)？`

- 自定义MDI窗口在释放时会把内部控件设置为空 `setWidget(nullptr)`，这样控件的父对象不再是MDI子窗口，考虑到当MDI子窗口存在时软件被关闭，MDI区域的释放会连带释放MDI子窗口，再连带其中控件(对象树会在执行完父对象的析构函数后，执行子对象的析构函数)，否则会造成指针数组的二次释放
- 自定义MDI窗口在关闭时会把内部控件设置为空 `setWidget(nullptr)`， 这样在点击关闭按钮后控件的父对象不再是MDI子窗口，考虑到`subWindow1->setAttribute(Qt::WA_DeleteOnClose);`，否则会造成提前释放指针数组