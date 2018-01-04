import json as js
with open('./recommend5/recommend_list') as f:
    line = f.readline()
    full_count={}
    full_count['relation']=0
    full_count['movie']=0
    full_count['show']=0
    while line:
        item = js.loads(line)
        for k,v in item.items():
            for i in v:
                for k2,v2 in i.items():
                    full_count[k2]=full_count[k2]+len(v2)
        line=f.readline()

print(full_count)
