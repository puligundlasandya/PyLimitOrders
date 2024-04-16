from trading_framework.execution_client import ExecutionClient
from trading_framework.price_listener import PriceListener


class LimitOrderAgent(PriceListener):

    def __init__(self, execution_client: ExecutionClient) -> None:
        """

        :param execution_client: can be used to buy or sell - see ExecutionClient protocol definition
        """
        self.execution_client=execution_client
        super().__init__()

    def on_price_tick(self, product_id: str, price: float):
        # see PriceListener protocol and readme file
        self.product_id=product_id
        self.price=price
    def add_order(self,bug_flag,product_id:str,amount:int,limit:float):
        self,
