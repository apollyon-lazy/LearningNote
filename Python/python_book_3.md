# 《Python网络爬虫开发实战》
## 目录
[第一章 开发环境配置](#开发环境配置)
[第二章 爬虫基础](#爬虫基础)

## 开发环境配置
## 爬虫基础
### 参考小节
  - 2.1 HTTP基础原理
  - 2.2 网页基础
  - 2.3 爬虫的基本原理
  - 2.4 会话和Cookies
  - 2.5 代理和基本原理

### 知识点
 - 浏览器向网站所在的服务器发送了一个请求，网站服务器接收到这个请求后进行处理和解析，然后返回对应的响应，传回浏览器，响应中包含有用网页源码等内容，浏览器对其进行解析，将网页呈现。

     ![[spider_1.jpg]]

 - URL(Universal Resource Locator) 统一资源定位符；hypertext 超文本(HTML、CSS、JavaScript)；HTTP(Hyper Text Transfer Protocol) 超文本传输协议
 - **请求**，由客户端向服务端发出，可以分为四部分内容：请求方法(Request Method)(GET、POST)、请求网址(Request URL)、请求头(Request Headers)、请求体(Request Body)
 - GET请求中的参数会包含在URL里面，POST请求数据通过表单形式传输包含在请求体中；GET请求提交数据有限制，POST没有限制
 - **响应**，由服务端返回给客户端，可以分为三部分内容：响应状态码(Response Status Code)(200：服务器正常响应；404：页面未找到)、响应头(Response Headers)、响应体(Response Body)
 - HTML(Hyper Text Markup Language)超文本标记语言、CSS(Cascading Style Sheets)层叠样式表、JS(JavaScript)一种脚本语言
 - 网页的标准形式是html标签内嵌套head和body标签，head标签内定义网页的配置和引用，body内定义网页的正文
 - 爬虫可以简单分为几步：抓取页面(urllib、requests等)、分析页面(Beautiful Soup、pyquery、lxml等)和存储数据(TXT、JSON、数据库等)
 - 会话在服务端，保存用户的会话信息；Cookies在客户端，浏览器在下次访问网页时会自动附带发给服务器
 - 代理指的是代理服务器(proxy server)，作用是代理网络用户取得网络信息
        
  
## 基本库的使用

### 参考小节
  - 3.1 3.2 使用urllib & 使用requests
  - 3.3 正则表达式
  - 3.4 抓取猫眼电影排行

### 知识点
  - 第三方库requests一般用于处理网络请求，是Python内置库urllib的高级封装
  - Python中的re库提供了整个正则表达式的实现，能够完成字符串的检索(search()、findall())、替换(sub())、匹配验证(match())
  - `. `点可以匹配任意字符（除换行符）`*`星代表匹配前面的字符无限次`.*`是贪婪匹配`.*？`是非贪婪匹配
  -[抓取猫眼电影排行代码]( https://github.com/Python3WebSpider/MaoYan) 