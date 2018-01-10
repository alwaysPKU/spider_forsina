import load_url as lurl
import get_stardict as star
import analysis
import json as js
import name_topicid as name_oid
import add_re_relation as add
import mkdir
import count

path1 = '/Users/zhangwei/Desktop/sina_job/recommend/oid_name_type/20180107.txt'  # 每次运行修改
path2 = '../res_container/res13'  # 每次运行修改
path3 = mkdir.mkdir('../recommend_container/recommend7/')# 每次运行修改
path3_3 = './recommend_container/recommend7/'# 修改

# 4.统计结果
count.count(path3)