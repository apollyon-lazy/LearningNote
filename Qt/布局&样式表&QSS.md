[【QT】史上最全最详细的QSS样式表用法及用例说明_qt qss用法_半醒半醉日复日，花落花开年复年的博客-CSDN博客](https://blog.csdn.net/WL0616/article/details/129118087)

如果要做自适应界面，遇到界面窗口比较多的场合，解决方案是层层布局，在每一层上保持尽可能少的可以控制的控件数量。

QSS文件可以用单一QSS方案，也可以多文件QSS方案，但是单一QSS方案适用于界面简单且样式基本一致的情况，多文件QSS则可以更好的管理不同界面的样式。

## QWidget
![[qt_qss1.jpg]]
QWidget是一个有四层的盒模型，从外到内分别是margin，border，padding，content(这四层都在QWidget内部)，默认情况下margin，border，padding的值为零(当然这可能对QWidget的派生类并非如此)。其中可以注意到一个细节，在Qt Designer中只有QWidget的属性设置栏下有styleSheet，而派生类属性中则没有styleSheet属性，猜测所有属性都在QWidget中被定义，但在派生类定义上却只有个别属性能够作效，且效果各不相同。
```CSS
margin: 10px; /*不支持margin同时设置四个方向不同的值*/
margin-top: 10px; /*bottom/left/right同理*/
/*用border可以同时对border-width border-style border-color进行设置*/
border-style: none; /*默认border-style是none*/
border: 1px solid color(245,245,245,1); /*不支持border同时设置四个方向不同的值*/
/*因为padding是看不见的，同时内容的显示大多不受padding影响，在特定控件中效果会明显*/
padding: 10px; 
/*下面是对QWidget和QLabel不起作用的样式*/
letter-spacing 字符间隔 ×
line-height 行间距 ×
vertical-align 垂直对齐方式 ×
```
`对于QWidget来说，stylesheet中的margin/padding和layout中的margin有什么区别呢(layout的作用域仍是整个QWidget, 设置影响的是QWidget中控件的布局；stylesheet中的margin/padding影响的是其中content，或者说影响的是背景贴图范围，并不会影响到控件的布局；可以理解为盒模型和layout是在下上两个不同的图层)？`

## QPushButton
QPushButton默认是带有border样式是完全覆盖背景的，如果设置background会看不到效果，如果在样式表中修改border则会替换掉原有样式。QPushButton还有flat属性，设置为真会有不一样的按下效果(按钮是否弹起)。在QtDesigner中icon添加资源文件有Normal，Disabled，Active，Selected四种状态，每种状态下有Off和On两种状态，总共有八种可以设置的情况。把图片放在按钮中有两种方式，第一种是通过**样式表**来设置为背景图片，第二种是作为**图标**(图标无法在样式表中添加)添加到按钮当中，两种方式均可在Qt Designer中进行设置。
```CSS
/*flat选择默认为true*/
/*示例一：标题栏上的放大缩小按钮*/
QPushButton#btnMax {
	border: none;
	background-image: url(:/icons/btn_max_default.png);
	background-position: center center;
	background-repeat: no-repeat;
}
QPushButton#btnMax:hover {
	border: none;
	background-color: rgba(230, 230, 230, 1);
}
QPushButton#btnMax:disabled {
	border: none;
	background-image: url(:/icons/btn_max_disable.png);
	background-position: center center;
	background-repeat: no-repeat;
}
```
`按钮的几种状态有什么区别(不同的按钮具有不同的状态，通常按下的按钮考虑Pressed状态，选择的按钮则是考虑Selected状态)？`
QPushButton默认情况下，只有hover(悬停)和pressed(按下)两种状态正在样式表中有明显的视觉效果。
```CSS
/*下面是QPushButton在上面基础上额外支持的一些设置*/
min-height 最小高度 √
max-height 最大高度 √
min-width 最小宽度 √
max-width 最大宽度 √
text-align 文本对齐方式 √ left/right/center
```

```CSS
/*background-color和background-image的先后顺序会影响效果*/
/*background-origin和padding能够调整背景图片位置*/
/*QPushButton的pressed状态从按钮按下保持到按钮释放*/
/*示例二：导航栏按钮切换*/
QPushButton#btnModule {
	border: none;
	background-color: rgba(39, 41, 61, 1);
	background-image: url(:/icons/btn_module_default.png);
	background-position: center top;
	background-origin: content;
	background-repeat: no-repeat;
	padding-top: 16px;
	padding-bottom:16px;
	padding-left: 0px;
	padding-right: 0px;
	font-size: 13px;
	font-weight: 400;
	font-family: "黑体";
	text-align: center bottom;
	color: rgba(124, 126, 153, 1);
}
QPushButton#btnModule:hover {
	border: none;
	background: rgba(26, 27, 41, 1);
	background-image: url(:/icons/btn_module_hover.png);
	background-position: center top;
	background-origin: content;
	background-repeat: no-repeat;
	padding-top: 16px;
	padding-bottom:16px;
	padding-left: 0px;
	padding-right: 0px;
	font-size: 13px;
	font-weight: 700;
	font-family: "黑体";
	color: rgba(169, 222, 216, 1);
	text-align: center bottom;
}
```

## QTreeWidget
```CSS
/*以下是会起效果的*/
alternate-background-color  交替背景色 /*需要alternatingRowColor属性设置为真*/
QTreeWidget::item
QTreeWidget::item:hover
QTreeWidget::item:selected 
QTreeWidget::branch /*更改项前的图标*/
/*无法使用样式表更改某一项的样式，以上均是作用于树状图所有项*/
```