#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time       : 2020/6/29 19:42
# @Author     : 代登辉
# @Email      : 3276336032@qq.com
# @File       : polysetmy.py
# @Software   : PyCharm
# @Description: 基于WordNet计算名词动词形容词和副词的平均多译性

from nltk.corpus import wordnet as wn
type = 'n'

# 返回WordNet数据库中名词类型的所有同义词集
synsets = wn.all_synsets(type)

# 用嵌套的for循环迭代同义词集（synsets）列表和每个同义词集（synset）中的词条（laemma）列表并将它们添加到词条（lammas）大列表中
lemmas = []
for synset in synsets:
    for lemma in synset.lemmas():
        lemmas.append(lemma.name())

# 删除重复项
lemmas = set(lemmas)

count = 0
for lemma in lemmas:
    count = count + len(wn.synsets(lemma, type))

print('Total distinct lemmas: ', len(lemmas))
print('Total senses :', count)
print('Average Polysemy of ', type, ': ', count/len(lemmas))