from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs = BeautifulSoup(html.read(),"html.parser")

for child in bs.find("table",{"id":"giftList"}).children: # 获取id属性值为giftList的第一个table标签的全部子标签
  print(child)
