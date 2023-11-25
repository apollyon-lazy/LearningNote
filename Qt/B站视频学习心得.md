
创建第一个Qt程序 `QWidget QMainWindow QDialog`
创建按钮控件 `QPushButton * btn = new QPushBytton("ButtonText", this)`
信号和槽 `connect() disconnect()`
点击按钮关闭窗口案例 `connect(btn, &QPushButton::click, this, &QWidget::close)`
自定义信号和槽  `emit 自定义信号`
`自定义信号：返回void 需要声明不需要实现 可以有参数 可以重载`
`自定义槽函数：返回void 需要声明需要实现 可以有参数 可以重载`
重载利用函数指针 

QMainWindow `QMenuBar(1) QToolBar(n) QStatusBar(1) QDockWidget(n) QCentralWidget(1)`
资源文件 `：+前缀名+文件名`
模态和非模态对话框 
界面布局
按钮控件 `QPushButton QToolButton radioButton checkBox`
列表容器 树控件 表格控件 `QListWidget QTreeWidget QTableWidget`
栈控件 下拉框 标签 `stackedWidget comboBox QLabel`

自定义控件封装 `QSpinBox + QSlider`
鼠标事件 `enterEvent leaveEvent mousePressEvent mouseReleaseEvent mouseMoveEvent`
定时器 `void timerEvent(QTimerEvent * ev)` `QTimer * timer = new QTimer(this)`
事件分发 事件过滤器
QPainter绘图 `void paintEvent()` `QPainter painter(this)`
QPaintDevice绘图设备 `QPixmap Qimage QPicture`
QFile文件读写
QFileInfo读取文件信息

---


