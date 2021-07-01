
# 神马是python？

> 本文章对应项目：[https://aistudio.baidu.com/aistudio/projectdetail/2144759](https://aistudio.baidu.com/aistudio/projectdetail/2144759)

python不会是传说中的蟒蛇吧？

不会吧就是那个冰冷冷，粗壮壮的蟒蛇吧？

哦！并不是呢~~~

不知道大家有没有听说过"人生苦短我用python"的经典语录

> Python 是一种易于学习、功能强大的编程语言。它具有高效的高级数据结构和简单但有效的面向对象编程方法。Python 优雅的语法和动态类型，加上它的解释性质，使其成为大多数平台上许多领域的脚本编写和快速应用程序开发的理想语言。---《python开发文档》

python语言又被称之为胶水语言，由于Python语言的简洁性、易读性以及可扩展性，在国内外用Python做科学计算的研究机构日益增多，一些知名大学已经采用Python来教授程序设计课程。

python具有的开源、易学、可移植、面向对象、可拓展、丰富的库等特点深受大家喜欢。

### 版本说明

python目前主流的版本为python2.7.X和python3.5+（3.5/3.6/3.7/3.8/3.9)

python2和python3的语法相差极大，所以学习前需要提前对里面的内容进行了解，确认自己学习的版本。

python2已于2020年元旦停止更新，划上了跨世纪的一笔。

目前主流学习的就是python3，最新版本是正式版3.9，非正式版本：pre（3.10）和dev（3.11）

**建议：** 学习优先选择python3版本，推荐3.7-3.9版本

### python小故事

* python的发亮代表

python作为一门编程语言，跑不过的必然是对程序员的发量的摧残严重嘛？

让我们一起来看看python创始人荷兰人吉多·范罗苏姆 (Guido van Rossum)的靓照和发亮吧！

<img src="https://user-images.githubusercontent.com/61859193/124131173-1bc71d80-dab2-11eb-83b3-e1fa1b4f5e6c.jpg" alt="pybb" style="zoom:60%;" />

由于python之父吉多·范罗苏姆发际线低头发浓密，成为了大家羡慕的对象，于是流传了一句python名句：**人生苦短我用python**

* python名称的由来

由于 吉多·范罗苏姆当时在追一部电视剧而且入迷很深就从电视剧上来了灵感。

电视剧名为:《蒙提.派森的飞行马戏团》(Monty **Python**'s Flying Circus)

原来大佬也追剧啊~~~

* python神奇的内置库

python中有许多内置库，他们有许多非常刺激的内容，让我们一起来康康：

> 里面的第三方库导入会在后期说明，这里只要查看内容即可

- 你好世界（hello world）

  hello world作为程序员都知道的学习语言测试问候的代码在python中输出该内容需要使用

  ```python 
  print("hello world")  
  ```

  > hello world

  python在这里给大家留了一个神奇的"你好世界"让我们一起来看看吧

  ```python
  import __hello__
  ```

  > hello world

* ### Python之禅

  据说是一位大佬对python的深度解读，同样是据说如果能够把Python之禅理解透彻，python技术水平能够直接芜湖起飞~

  ```python
  import this
  ```

  >

  ```
  The Zen of Python, by Tim Peters
  
  Beautiful is better than ugly.
  Explicit is better than implicit.
  Simple is better than complex.
  Complex is better than complicated.
  Flat is better than nested.
  Sparse is better than dense.
  Readability counts.
  Special cases aren't special enough to break the rules.
  Although practicality beats purity.
  Errors should never pass silently.
  Unless explicitly silenced.
  In the face of ambiguity, refuse the temptation to guess.
  There should be one-- and preferably only one --obvious way to do it.
  Although that way may not be obvious at first unless you're Dutch.
  Now is better than never.
  Although never is often better than *right* now.
  If the implementation is hard to explain, it's a bad idea.
  If the implementation is easy to explain, it may be a good idea.
  Namespaces are one honking great idea -- let's do more of those!
  ```

> ```
> Python之禅 by Tim Peters
>  
> 优美胜于丑陋（Python 以编写优美的代码为目标）
> 明了胜于晦涩（优美的代码应当是明了的，命名规范，风格相似）
> 简洁胜于复杂（优美的代码应当是简洁的，不要有复杂的内部实现）
> 复杂胜于凌乱（如果复杂不可避免，那代码间也不能有难懂的关系，要保持接口简洁）
> 扁平胜于嵌套（优美的代码应当是扁平的，不能有太多的嵌套）
> 间隔胜于紧凑（优美的代码有适当的间隔，不要奢望一行代码解决问题）
> 可读性很重要（优美的代码是可读的）
> 即便假借特例的实用性之名，也不可违背这些规则（这些规则至高无上）
>  
> 不要包容所有错误，除非你确定需要这样做（精准地捕获异常，不写 except:pass 风格的代码）
>  
> 当存在多种可能，不要尝试去猜测
> 而是尽量找一种，最好是唯一一种明显的解决方案（如果不确定，就用穷举法）
> 虽然这并不容易，因为你不是 Python 之父（这里的 Dutch 是指 Guido ）
>  
> 做也许好过不做，但不假思索就动手还不如不做（动手之前要细思量）
>  
> 如果你无法向人描述你的方案，那肯定不是一个好方案；反之亦然（方案测评标准）
>  
> 命名空间是一种绝妙的理念，我们应当多加利用（倡导与号召）
> (主流解释，非官方~)
> ```

python还有其他的经典小彩蛋，可以在以后的学习过程中进行查看等

python的故事很精彩，使用很精巧，我们后期慢慢展开~~~


> 参考文章：
>
> 1、[《大话Python——盘点一些关于Python当中的梗》](https://aistudio.baidu.com/aistudio/projectdetail/1499947)— super 松
>
> 2、[《python基础知识》](https://aistudio.baidu.com/aistudio/projectdetail/1564661)— 三 岁
>
> 3、[python官方文档：https://docs.python.org/zh-cn/3.7/tutorial/index.html](https://docs.python.org/zh-cn/3.7/tutorial/index.html)
>
> 4、[python官网：https://www.python.org/](https://www.python.org/)
