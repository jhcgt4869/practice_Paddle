#  -*- coding:utf-8 -*-
# Author:三岁 2021.7.11

###############  first inning：单纯的输入输出  ###########
print('first inning:基本输入输出')
print("***********输入************")
name = input("输入你的名字")
height = input("输入你的身高")
age = input("输入你的年龄")

print("***********输出************")
print("姓名:%s\n身高：%s\n年龄：%s\n" % (name, height, age))
# 由于输入数据是属于字符串这里只能够是%s


########### the second round ：在上面输入输出的基础上添加强制转换（身高和年龄)  ######
print('the second round：使用float和int强制转换')
print("***********输入************")
name = input("输入你的名字")
height = float(input("输入你的身高"))  # 强制转换成浮点型
age = int(input("输入你的年龄"))  # 强制转换成整型

print("***********输出************")
print("姓名:%s\n身高：%.2f\n年龄：%d\n" % (name, height, age))  # 身高保留两位小数


########### third round ：在上面输入输出的基础上使用eval()函数进行转换  ######
print('third round：使用eval()进行强制转换')  # eval()的使用会在后期说明
print("***********输入************")
name = input("输入你的名字")
height = eval(input("输入你的身高"))  # 强制转换成对应类型
age = eval(input("输入你的年龄"))  # 强制转换成对应类型

print("***********输出************")
print("姓名:%s\n身高：%.2f\n年龄：%d\n" % (name, height, age))  # 身高保留两位小数


'''
内容说明：
这里分成了3部分，分别是正常的输入输出，然后是有强制转换的，有eval()函数的强制转换
强制转换、数据类型和eval()、format()等会在后期说明
有什么问题可以直接提issue(不懂的也可以）
'''
