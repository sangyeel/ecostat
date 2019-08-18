import requests
import bs4
import re
import os
import pandas
#https://finance.naver.com/item/sise_day.nhn?code=215600
class NaverStockData:
    __URL = 'https://finance.naver.com/item/sise_day.nhn?code='
    __SAVEDIR = "SavedStock"
    # self.stockCode
    # self.lastPageNum
    # self.totalStockList
    def __init__(self,stockCode):
        self.stockCode = stockCode
        self.lastPageNum = 0
        self.totalStockList = []
        self.get_last_page_number()
        self.get_stock_data_with_data_frame()

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
        print (targetUrl)
        print (self.lastPageNum)

    def make_dir_for_save_csv(self):
        if not(os.path.isdir(NaverStockData.__SAVEDIR)):
                os.makedirs(os.path.join(NaverStockData.__SAVEDIR))


    def get_stock_data(self):
        for i in range(1,self.lastPageNum):
            res = requests.get(NaverStockData.__URL + self.stockCode + '&page=' + str(i))
            bs4Obj = bs4.BeautifulSoup(res.text,'html.parser')
            stockObj = bs4Obj.find_all('span',class_='tah p11')
            self.totalStockList.append(stockObj)


    def get_stock_data_with_data_frame(self):
        self.make_dir_for_save_csv()
        #for i in range(1,self.lastPageNum):
        for i in range(1,2):
            tempDataFrameList = pandas.read_html(NaverStockData.__URL + self.stockCode + '&page=' + str(i))
            tempDataFrame = tempDataFrameList[0]
            tempDataFrame.to_csv(NaverStockData.__SAVEDIR+'\\'+self.stockCode+'.csv',mode='a')

'''
datafame from naver has 2 table
1 is data table
2 is pagenation table
So we parsed the 0 table, means data
'''




samsungStock = NaverStockData('005930');
