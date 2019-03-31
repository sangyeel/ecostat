import requests
import bs4
import re
#https://finance.naver.com/item/sise_day.nhn?code=215600
class NaverStockData:
    __URL = 'https://finance.naver.com/item/sise_day.nhn?code='
    # self.stockCode
    # self.lastPageNum
    # self.totalStock
    def __init__(self,stockCode):
        self.stockCode = stockCode
        self.get_last_page_number()
        self.get_stock_data()
   
    def get_last_page_number(self):
        # request first html for getting end page
        targetUrl = NaverStockData.__URL+self.stockCode + '&page=1'
        res = requests.get(targetUrl)
        bs4Obj = bs4.BeautifulSoup(res.text,'html.parser')
        # find last page number attr is 'pgRR'
        pageNation = bs4Obj.find('td',class_='pgRR')
        lastPageURL = pageNation.find('a')['href']
        lastPageNumReg = re.split('page=',lastPageURL)
        lastPageNum = lastPageNumReg[1]
        self.lastPageNum = str(lastPageNum)
        self.lastPageNum = int(self.lastPageNum)
        print targetUrl
        print self.lastPageNum
    
    def get_stock_data(self):
        for i in range(1,self.lastPageNum):
            res = requests.get(NaverStockData.__URL + self.stockCode + '&page=' + str(i))
            bs4Obj = bs4.BeautifulSoup(res.text,'html.parser')
            stockObj = bs4Obj.find_all('span',class_='tah p11')
            self.totalStock = self.totalStock + stockObj

        print self.totalStock
 
     





samsungStock = NaverStockData('005930');
