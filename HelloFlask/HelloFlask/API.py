
from GlobalVariable import *
import requests
from urllib.parse import urljoin

class BaseAPI:
    def __init__(self, priv, pub):
        self.private_key=priv
        self.public_key=pub
        self.BaseURL=None

    def GetTickers(self):
        raise NotImplementedError(__name__+ ": The method not implemented")

    def GetOrderBook(self):
        raise NotImplementedError(__name__+ ": The method not implemented")

    def GetBalance(self):
        raise NotImplementedError(__name__+ ": The method not implemented")

    def GetDepositAddress(self):
        raise NotImplementedError(__name__+ ": The method not implemented")

    def GetBuyOrder(self):
        raise NotImplementedError(__name__+ ": The method not implemented")

    def GetSellOrder(self):
        raise NotImplementedError(__name__+ ": The method not implemented")

    def GetOpenOrderCheck(self):
        raise NotImplementedError(__name__+ ": The method not implemented")

    def GetCancelOrders(self):
        raise NotImplementedError(__name__+ ": The method not implemented")

    def GetWithdrawal(self):
        raise NotImplementedError(__name__+ ": The method not implemented")


class KucoinAPI(BaseAPI):
    def __init__(self):        
        BaseAPI.__init__(self, gKeyPair[gMarketList[0]][0], gKeyPair[gMarketList[0]][1])
        self.BaseURL="https://api.kucoin.com/v1/open/"

        #$$$test
        self.testsymbol="btc-usdt"

    def GetOrderBook(self):
        #sess= requests.session()
        #res= sess.get(self.BaseURL+"orders")
        #api_url= self.BaseURL+"orders?symbol={symbol}"
        api_url= self.BaseURL+"orders?symbol="+self.testsymbol
        
        api_url.format(symbol= self.testsymbol)
        res= requests.get(api_url)
        res.raise_for_status()
        print(res.text)
        return res.text


class GateAPI(BaseAPI):
    def __init__(self):
        BaseAPI.__init__(self, gKeyPair[gMarketList[1]][0], gKeyPair[gMarketList[1]][1])
