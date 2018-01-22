# 从名单直接拼接url爬取所需内容
# 直接输出对应name的推荐列表
import load_url as lurl
import get_stardict as star
import analysis
import json as js
import name_topicid as name_oid
import add_re_relation as add
import mkdir
import count
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


# path1 = '/Users/zhangwei/Desktop/sina_job/recommend/oid_name_type/20180107.txt'  # 每次运行修改
# path2 = './res_container/res11'  # 每次运行修改
# # 2. 获取oid推荐列表
#
# path3 = mkdir.mkdir('./recommend_container/recommend6/')# 每次运行修改
# print(type(path3))
# name_oid.name_oid(path1, path2, path3)
# # 3. 增加反向关系，得到最终的列表
# add.ad_re_relation(path3)
# # 4.统计结果
# count.count(path3)

# html = urlopen('http://www.baidu.com')
# data = html.read()
# print(type(html))
# print(type(data))
# data = BeautifulSoup(html, 'html.parser')
# data1 = BeautifulSoup(data, 'html.parser')
l = ['林心如', '霍建华', '林心', '赵薇', '林心如', '尔康', '小燕子']

addr_to = list(set(l))
print(addr_to)
addr_to.sort(key=l.index)
print(addr_to)



