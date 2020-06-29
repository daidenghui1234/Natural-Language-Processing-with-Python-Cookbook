#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time       : 2020/6/29 18:26
# @Author     : 代登辉
# @Email      : 3276336032@qq.com
# @File       : HypoNHypernyms.py
# @Software   : PyCharm
# @Description: 讨论上位词下位词

from nltk.corpus import wordnet as wn
woman = wn.synset('woman.n.01')
bed = wn.synset('bed.n.01')

# hypernyms() API函数返回具有直接关系的同义词集
# hypernym_paths() 返回一个集合列表，每个集合包含从根节点到woman同义词路径
print(woman.hypernyms())
woman_paths = woman.hypernym_paths()

# 打印从根节点到'woman.n.01'节点的路径
for idx, path in enumerate(woman_paths):
    print('\n\nHypernym Path :', idx + 1)
    for synset in path:
        print(synset.name(), ', ', end='')

# 获取同义词集bed.n.01的下位词并将其打印
types_of_beds = bed.hyponyms()
print('\n\nTypes of beds(Hyponyms): ', types_of_beds)

print('\n', sorted(set(lemma.name() for synset in types_of_beds for lemma in synset.lemmas())))