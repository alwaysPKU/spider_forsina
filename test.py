
path = '/Users/zhangwei/PycharmProjects/spider_mingxing/20171123.txt'

# star_list = star.get_yinyueurl_dict(path)
# print(len(star_list))
# print(star_list)

with open(path) as f:
    line = f.readline()
    n=0
    while line:
        item = line.split()
        if len(item) == 3 and item[2] == 'CP':
            n = n+1
            print(line, n)
        line = f.readline()




