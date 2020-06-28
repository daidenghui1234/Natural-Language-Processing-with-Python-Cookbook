#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time       : 2020/6/29 0:15
# @Author     : 代登辉
# @Email      : 3276336032@qq.com
# @File       : Brown WH.py
# @Software   : PyCharm
# @Description: 计算布朗语料库中三种类别不同的特殊疑问词

# 导入NLTK库和布朗语料库
import nltk
from nltk.corpus import brown

# 检查语料库中的类别
print(brown.categories())

# 创建列表
genres = ['fiction', 'humor', 'romance']
whWords = ['what', 'which', 'how', 'why', 'when', 'where', 'who']

for i in range(0, len(genres)):
    genre = genres[i]
    print()
    print("Analysing '" + genre + "' wh words")
    genres_text = brown.words(categories=genre)
    # FreqDist()函数接收一个单词列表并返回一个对象，该对象包含映射词（map word）
    # 及其输入单词列表中的相应频率。
    fDist = nltk.FreqDist(genres_text)

    for wh in whWords:
        print(wh + ':', fDist[wh], end=' ')
