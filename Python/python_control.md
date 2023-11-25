本文旨在归纳python与control相关的内容

## control

### demo1
![[pyct1.jpg]]

```Python
>>> import control as ct
>>> P = ct.tf2io(1, [1, 0], inputs='u', outputs='y')
>>> C = ct.tf2io(10, [1, 1], inputs='e', outputs='u')
>>> sumblk = ct.summing_junction(inputs=['r', '-y'], output='e')
>>> T = ct.interconnect(syslist=[P, C, sumblk], inputs='r', outputs='y')
>>> T.ninputs, T,ninputs, T.noutputs
(1, 1, 2)
```
![[pyct2.jpg]]
tf2io() 能够把 LTI 转化为 `InputOutputSystem`
summing_junction() 会创建一个结合点，这个结合点的类型是 `InputOutputSystem`
interconnect() 会把 syslist 中的 InputOutputSystem 按照 connections 连接起来
这里就是把 P C sumblk 连接在一起；这里 connections 缺省，会默认将名字相同的信号尝试连接
最终搭建了一个闭环反馈系统，是 SISO 系统，类型是 `LinearICSyetem`
所以还不能确定用 interconnect() 可以连接 `NonlinearSyetem` ?

