#  -*- coding:utf-8 -*-
# Author:三岁 2021.7.18

'''
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''

# 方法一
count = 0  # 计数
for a in range(1, 5):
    for b in range(1, 5):
        for c in range(1, 5):
            if (a != b) and (b != c) and (a != c):
                print(100 * a + 10 * b + c)
                count += 1
print(f'一共有{count}种')

'''
方法一解析：
分别循环1-4
然后判定具体的内容
选择输出（把给个位置进行拼接）
'''
print('--------------------------')
# 方法二：使用迭代器函数
import itertools

count = 0
a = [1, 2, 3, 4]
for i in itertools.permutations(a, 3):
    print(i[0] * 100 + i[1] * 10 + i[2])
    count += 1
print(f'一共有{count}种')

'''
方法二解析：
使用了迭代器函数
高效处理和解析了内容
具体的解析请查看下面的链接或提issue
'''
# 具体解析请查看：https://blog.csdn.net/weixin_45623093/article/details/113177709
