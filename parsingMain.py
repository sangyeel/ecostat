import bs4 as bs;
import requests as re;

def getLastPageNum(naverStocURLFirstPage):
    with re.get(naverStocURLFirstPage) as res:
        htmlData = res.text;
        soup = bs.BeautifulSoup(htmlData,'lxml');

    LastLink = soup.select('.pgRR');#last page css class
    #print(LastLink);

    LastLinkStr = (LastLink[0].find('a')['href'])
    #print(LastLinkStr.split('page=')[1]);
    LastPageNum = LastLinkStr.split('page=')[1];
    return LastPageNum;







