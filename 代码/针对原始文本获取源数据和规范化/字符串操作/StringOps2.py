#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time       : 2020/7/3 17:28
# @Author     : 代登辉
# @Email      : 3276336032@qq.com
# @File       : StringOps2.py
# @Software   : PyCharm
# @Description: 字符串操作

str1 = 'NLTK Dolly Python'
print('Substring end at :', str1[:4])
print('Substring starts from :', str1[11:])
print('Substring :', str1[5:11])

if 'NLTK' in str1:
    print('found NLTK')

# replaced 函数只需要两个参数。第一个是需要被替换的字符串，第二个是用来替换前面字符串的新字符串。
# replaced 函数 返回一个新的sting对象，并且它不会修改调用它的字符串。
replaced = str1.replace('Dolly', 'Dorothy')
print('Replaced String: ', replaced)

print('Accessing each character')
for s in replaced:
    print(s)