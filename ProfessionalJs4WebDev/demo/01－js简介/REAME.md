# JavaScript 核心部件：

> * ECMAScript - 欧洲计算机制造商协会
> * DOM - Document Object Model
> * BOM - Bowser Object Model

ECMAScript 规定了js的规范，web浏览器只是实现其规范的宿主环境之一，其它宿主环境还有`node`、`Flash`等。

ECMAScript 主要组成部分：

 - 列表项
 - 语法
 - 类型
 - 操作符
 - 对象
 - 保留字
 - 语句等


## DOM

DOM 是针对xml但经过扩展用于html 的程序接口

DHTML 形成后，由于各种历史原因，两大浏览器厂商（`Netscape` 和 `Microsoft`）各不兼容，给前端开发带来极大麻烦。此时，**w3c**（World Wide Web Consortium 万维网联盟）开始着手规划 DOM

DOM1 ( DOM Level-1)，w3c 推出第一个版本的dom，由两个模块组成： DOM Core + DOM HTML。目的是为了映射文档结构。

DOM2 ( DOM Level-2)，在第一版的基础上又加入了 css、事件、鼠标、遍历； 早期浏览器厂商对dom1~2 实现并不完善，特别是`ie`，`ff`在这方面更下功夫，后来居上的`chrome` 更是强大


## BOM

BOM 主要处理浏览器窗口和框架 （window + frame），另外还包括一些扩展：

 - 窗口事件
 - navigator
 - location
 - screen
 - XMLHttpRequest
 - cookie
 
-----

虽然有了ECMAScript 规范，但各个浏览器支持程度不同，导致大多数web应用兼容性不好； 目前主流浏览器对 ECMAScript v3（1997~2007） 支持的都不错， ECMAScript 2015(2015.6.17) 正式发布后，大家也在努力实现，预计明年6月能看到几大主流厂商的努力成果。