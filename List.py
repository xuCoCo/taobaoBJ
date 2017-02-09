#coding=utf-8
# 获取商品列表的数据，包含nid,总销量，价格
# 导入开发模块
import requests
import codecs
import json
from bs4 import BeautifulSoup
# 定义空列表，用于创建所有的爬虫链接
urls = []
# 拼接所有需要爬虫的链接
for j in list(range(0,99)): 
	urls.append('https://s.taobao.com/list?spm=5704.7773518.226594.41.RvraR8&source=youjia&q=摆件&bcoffset=0&p4poffset=5&sort=sale-desc&s='+bytes(j*60))
file=codecs.open('baijian','w','utf-8')
for url in urls:
	res = requests.get(url) # 发送get请求
	res = res.text.encode(res.encoding).decode('utf-8') # 需要转码，否则会有问题
	soup = BeautifulSoup(res,'html.parser') # 使用bs4模块，对响应的链接源代码进行html解析
	# 使用finalAll方法，获取页面商品列表
	page = soup.findAll('script')[6].text.split('\n')[2].replace('g_page_config =','',1).strip()[:-1]
	#  unicode转String
	utf8string=page.encode('utf-8')
	#  String 转json
	jo=json.loads(utf8string)
	auctions=jo['mods']['itemlist']['data']['auctions']
	for i in range(0,len(auctions)):
		nId=auctions[i]['nid']#主键
		commentCount=auctions[i]['comment_count']#总销量
		price=auctions[i]['view_price']
		file.write(','.join((nId,commentCount,price))+'\n')
file.close()