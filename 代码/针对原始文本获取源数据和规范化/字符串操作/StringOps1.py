#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time       : 2020/7/3 16:31
# @Author     : 代登辉
# @Email      : 3276336032@qq.com
# @File       : StringOps1.py
# @Software   : PyCharm
# @Description: 字符串操作

nameList = ['Tuffy', 'Ali', 'Nysha', 'Tim']   # 字符串列表
sentence = 'My dog sleeps on sofa'  # 字符串对象

# join()函数可以被当作任意一个string对象调用，它的输入参数是一个str对象的列表。
# 通过调用字符串的内容作为连接分割符，他将所有str的对象连接成str对象，并返回链接后的对象
names = ';'.join(nameList)
print(type(names), ' : ', names)

# split 函数调用一个字符串时，它会将其内容分割成多个str对象，创建一个包含这些字符串对象的列表
# 并返回该列表。该函数接受单个str对象作为参数，表示分隔符。
wordList = sentence.split(' ')
print(type(wordList), ' : ', wordList)

additionExample = 'ganehas' + 'ganesha' + 'ganesha'
multiplicationExample = 'ganesha' * 2;
print('Text Additions:', additionExample)
print('Text Multiplication :', multiplicationExample)

str1 = 'Python NLTK'
print(str1[1])
print(str1[-3])


