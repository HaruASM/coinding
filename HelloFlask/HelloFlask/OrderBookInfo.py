

class OrderBookInfo:

    def __init__(self, api):
        self.m_lask=[]
        self.m_lbid=[]
        self.API= api

        if self.API == None:
            print("Error : API is not created"+__LINE__)
        
    def MakeOrderBookInfo(self):
        #API로 HTTP통신을 통해 실제 거래소 정보를 읽어오는 code구현

        #읽어들인 data를 ask와 bid list로 나누어서 저장
        return BookInfo

    def GetAskList(self):
        return m_lask

    def GetBidList(self):
        return m_lbid

    