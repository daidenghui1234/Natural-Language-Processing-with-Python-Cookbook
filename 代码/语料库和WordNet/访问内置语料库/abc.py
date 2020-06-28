#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time       : 2020/6/28 23:28
# @Author     : 代登辉
# @Email      : 3276336032@qq.com
# @File       : abc.py
# @Software   : PyCharm
# @Description: 访问abc语句库

from nltk.corpus import abc

files = abc.fileids()
print(files)

wordsRural = abc.words(['rural.txt'])
print(wordsRural)

word20 = abc.words(['rural.txt'])[:20]
print(word20)

# abcGenres = abc.categories()
# print(abcGenres)

for w in abc.words(['science.txt']):
    print(w + ' ', end=' ')
    if w is '.':
        print()

