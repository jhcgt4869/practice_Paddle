#  -*- coding:utf-8 -*-
# Author:三岁 2021.7.18

# 方法一
for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d * %d = %d" % (i, j, i * j), end='\t')
    print()

'''
方法一思路：
循环0-9得到我们的乘数1
在循环1-i得到我们的乘数2
修改换行变成‘\t’
在一行结束以后添加一个换行即可
'''
print('--------------------------------------------')
# 方法二：
print('\n'.join(['\t'.join(["%s * %s = %s" % (j, i, i * j) for j in range(1, i + 1)]) for i in range(1, 10)]))

'''
方法二说明：
使用办法是join模式然后使用了[]特殊方法
'''