'''
http://ecos.bok.or.kr/api/StatisticSearch/AuthKey/xml/kr/1/10/060Y001/DD/20110101/20130101/010101000/?/?/
CommonURL : http://ecos.bok.or.kr/api
Service Name : /StatisticSearch
AuthKey : /AuthKey
Datatype : /xml /json
Language : /kr
Request Start : /1
Request End : /10
Statistic Code : 060Y001
Request Cycle : DD / MM / YY
Search Start Date : 20110101
Search End Date : 20130101
Item Code1 : 010101000
Item Code2 : ?
Item Code3 : ?
'''

import requests as re;
import json as js;
import matplotlib.pyplot as plt;
import datetime;
from collections import OrderedDict;
from pprint import pprint;

CommonURL = 'http://ecos.bok.or.kr/api'
ServiceName = '/StatisticSearch'
AuthKey = '/VW6RCULG0E8IQUE684SN'
RequestDataType = '/json'
RequestLanguage = '/kr'
RequestStart = '/1'
RequestEnd = '/5905'
RequestStaticCode = '/060Y001'  #Daliy Bank Rate
RequestCycle = '/DD'
RequestStartDate = '/19800101'
RequestEndDate = '/20180101'
ItemCode1 = '/010101000' #Daliy Bank Code
ItemCode2 = '/?'
ItemCode3 = '/?'

TargetUrl = CommonURL + ServiceName + AuthKey + RequestDataType + RequestLanguage + RequestStart + RequestEnd + RequestStaticCode + RequestCycle + RequestStartDate + RequestEndDate + ItemCode1 + ItemCode2 + ItemCode3

def GetTotalNumberOfItem(targetURL,targetServiceName):
    htmlRes = re.get(targetURL)
    htmlText = htmlRes.text
    parsedHtml = js.loads(htmlText)
    return parsedHtml[targetServiceName]['list_total_count'];



DailyRatioList = [];
DailyRatioDate = [];

print(TargetUrl);
res = re.get(TargetUrl);
resData = res.text;
#print(res.text);

parsedDicData = js.loads(resData); # json text to dic

totalNum = GetTotalNumberOfItem(TargetUrl,'StatisticSearch')

print(parsedDicData['StatisticSearch']['row'][1])
print(parsedDicData['StatisticSearch']['row'][1]['TIME'])
print(parsedDicData['StatisticSearch']['row'][1]['DATA_VALUE'])

'''
for i in range(1, totalNum-2):
    tempTime = parsedDicData['StatisticSearch']['row'][i]['TIME'];
    tempValue = parsedDicData['StatisticSearch']['row'][i]['DATA_VALUE'];
    print(i, tempTime , tempValue)
    DailyRatioList.append([tempTime, tempValue]);
'''
for i in range(1, totalNum-1):
    tempTime = parsedDicData['StatisticSearch']['row'][i]['TIME'];
    tempValue = parsedDicData['StatisticSearch']['row'][i]['DATA_VALUE'];
    DailyRatioList.append(float(tempValue));
    convertedTime = datetime.datetime.strptime(tempTime,"%Y%m%d").date()
    print(convertedTime);
    DailyRatioDate.append(convertedTime);
    #DailyRatioList.append([tempTime, tempValue]);

#print(DailyRatioList)
#print(DailyRatioList[0])


plt.figure(dpi=200)
plt.plot(DailyRatioDate,DailyRatioList);
plt.gcf().autofmt_xdate()

plt.xlabel('Daily Ratio');
plt.ylabel('Date');
plt.title('Daily Ratio');
plt.show();




#print(parsedJs)
#jsonString = js.dumps(parsedJs,indent=4) # json dic to str
#jsonString = jsonString.encode('utf-8').decode('euc-kr');
#print(jsonString)
#print(type(jsonString))





#print(resData);


