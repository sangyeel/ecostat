import pandas
import os
'''
Stock code data from Savedstock folder.
those excel file(xls) from https://kind.krx.co.kr/corpgeneral/corpList.do?method=loadInitPage
So those file sometimes need update from upper website.(if new company registered in KOSPI,KONEX,KOSDAQ)
that excel file is database
the xls file binary looks like html. So, read_heml method will be used in Pandas
형식                                 확장명        설명
Excel 통합 문서                      .xlsx         Office Excel 2007 기본 파일 형식으로, VBA 매크로 코드를 저장할 수 없습니다.
Excel 매크로 사용 통합 문서           .xlsm         Office Excel 2007 파일 형식으로, VBA 매크로 코드를 포함하여 저장할 수 있습니다.
Excel 바이너리 통합 문서              .xlsb         Office Excel 2007 이진 파일 형식(BIFF12)입니다.
서식 파일                            .xltx         Excel 서식 파일의 기본 Office Excel 2007 파일 형식으로, VBA 매크로 코드를 저장할 수 없습니다.
Excel 매크로 사용 서식 파일           .xltxm        Excel 서식 파일의 Office Excel 2007 파일 형식으로, 매크로를 포함할 수 있으며, VBA 매크로 코드를 저장할 수 있습니다.
Excel 97 - Excel 2003 통합 문서      .xls          Excel 97 - Excel 2003 이전 파일 형식입니다.
Excel 97 - Excel 2003 서식 파일      .xlt          Excel 서식 파일의 Excel 97 - Excel 2003 이진 파일 형식입니다.
Microsoft Excel 5.0 / 95 통합 문서   .xls          Excel 5.0/95 이진 파일 형식입니다.
XML 스프레드시트 2003                .xml           XML 스프레드시트 2003 파일 형식입니다.
XML 데이터                           .xml          XML 데이터 형식입니다.
Microsoft Office Excel 추가 기능     .xlam         Office Excel 2007 추가 기능으로, 매크로를 포함할 수 있습니다
'''
class StockCodeSearch:
    __SAVEDIR = 'SavedStock'
    def __init__(self):
        #self.df = pandas.read_excel(os.path.join(StockCodeSearch.__SAVEDIR,"total.xls"),sheet_name="total")

        self.df = pandas.read_html(os.path.join(StockCodeSearch.__SAVEDIR,"total.xls"))
        #print(self.df)
        print(type(self.df))
        print(self.df[0])




total = StockCodeSearch()
