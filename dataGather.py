import requests
import bs4
import re

naverStockDataURL = 'http://finance.naver.com/item/sise_day.nhn?code='

stockCode = '005930'

print(naverStockDataURL + stockCode)

res = requests.get(naverStockDataURL+stockCode)

origHtml = res.text

bs4ObjHtml = bs4.BeautifulSoup(origHtml,'html.parser')


#print(res.text)

stockPrice = bs4ObjHtml.find_all('span',class_='tah p11')
pageNation = bs4ObjHtml.find('td',class_='pgRR')
lastPageURL = pageNation.find('a')['href']
lastPageNumReg = re.split('page=',lastPageURL)
lastPageNum = lastPageNumReg[1]
#lastPageNum=lastPageURL[lastPageNumReg.search(lastPageURL).end]
#lastPage = pageNation.find('a')


# bs4 find_all(name, attrs, recursive, string, limit, **kwargs) 
# print(stockPrice)
#print(pageNation[0])
print(lastPageNumReg)

print(lastPageNum)
#print(type(stockPrice))






