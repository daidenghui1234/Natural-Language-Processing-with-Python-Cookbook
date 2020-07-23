#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time       : 2020/7/11 18:16
# @Author     : 代登辉
# @Email      : 3276336032@qq.com
# @File       : Gutenberg.py
# @Software   : PyCharm
# @Description: 停用词

import nltk
from nltk.corpus import gutenberg
print(gutenberg.fileids())

gb_words = gutenberg.words('bible-kjv.txt')
words_filtered = [e.lower() for e in gb_words if len(e) >= 3]     # 去除长度小于3的单词
stopwords = nltk.corpus.stopwords.words('english')
words = [w for w in words_filtered if w.lower() not in stopwords]

fdist = nltk.FreqDist(words)
fdist2 = nltk.FreqDist(gb_words)

print('Following are the most common 10 words in the bag')
print(fdist2.most_common(10))
print('Following are the most common 10 words in the bag minus the stopwords')
print(fdist.most_common(10))
fdist.plot(cumulative=True)