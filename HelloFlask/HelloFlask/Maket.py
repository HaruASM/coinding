
class Market:

    def __init__(self, name, api):
        self.marketname=name
        self.TradableCoin=[]
        self.API= api

        if self.API == None:
            print("Error : API is not created"+__LINE__)
        
    def GetBookInfo(self):        
        #BookInfo읽어오는 code구현
        return BookInfo

    def TradableCoin(self):
        #거래가능한 coin list읽어오는 code구현        

        return self.TradableCoin

    def SetAPI(self, api):
        self.API= api

