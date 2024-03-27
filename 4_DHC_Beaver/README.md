## 导航

内部链接
[[anaconda]] Python环境配置
[[《Python编程从入门到实践》]] Python编程从入门到实践
[[dhc2_dynamics]] DHC_beaver动力学开环测试
[[dhc2_trim]] DHC_beaver带配平的动力学开环测试

外部链接
[Analyze Dynamic Response and Flying Qualities of Aerospace Vehicles - MATLAB & Simulink - MathWorks 中国](https://ww2.mathworks.cn/help/aeroblks/analyze-dynamic-response-and-flying-qualities-of-aerospace-vehicles.html?searchHighlight=this%20template%20uses%20a%206DOF&s_tid=srchtitle_this%20template%20uses%20a%206DOF_1#mw_7530ee8e-d206-4db2-b73c-3d66075b402a) Simulink (Aerospace Blocket) 2-56
[Fly the De Havilland Beaver - MATLAB & Simulink - MathWorks 中国](https://ww2.mathworks.cn/help/aeroblks/fly-the-dehavilland-beaver.html?searchHighlight=beaver&s_tid=srchtitle_beaver_1) Simulink (Aerospace Blocket) 9-7

## BrainStorming

1. 怎么写代码？在哪写代码？文档怎么写？怎么测试函数？

在Vscode用的.py文件中用Python语法写代码(当然Juypter也行)；
文档计划按照功能划分，每个阶段我想实现的功能我会单独写一份文档出来；
测试函数理论上是要和Fdc工具箱的结果进行比对，最好是MATLAB也有对应的对比程序；

2. 想一想目前要按照什么功能划分文档？文档里该有什么？测试对比有差异怎么办？

暂定划分功能如下：动力学代码一份文档；配平代码一份文档；后续等待拆分...
文档里主要是对涉及原理的介绍，公式及代码的展示，展示的代码通过复制拼合要能在一个文件当中跑通，并实现文档中对该功能的描述；
有明显差异可能是存在Bug，有微小差异也要能确定是数值精度或者底层代码不同的原因；

3. 那文档写在哪里？怎么利用之前已有的成果？已有的成果有哪些？

文档目前全部写在Obsidian中，原先可以利用的有main和debug两个主要的文档，main是负责主要展示的代码，debug主要是心路历程，目的是方便检查问题细分后是哪里出现了问题，main类的文档别人要能看懂，debug类的文档自己要能够看懂；

目前成果有：Python环境的配置；动力学代码一份文档；配平代码一份文档等...... 后续写好后会使用双向链接功能链接在REAMDA文档当中

4. README文档主要干什么？

目前就写写发散思维的问题及回答，项目的进度及新路想法，后期成果的链接，其余后续再补充...哦对，GPT是肯定要考虑的！

5. 控制怎么写？
先学会matlab control工具箱中的经典案例及背后原理，明确MATLAB代码能不能实现Simulink同样的结果；再到python control研究其中MATLAB是否能够帮助构建控制系统...
[[Tutorial] Control Systems Simulation in Python | Example (csestack.org)](https://www.csestack.org/control-systems-simulation-python-example/) 自定义类写控制代码
[Python Control Systems Library — Python Control Systems Library 0.9.4 documentation (python-control.readthedocs.io)](https://python-control.readthedocs.io/en/0.9.4/) 现成control库使用
[Control System with Python - Air Heater System.pdf (halvorsen.blog)](https://www.halvorsen.blog/documents/programming/python/resources/powerpoints/Control%20System%20with%20Python%20-%20Air%20Heater%20System.pdf) 教你如何使用control库





- [x] 更新于2023-5-31
