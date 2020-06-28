#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 20:13
# @Author  : 代登辉
# @Email   : 3276336032@qq.com
# @File    : reuters.py
# @Software: PyCharm

# NLTK数据库集中访问路透社语料库的特定方式
from nltk.corpus import reuters

# 查看语料库中的内容
files = reuters.fileids()
print(files)

# 访问具体文件的内容
word16097 = reuters.words(['test/16097'])
print(word16097)

# 获取指定长度的单词列表
word20 = reuters.words(['test/16097'])[:20]
print(word20)

# 输出主题列表
reutersGenres = reuters.categories()
print(reutersGenres)

# 访问主题的内容并打印
for w in reuters.words(categories=['bop', 'cocoa']):
    print(w+' ', end=' ')
    if w is '.':
        print()
