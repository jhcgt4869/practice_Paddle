#  -*- coding:utf-8 -*-
# Author:三岁 2021.7.25

''''
英尺转换为千克
（英尺+（英寸/12））* 0.03048
'''

foot = eval(input('请输入需要转换的英尺：'))
inch = eval(input('请输入需要转换的英寸：'))
kilo = (foot + (inch / 12)) * 0.3048
print('对应的高度为：%.2f米' % kilo)

'''
解析：
使用input获取输入的英尺和英寸的值
使用eval()实例化值的类型（后期会进行介绍）
计算后输出
'''

# print('对应的高度为：{}米'.format(kilo))  # format显示
# print(f'对应的高度为：{kilo}米' # format缩写显示
