#  -*- coding:utf-8 -*-
# Author:三岁 2021.7.25

''''
华氏度转摄氏度
℃ = (οF - 32) / 1.8
摄氏度转华氏度
°F = (9/5)*°C + 32
'''

fahrenheit = eval(input('输入华氏度：'))
degree = (fahrenheit - 32) / 1.8
print('对应的摄氏度为：%.2f℃' % degree)

degree = eval(input("输入摄氏度："))
fahrenheit = (9/5) * degree + 32
print("对应的华氏度是：%.2f℉\n" % fahrenheit)

'''
说明：
这个和之前的英尺米转换类似
'''