import pandas as pd
import parsingMain as pm


naverStockURL = 'https://finance.naver.com/item/sise_day.nhn?code=005930&page=';



lastPageNum = pm.getLastPageNum(naverStockURL+'1');

print(lastPageNum);
print(type(lastPageNum));


tempDataFrame = pd.DataFrame();
DataList = [];
for i in range(1,int(lastPageNum)):
    newStockURL = naverStockURL + str(i);
    tempDataFrameList = pd.read_html(newStockURL);
    tempStockDataFrame = tempDataFrameList[0];
    tempStockDataFrame = tempStockDataFrame.dropna();
    DataList.append(tempStockDataFrame);


print('DataList');
print(DataList);


'''

#print(naverStockURL);





naverStockData = pd.read_html(naverStockURL,header=0);

stockDataFrame = naverStockData[0];


stockDataFrame = stockDataFrame.dropna();


print(stockDataFrame);
print(stockDataFrame.종가);
#print(stockDataFrame.iloc[0]);
#print(stockDataFrame['종가']);
#print(stockDataFrame['날짜']);




#print(stockDataFrame.iloc[0]);


#print(stockDataFrame.loc[:'2018.09.28']);
'''








