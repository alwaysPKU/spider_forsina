import urllib.request

def load(url):
	if url == None:
		return None
	try:
		response = urllib.request.urlopen(url, timeout=60)
		if response.getcode==200:
			return None
		return response.read()
	except Exception as e:
		with open('log','a') as f:
			f.write('错误url : '+url+'-'+str(e)+'\n')
		return None


# 写html
def write_html(star_name,html):
	if html is not None:
		with open(star_name,'w') as f:
			f.write(html)


url = "https://baike.baidu.com/item/"+urllib.request.quote("舒畅")
print(url)

data = load(url).decode("utf-8")
with open("./shuchang", "w") as f:
	f.write(data)
