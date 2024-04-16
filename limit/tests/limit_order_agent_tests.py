import unittest
import random

class LimitOrderAgentTest(unittest.TestCase):

    def setup(self):
        self.mock_execution_client=MagicMock(spec=ExecutionClient)
        
    def test_price_tick_executes_buy(self):
        agent=LimitOrderAgent(self,mock_execution_client)
        agent.price_tick("IBM",99.0)
        self.mockexecution_client.buy.assert_called_once_with("IBM",1000)
        
     def test_add_order_adds_to_held_orders(self):
        agent = LimitOrderAgent(Mock())
        agent.add_order(buy_flag=True, product_id='AAPL', amount=500, limit_price=150.0)
        self.assertEqual(len(agent.held_orders), 1)

    def test_execute_held_orders_executes_orders(self):
        agent = LimitOrderAgent(self.mock_execution_client)
        agent.add_order(buy_flag=True, product_id='AAPL', amount=500, limit_price=150.0)
        agent.execute_held_orders(145.0)
        self.mock_execution_client.buy.assert_called_once_with('AAPL', 500)
        self.assertEqual(len(agent.held_orders), 0)

    def test_execute_held_orders_executes_orders_sell(self):
        agent = LimitOrderAgent(self.mock_execution_client)
        agent.add_order(buy_flag=True, product_id='IBM', amount=1000, limit_price=random.randrange(120,150))
        agent.execute_held_orders(100.0)
        self.mock_execution_client.sell.assert_called_once_with('IBM', 1000)
        self.assertEqual(len(agent.held_orders), 1)

     def test_execute_held_orders_executes_orders_buy(self):
        agent = LimitOrderAgent(self.mock_execution_client)
        agent.add_order(buy_flag=True, product_id='IBM', amount=1000, limit_price=random.randrange(50,100))
        agent.execute_held_orders(100.0)
        self.mock_execution_client.buy.assert_called_once_with('IBM', 1000)
        self.assertEqual(len(agent.held_orders), 1)
    

    if __name__ == '__main__':
        unittest.main()
    

