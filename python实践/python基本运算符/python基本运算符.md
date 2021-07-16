python基础运算符、表达式

由于本章内容纯文字解析说不清楚，直接把.ipynb的notebook给搬运了过来，虽然不是很好看，但是更加清晰，大家看看有啥问题直接issue给我

> 线上平台体验地址：[python 基础运算符与表达式](https://aistudio.baidu.com/aistudio/projectdetail/1570215)

## 基础运算符
***
  ### 加减乘除
***
编程的加减乘除与普通数学有所不同  
有基础的盆友要注意python的运算与其他语言有所区别！！！  
***
### **加法:使用 '+'**    
' + ' 运算符不仅仅用于数学的加法还用于字符串的拼接等

```python
print('hello' + 'world')
```

```
hello world
```



***
  ### **减法 使用 '-'**  
' - '可以用于减法  
***
### **乘法  使用'*'**  
' * ' 使用方法  
①用于数字的乘法  
②用于字符串的多次输出  (在print里面举过多次输出的例子)

***
###   **除法 使用 ' / '**  
普通数学除法    

* 有计算机编程基础的小哥哥小姐姐注意！！！**有余数**  


```python
# 加法
print(1+2)
print('hello '+'paddle')

# 减法
print(2-1)
# 乘法
print(2*3)
print('Paddle'*2)
# 除法
print(10/3)
```

    3
    hello paddle
    1
    6
    PaddlePaddle
    3.3333333333333335


## 其他基础运算符
***
  ### 整除 、乘幂 、取模
***
整除：与其他的编程语言略微不同
  乘幂：与数学基本相同
  取模：就是传说中的取余数
***
### **整除:使用 '//'**    
' // ' 除法得到的结果取整数位
***
  ### **乘幂 使用 '\*\*'**  
' \*\* '和数学一样 
***
### **取模  使用'%'**  
' % '：就是取余数   
* 有计算机编程基础的小哥哥小姐姐注意！！！**有余数**  



```python
a = 5
b = 2
print('整除:', a // b)
print('乘幂：', a ** b)
print('取余：', a % b)
```

    整除: 2
    乘幂： 25
    取余： 1


## 特殊运算符
***
  特殊算法是比较贴合计算机低层，在python中多用于脚本书写和一些算法    
主要是一些二进制的运算！！！  

***

### **向左移 使用' << '**  
该符号是把数字转换为二进制然后向左移  


```python
2  <<  2
```


    8



![ 2<<2解析 ](https://img-blog.csdnimg.cn/2020031717330976.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTYyMzA5Mw==,size_16,color_FFFFFF,t_70)
 >我们先把2转换为2进制“10”一共6位前面拿0补齐  
 我们把10往前移2位后面0补齐得到“001000”  
 得到结果8  

  ###  **向右移  使用' >> '**  
与向右移差不多异曲同工  
  该符号是把数字转换为二进制然后向右移


```python
11 >> 1
```


    5



![右移解析](https://img-blog.csdnimg.cn/20200317173810659.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTYyMzA5Mw==,size_16,color_FFFFFF,t_70)  
>11的二进制右移其他的0补齐，得到的结果基本上就是了  
至于少掉的1应该理解为缺失了

自己画的图有问题的及时提哟！！

  ###  **按位与 使用 '&'**  
都为1取1，有一个是0就是0


```python
5 & 3
```


    1



![在这里插入图片描述](https://img-blog.csdnimg.cn/20200317181320980.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTYyMzA5Mw==,size_16,color_FFFFFF,t_70)
> 都是1的为1有一个为0的就是0,补齐后就是结果

  ###  **按位或  使用'|'**  
有一个是1就是1，全部为0才是0


```python
5 | 3
```


    7



![在这里插入图片描述](https://img-blog.csdnimg.cn/20200317181447178.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTYyMzA5Mw==,size_16,color_FFFFFF,t_70)
>有一个是1就是1，全部为0才是0,补齐即可

  ###  **按位异或 使用' ^ '**  
相同的写0，不同的写1


```python
5 ^ 3
```


    6



![在这里插入图片描述](https://img-blog.csdnimg.cn/20200317181617596.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTYyMzA5Mw==,size_16,color_FFFFFF,t_70)

  ###  **按位取反 使用' ~ '**  
按位取反的结果等于-（n+1）（正负号都符合）


```python
~5
```


    -6



![在这里插入图片描述](https://img-blog.csdnimg.cn/20200317183226989.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTYyMzA5Mw==,size_16,color_FFFFFF,t_70)

以上内容如有不同看法或有错误请及时指出，三岁一定认真对待及时修改！

## 比较符
***
<font size=3>

  ###  **小于 使用 ' < '**  
判断结果是否正确返回浮点型  
  ###  **大于 使用'  > '**  
判断结果是否正确返回浮点型  
  ###  **大于等于 使用' >= '  小于等于 使用' <='**  
判断结果是否正确返回浮点型  
  ###  **赋值  使用' = '  等于使用 ' == '**  
判断结果是否正确返回浮点型  
  ###  **不等于 使用' != '**  
判断结果是否正确返回浮点型，与等于相反  
  </font>


```python
a = 1
b = 2

print(a < b)  # 小于
print(a > b)  # 大于
print(a >= b)  # 大于等于
print(a <= b)  # 小于等于
print(a == b)  # 等于
print(a != b)  # 不等于
```

    True
    False
    False
    True
    False
    True


<font size=3>

  ###  **且 使用' and '**  
两者或多者全部符合为真反之为假  
当有一个为假时python将停止判断直接输出  
该方式为“短路计算”  
  ###  **或 使用 ' or '**  
两者或多者有一者符合即为真，全部为假才是假 
  ###  **非 使用' not '**  
表示非,不是，相反的 
  ###  **"属于" 使用 ' in '**  
在字符串、字典、元组、数值等类型中可以用'in'和'not in'  
判定值是否在该类型中 
 相对应属于 在……中  
  ###  **"不属于" 使用 'not in '**  
在字符串、字典、元组、数值等类型中可以用'in'和'not in'  
判定值是否在该类型中 
 相对应不属于 不在……中
  </font>


```python
x = False
y = True
z = 'abcdef'
w = 'a'
print(x and y)   # 且
print(x or y)  # 或
print(not x)  # 非
print(w not in z)  # 不属于
print(w in z)  # 属于
```

    False
    True
    True
    False
    True


## 数值缩写方式
***
<font size=3>

  变量	=	变量	运算	表达式		演变成		变量	运算	=	表达式	  (两者相同)
***
  ###  **自加 使用' += '**  

  ###  **自减 使用' -= '**  
  ###  **自乘 使用' \*= '** 
  ### **自除 使用' /= '**  
  ### **自幂 使用' \*\*= '**  
  ### **自模 使用' %= '**
  ### **自整除 使用 ' //= '**



```python
a = a + 1 == a += 1
a = a - 1 == a -= 1
a = a * 1 == a *= 1
a = a / 1 == a /= 1
a = a ** 1 == a **= 1
a = a % 1 == a %= 1
a = a // 1 == a //= 1
```

## 各个运算的优先级
***
与我们小学数学的先乘除后加减相类似
***
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210224155421480.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTYyMzA5Mw==,size_16,color_FFFFFF,t_70)





> 参考资料:  
> [python基础 基础运算符与表达式](https://blog.csdn.net/weixin_45623093/article/details/104924638)

注：以上内容如有问题请及时留言，会立即处理！直接提issue就行
