class KoreaBankRequestor:
    cUrlTuple = ('http://ecos.bok.or.kr/api','StatisticSearch')
    CommonURL = 'http://ecos.bok.or.kr/api'
    ServiceName = '/StatisticSearch'
    AuthKey = '/VW6RCULG0E8IQUE684SN'
    RequestDataType = '/json'
    RequestLanguage = '/kr'
    mRequestStart = '/1'
    mRequestEnd = '/5905'
    mRequestStaticCode = '/060Y001'  # Daliy Bank Rate
    mRequestCycle = '/DD'
    mRequestStartDate = '/19800101'
    mRequestEndDate = '/20180101'
    mItemCode1 = '/010101000'  # Daliy Bank Code
    mItemCode2 = '/?'
    mItemCode3 = '/?'
    def __init__(self, rReqStaticCode, rReqStartDate, rRequestEndDate, rReqItemCode1, rReqItemCode2, rReqItemCode3):
        self.reqStaticCode = rReqStaticCode
        self.reqStartDate = rReqStartDate
        self.reqEndDate = rRequestEndDate
        self.reqItemCode1 = rReqItemCode1
        self.reqItemCode2 = rReqItemCode2
        self.reqItemCode3 = rReqItemCode3


ratio = KoreaBankRequestor(1,2,3,4,5,6)

print(ratio.cUrlTuple[0])



