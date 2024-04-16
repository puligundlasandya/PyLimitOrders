from trading_framework.execution_client import ExecutionClient
from trading_framework.price_listener import PriceListener


class LimitOrderAgent(PriceListener):

    def __init__(self, execution_client: ExecutionClient) -> None:
        """

        :param execution_client: can be used to buy or sell - see ExecutionClient protocol definition
        """
        self.execution_client=execution_client
        self.held_orders=[]
        super().__init__()

    def on_price_tick(self, product_id: str, price: float):
        # see PriceListener protocol and readme file
        print(f"Price tick for {product_id}: {price}")
        self.held_orders(product_id, price)
    def add_order(self,buy_flag:bool,product_id:str,amount:int,limit_price:float):
        order={'buy_flag':buy_flag,
        'product_id':product_id,
        'amount':amount,
        'limit_price':limit_price
        }
        self.held_orders.append(order)
    def execute_held_orders(self,current_price:float):
        executed_orders=[]
        for order in self.held_orders:
            if order['buy_flag'] and current_price<=order['limit_price']:
                self.execution_client.buy(order['prodect_id'],order['amount'])
                executed_orders.append(order)
            elif not orded['buy_flag'] and current_price>=orderd['limit_price']:
                self.execution_client.sell(order['prodect_id'],order['amount'])
                executed_orders.append(order)
        for executed_order in executed_orders:
            self.held_orders.remove(executed_order)
