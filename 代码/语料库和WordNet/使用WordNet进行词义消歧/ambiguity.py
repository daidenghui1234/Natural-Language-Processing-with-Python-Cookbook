#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time       : 2020/6/29 18:00
# @Author     : 代登辉
# @Email      : 3276336032@qq.com
# @File       : ambiguity.py
# @Software   : PyCharm
# @Description: 列出单词的所有含义

from nltk.corpus import wordnet as wn
chair = 'chair'

# 访问内部WordNet数据库的API接口，并获取与chair相关的所有含义
# WordNet吧每一个含义都定义为同义词集（Synsets）
chair_synsets = wn.synsets(chair)
print('Synsets/Senses of Chair :', chair_synsets, '\n\n')


for synset in chair_synsets:
    print(synset, ': ')
    print('Definition', synset.definition())
    print('Lemmas/Synonymous words:', synset.lemma_names())
    print('Example:', synset.examples(), '\n')
