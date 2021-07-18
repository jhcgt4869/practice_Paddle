#  -*- coding:utf-8 -*-
# Author:三岁 2021.7.18
# Narcissistic number(水仙花数）

'''
水仙花数说明：
水仙花数指的是一个3位数，各位上的立方和为他本身。
举例：1^3+5^3+3^3=153
'''

print("所有三位数中的水仙花数如下所示：")
SingleDigit = TenDigits = Hundred = Surplus = sum = 0
for i in range(100, 1000):
    Hundred = i // 100
    Surplus = i % 100
    TenDigits = Surplus // 10
    SingleDigit = Surplus % 10
    if i == ((Hundred ** 3) + (TenDigits ** 3) + (SingleDigit ** 3)):
        sum += 1
        print(i)
print("共有%s个" % sum)
