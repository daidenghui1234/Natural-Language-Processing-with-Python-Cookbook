#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time       : 2020/7/10 19:38
# @Author     : 代登辉
# @Email      : 3276336032@qq.com
# @File       : rssReader.py
# @Software   : PyCharm
# @Description: 方法描述,必填
import feedparser

myFeed = feedparser.parse("http://feeds.mashable.com/Mashable")
print('Feed Title :', myFeed['feed']['title'])
print('Number of posts :', len(myFeed.entries))
post = myFeed.entries[0]
print('Post Title :', post.title)
content = post.content[0].value
print('Raw content :\n', content)