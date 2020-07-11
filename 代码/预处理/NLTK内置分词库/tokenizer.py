#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time       : 2020/7/11 17:37
# @Author     : 代登辉
# @Email      : 3276336032@qq.com
# @File       : tokenizer.py
# @Software   : PyCharm
# @Description: 分词

# 导入相应库
from nltk.tokenize import LineTokenizer, SpaceTokenizer, TweetTokenizer
from nltk import word_tokenize

text = "My name is Maximus Decimus Meridius, commander of the Armies of the North, General of the Felix Legions and " \
       "loyal servant to the true emperor, Marcus Aurelius. \nFather to a murdered son, husband to a murdered wife. " \
       "\nAnd I will have my vengeance, in this life or the next. "
ITokenizer = LineTokenizer()
print("按照换行分词 ", ITokenizer.tokenize(text))

rawText = "By 11 o'clock on Sunday, the doctor shall open the dispensary."
sTokenizer = SpaceTokenizer()
print("按照空格符分词 :", sTokenizer.tokenize(rawText))      # 表达符号和单词连在一起
print("按照单词分词 ：", word_tokenize(rawText))     # 表达符号和单词分开

tweet = "This is a cooool #dummysmiley: :-) :-P <3"
tTokenizer = TweetTokenizer()
print("处理特殊字符 ", tTokenizer.tokenize(tweet))