
#test용 data인 market name
BaseMarketName= "Kuko"

class TradingSystem:
    def __init__(self):
        self.mBaseMarket= CreateMarket(BaseMarketName)
        self.name=""


    def CreateMarket(self, name):
        #Market별로 상이한 API를 생성하고 Market instance를 생성한다.

        if(self.name in BaseMarketName):            
            print("Kuko market created")

        