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
from multiprocessing import Pool
import time




def recomend(star_url, path):
    with open(path,'a') as f:
        for k,v in star_url.items():
            p = Pool(3)
            star_name = k    #明星名字
            print('======='+star_name+'=======')
            relation_list = [] # 解析的明星relation列表
            movie_url = [] # 解析明星的movieurl列表
            show_url = [] # 解析明星的showurl列表

            full = {} # each line {star_name:full_relation}
            full_relation=[] # 一条总记录
            movie_dic={} # 解析的movie推荐列表
            show_dic={} # 借些的show推荐列表

            # print(v)
            data = lurl.load(v)
            if data == None:
                with open('log','a') as f1:
                    f1.write('明星url_load失败:')
                    f1.write(k+':'+v+'\n')
                continue
            #解析结果：relation，movieurl，showurl
            # relation_list=analysis.get_relations(data)
            relation_list = p.apply_async(analysis.get_relations, args=(data,)).get()
            # movie_url=analysis.get_movieurl(data)
            movie_url=p.apply_async(analysis.get_movieurl, args=(data,)).get()
            # show_url=analysis.get_showurl(data)
            show_url=p.apply_async(analysis.get_showurl, args=(data,)).get()
            # print(show_url)
            p.close()
            p.join()

            # relation 结果存储 {relation:[name...}
            if len(relation_list)!=0:
                tmp_dict={}
                tmp_list=[]
                print('relation')
                for i in relation_list:
                    for j in i.keys():
                        tmp_list.append(i[j])
                tmp_dict['relation']=tmp_list
                full_relation.append(tmp_dict)
                print('relation_over')

            p2 = Pool(2)
            #load movieurl列表并解析
            if movie_url != None:
                print('movie')
                movie_set = p2.apply_async(get_movieset, args=(movie_url, )).get()
                # 把该明星名字从列表中去除
                if movie_set != '' and star_name in movie_set:
                    movie_set.remove(star_name)
                movie_list=list(movie_set)
                movie_dic['movie']=movie_list
                if len(movie_dic['movie']) != 0 and movie_dic['movie'] != None:
                    full_relation.append(movie_dic)
                    print('movie_over')

            # load showurl列表并解析
            if show_url!= None:
                print('show')
                show_set=p2.apply_async(get_showset, args=(show_url, )).get()
                # 20171228新加的还没尝试(过滤重复名字)
                if show_set != '' and star_name in show_set:
                    show_set.remove(star_name)
                show_list=list(show_set)
                # print(show_list)
                show_dic['show'] = show_list
                if len(show_dic['show']) != 0 and show_dic['show'] != None:
                    full_relation.append(show_dic)
                    print('show_over')
            p2.close()
            p2.join()
            if len(full_relation)!=0:
                full[star_name]=full_relation
                data = js.dumps(full, ensure_ascii=False)
                f.write(data+'\n')
            else:
                with open('None_recommend_list','a') as f3:
                    f3.write(k+':'+v+'\n')

def get_movieset(movie_url):
    movie_set = set()
    # 逐一借些movie的url
    for url in movie_url:
        # print(url)
        tmpset = analysis.analysis_movieurl(url)
        # print(tmpset)
        if tmpset != None and len(tmpset) != 0:
            movie_set = movie_set | tmpset
        else:
            continue
    return movie_set
def get_showset(show_url):
    show_set = set()
    for url in show_url:
        # print(url)
        tmpset2 = analysis.analysis_showurl(url)
        # print(tmpset2)
        if tmpset2 != None and len(tmpset2) != 0:
            show_set = show_set | tmpset2
        else:
            continue
    return show_set

if __name__=='__main__':
    start_time = time.time()
    # 1. 获取推荐列表（人名）
    path1 = '/Users/zhangwei/Desktop/sina_job/recommend/oid_name_type/20180107.txt'  # 每次运行修改
    path2 = '../res_container/res13'  # 每次运行修改
    # {starname:url}
    full = []
    full.append(star.get_mingxingurl_dict(path1))
    full.append(star.get_yinyueurl_dict(path1))
    # star_url = star.get_mingxingurl_dict(path)  # 明星
    # star_url = star.get_yinyueurl_dict(path)  # 音乐
    # star_url = star.getmingxingurl_test() # 测试用例
    for i in full:
        recomend(i, path2)
    # 2. 获取oid推荐列表
    path3 = mkdir.mkdir('../recommend_container/recommend7/')# 每次运行修改
    # path3_3 = './recommend_container/recommend7/'# 修改
    name_oid.name_oid(path1, path2, path3)
    # 3. 增加反向关系，得到最终的列表
    add.ad_re_relation(path3)
    # 4.统计结果
    count.count(path3)
    end_time = time.time()
    print('程序运行了：' + (end_time - start_time) / 60 + '分钟')
