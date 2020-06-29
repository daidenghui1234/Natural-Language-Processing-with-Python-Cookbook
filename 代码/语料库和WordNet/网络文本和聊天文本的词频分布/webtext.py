#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time       : 2020/6/29 16:31
# @Author     : 代登辉
# @Email      : 3276336032@qq.com
# @File       : webtext.py
# @Software   : PyCharm
# @Description: 对webtext语料库进行访问

# 导入所需库打印组织文件名称
import nltk
from nltk.corpus import webtext
print(webtext.fileids())

# 访问个人广告数据的文件，并对该文件计算频率分布
fileid = 'singles.txt'
wbt_word = webtext.words(fileid)
fdist = nltk.FreqDist(wbt_word)

# fdist.max()：显示最常见单词 fdist[fdist.max()]：该词的计数
print('Count of the maximum appearing token "', fdist.max(), '" :', fdist[fdist.max()])

# fdist.N()：得到频率分布包中不同单词的的计数
print('Total Number of distinct tokens in the bag : ', fdist.N())

# 找出所在语料库中最常见的10个单词
print("Following are the most common 10 words in the bag")
print(fdist.most_common())

# fdist.tabulate()将整个频率分布制成表格
print('Frequent Distribution on Personal Advertisements')
print(fdist.tabulate())

# 使用fdist.plot()画出积累词频的频率分布
fdist.plot(cumulative=True)
