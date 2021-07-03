# python的安装与编译器

python的安装有几种方式：安装python本体、安装conda（开源的软件包管理系统和环境管理系统）、使用编译器虚拟环境等

## 不同情况不同推荐

* 个人使用，无多种环境需求，没有同类大型框架需要切换可以使用——python本体

* 个人或教师使用，对于不同版本有需求，需要多个环境进行切换——conda

* 仅在固有编译器中使用，不在计算机环境下使用——编译器虚拟环境（例如pycharm）

  **说明：**如果有不同版本需要切换python就要安装多个，这样子使用不方便而且环境变量设置极为麻烦。建议conda。如果是多个同类大型框架，容易造成冲突建议单独设立环境，这样子就不会出现未知的冲突和意外的报错。

-----

### python本体

本体就是单个的python环境，自带IDLE编译器
<img src="https://user-images.githubusercontent.com/61859193/124354084-c66b4780-dc3c-11eb-9608-8c2e2e4c9bcf.png" alt="image-20210703150848118" style="zoom: 67%;" />

该环境可以实现python的运行等，大部分的事情，配合各类编译器使用非常Nice！

----

### conda

Conda 是一个开源的软件包管理系统和环境管理系统，用于安装多个版本的软件包及其依赖关系，并在它们之间轻松切换。

分为Anaconda和Miniconda中文名分别是"大蟒蛇"和"小蟒蛇"。

两者唯一的区别就是内置的第三方库数量不一样，其他的基本上一样。

切换环境非常Nice！

---

### 编译器

主流编译器：IDLE（本体自带）、Jupyter Notebook（conda打包，云端）、pycharm、Visual Studio

* IDLE（本体自带）

  推荐新手学习使用，虽然界面很单调，功能很局限但是还是非常强烈推荐

  新手学习得多敲代码，自己查找和查看报错，所以IDLE非常推荐，最开始的一段时间的学习。

* Jupyter NoteBook

  一个适用于上课学习的环境里面可以逐段运行查看数据，对新手和课程教学非常友好，而且有代码自动补充功能非常好上手

  安装方式：

  本体可以通过在cmd中使用`pip install jupyterlab`进行安装，然后使用`jupyter notebook`代码进行运行。

  conda中自带了notebook环境点击即可，或者使用`jupyter notebook`代码进行运行。
  ![image-20210703160338770](https://user-images.githubusercontent.com/61859193/124354098-d97e1780-dc3c-11eb-8798-baab4a64e594.png)




* pycharm

  **JetBrains Academy** 公司产品

  分为社区版本和专业版本
  
  其中社区版本完全免费，专业版本收费（学生证可以免需要申请）
  
  一般情况社区版本完全可以满足日常需要。
  
  > * 更加高效
  >   由PyCharm负责处理日常繁琐的工作细节，为您节省宝贵的时间。 让您专注于关键任务，并且善用以键盘操作为主的编程方法，充分利用 PyCharm 的种种高效功能。
  >
  > * 获得智能辅助
  >
  >   PyCharm完全理解代码的每个面向。 依靠它的智能代码补全、 实时错误检查和快速修复功能，轻松进行项目导航 等众多功能辅助您。
  >
  > * 提高代码质量
  >
  >   编写整洁、易维护的代码，而 IDE 将利用 PEP8 检查、测试辅助、智能重构和大量检查帮助您控制质量。
  >
  > * 正如您所需
  >
  >   PyCharm是程序员为程序员设计的开发环境，提供您进行 高效Python开发所需的所有工具。
  >
  >   ——《pycharm官网》
  
* Visual Studio

  Microsoft Visual Studio（简称VS）是美国微软公司的开发工具包系列产品。VS是一个基本完整的开发工具集，它包括了整个软件生命周期中所需要的大部分工具。他不仅仅只能够处理python，还有其他的语言。

## 本体安装

### 本体下载（各版本）

* 官网下载

  第一步进入官网

  官网地址：[https://www.python.org/](https://www.python.org/)

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126203747589.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTYyMzA5Mw==,size_16,color_FFFFFF,t_70)

  点击资料下载然后选择所有发行
  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126204008334.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTYyMzA5Mw==,size_16,color_FFFFFF,t_70)

  下滑，找到特定版本然后选择自己的版本点击下载
  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126204044103.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTYyMzA5Mw==,size_16,color_FFFFFF,t_70)

  此处以3.7.4为例子，继续下滑
  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126204241864.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTYyMzA5Mw==,size_16,color_FFFFFF,t_70)

  找到档案和选择适合自己的版本下载接口

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126204116670.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTYyMzA5Mw==,size_16,color_FFFFFF,t_70)

  根据自己实际情况进行下载下载即可。

  

