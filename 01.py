from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page1.html") # 导入urlopen函数向服务器发起请求获取HTML页面
bs = BeautifulSoup(html.read(),"html.parser") # 使用BeautifulSoup解析HTML页面

print(bs.h1)
