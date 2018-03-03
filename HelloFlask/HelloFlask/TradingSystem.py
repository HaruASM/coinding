from Market import *
from GlobalVariable import *
from API import *
#test용 data인 market name



class TradingSystem:
    def __init__(self):
        self.mBaseMarket= self.CreateMarket(gBaseMarketName)
        self.mMarketList=[] #base market이외의 market들
        
        for market in gMarketList:
            if market != gBaseMarketName:
                self.mMarketList.append(self.CreateMarket(market))

    def CreateMarket(self, name):
        #Market별로 상이한 API를 생성하고 Market instance를 생성한다.      
        api= self.CreateAPI(name)

        if api == None:
            print(name+": API creation failed!!!")
            return None
        else:
            print(name+": API createion successful")            

        return Market(name, api)


    #$$$market market추가시 수정되어야할 코드
    #{string:class_name} 형태의 dic자료형으로 변환 가능한지 확인하면 코드 줄일수 있음
    def CreateAPI(self, name):
        if name in gMarketList[0]:
            return KucoinAPI()
        elif name in gMarketList[1]:
            return GateAPI()
        else:
            return None
            

    def GetOrderBookInfo(self, market):
        return market.GetBookInfo()

    def RunSimulation(self):
        print("Run simulation!!!")   
        #testing
        print(self.GetOrderBookInfo(self.mBaseMarket))
        

