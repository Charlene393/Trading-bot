import pandas as pdb

from td.client import TDClient
from td.utils import milliseconds_since_epoch

from datetime import datetime, time, timezone

from typing import List, Dict, Union

class PyRobot():

    def __init__(self, client_id: str, redirect_url:str, credentials_path:str = None, trading_account:str = None)-> None:
        self.trading_account: str = trading_account
        self.client_id: str = client_id
        self.redirect_url: str = redirect_url
        self.credentials_path: str = credentials_path
        self.session: TDClient = self._create_session()
        self.trades: dict={}
        self.historical_prices: dict ={}
        self.stock_frame = None

    def _create_session(self)-> TDClient:
        td_client = TDClient(
            client_id = self.client_id,
            redirect_url = self.redirect_url,
            credentials_path = self.credentials_path
        )

        #login to the session
        td_client.login()

        return td_client
    @property

    def pre_market_open(self) -> bool:
        pre_market_start_time = datetime.now().replace(hour =12, minute= 00, second= 00, tzinfo= timezone.utc).timestamp()
        market_start_time = datetime.now().replace(hour =13, minute= 30, second= 00, tzinfo= timezone.utc).timestamp()
        right_now = datetime.now().replace(tzinfo=timezone.utc).timestamp()

        if market_start_time >= right_now >=pre_market_start_time:
            return True
        else:
            return False

    @property
    def post_market_open(self) ->bool:
        post_market_end_time = datetime.now().replace(hour =22, minute= 30, second= 00, tzinfo= timezone.utc).timestamp()
        market_end_time = datetime.now().replace(hour =20, minute= 00, second= 00, tzinfo= timezone.utc).timestamp()
        right_now = datetime.now().replace(tzinfo=timezone.utc).timestamp()

        if post_market_end_time >= right_now >= market_end_time :
            return True
        else:
            return False

    @property

    def regular_market_open(self) -> bool:
        market_start_time = datetime.now().replace(hour =13, minute= 30, second= 00, tzinfo= timezone.utc).timestamp()
        market_end_time = datetime.now().replace(hour =20, minute= 00, second= 00, tzinfo= timezone.utc).timestamp()
        right_now = datetime.now().replace(tzinfo=timezone.utc).timestamp()

        if market_end_time >= right_now >= market_start_time :
            return True
        else:
            return False
        

    def create_portfolio(self):
        pass

    def create_trade(self):
        pass
    
    def grab_current_quotes(self) -> dict:
        pass

    def grab_historical_prices(self) -> List[Dict]:
        pass

    def create_stock_frame(self):
        pass



