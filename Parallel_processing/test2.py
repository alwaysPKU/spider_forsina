import load_url as lurl
import get_stardict as star
import analysis
import json as js
import name_topicid as name_oid
import add_re_relation as add
import mkdir
import count
import Parallel_processing.recommend_main as recommend

path1 = '/Users/zhangwei/Desktop/sina_job/recommend/oid_name_type/test.txt'  # 每次运行修改
path1_1='/Users/zhangwei/Desktop/sina_job/recommend/oid_name_type/20180114.txt'
path2 = '../res_container/test'  # 每次运行修改
# path3 = mkdir.mkdir('../recommend_container/recommend7/')# 每次运行修改
# path3_3 = './recommend_container/recommend7/'# 修改

path3 = mkdir.mkdir('../recommend_container/test/')# 每次运行修改
# print(type(path3))
# print(path3)
full = []
full.append(star.get_mingxingurl_dict(path1))
full.append(star.get_yinyueurl_dict(path1))
# star_url = star.get_mingxingurl_dict(path)  # 明星
# star_url = star.get_yinyueurl_dict(path)  # 音乐
# star_url = star.getmingxingurl_test() # 测试用例
for i in full:
    recommend.recomend(i, path2)
# path3_3 = './recommend_container/recommend7/'# 修改#注意逻辑这里是错的
name_oid.name_oid(path1_1, path2, path3)
# 3. 增加反向关系，得到最终的列表
add.ad_re_relation(path3)
# 4.统计结果
count.count(path3)