* 镜像地址下载

  推荐地址：[https://mirrors.huaweicloud.com/python/](https://mirrors.huaweicloud.com/python/)

  进入镜像，选择自己想要下载的版本

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126204456253.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTYyMzA5Mw==,size_16,color_FFFFFF,t_70)

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126204520242.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTYyMzA5Mw==,size_16,color_FFFFFF,t_70)

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126204553609.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTYyMzA5Mw==,size_16,color_FFFFFF,t_70)

  上述还是以3.7.4为例进行的查找。

  

通过上面的办法就可以下载到我们心仪的版本了，接下来就是安装了，让我们一起来看看怎么样安装。

### 本体安装

找到下载的本体，双击/右击打开/右击以管理员模式运行都可，接下去我们会看到如下内容：

![在这里插入图片描述](https://img-blog.csdnimg.cn/2020041411362119.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTYyMzA5Mw==,size_16,color_FFFFFF,t_70)

* 安装界面说明

  <img src="https://img-blog.csdnimg.cn/20200414113735261.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTYyMzA5Mw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" style="zoom:80%;" />

  

* **注意！！！关键！！！！**

  这里的`Add Python 3.x to PATH`前面的框框一定要打上勾，不然需要自己去配置环境（如果是大佬请随便！）

  如果家里有矿（bushi）电脑内存等富裕可以直接点击`Install Now`如果没有请选择`Customize installation`

  然后选择`next`接着修改自己选择安装的地址再选择`install`（如下图）

  ​	![在这里插入图片描述](https://img-blog.csdnimg.cn/20200414113801460.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTYyMzA5Mw==,size_16,color_FFFFFF,t_70)

  ​	<img src="https://img-blog.csdnimg.cn/20200414113816101.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTYyMzA5Mw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" style="zoom:85%;" />

这样子就基本上安装完成了。

如果出现安装失败请查看是否是下载错版本了（64位和32位的）

* 个人不推荐下载最新版本，目前推荐的3.7和3.8，然后是3.9（2021年7月）

### conda安装

Anaconda官方下载地址：[https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual)

Miniconda下载地址：[https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)

下载对应的版本然后安装即可，这里要注意也要添加环境变量的配置，记得打上勾~~~

> 本体安装视频：[https://www.bilibili.com/video/BV1Mi4y1t7cP](https://www.bilibili.com/video/BV1Mi4y1t7cP)

> 参考资料：
>
> [《如何下载python3.7/3.8或者更早版本》](https://blog.csdn.net/weixin_45623093/article/details/113193263)——三岁学编程
>
> [《三岁学编程之python安装（最细教程）》](https://blog.csdn.net/weixin_45623093/article/details/105508265)——三岁学编程
>
> [python官网](https://www.python.org/)：https://www.python.org/
>
> [Anaconda官网：](https://www.anaconda.com/)https://www.anaconda.com/
>
> [康达文档](https://docs.conda.io/projects/conda/en/latest/index.html#)：https://docs.conda.io/projects/conda/en/latest/index.html
>
> [pycharm官网：](https://www.jetbrains.com/pycharm/)https://www.jetbrains.com/pycharm/

