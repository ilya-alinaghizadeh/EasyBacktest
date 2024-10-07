import pandas as pd
import matplotlib.pyplot as plt

NEW_QUANTITY = "new_quantity"
SAME_QUANTITY = "same_quantity"
GRAPH = "graph"
NO_GRAPGH = "no_grapgh"

class BackTest:
    
    def __init__(self , data: pd.DataFrame , load_per_step:int,
                 buy_condition , sell_condition, win_percentage,
                 loss_percentage,
                 buy_tp_condition, buy_sl_condition,
                 sell_tp_condition , sell_sl_condition,
                 quantity:float,
                 money_management,
                 graph
                 ):
        
        self.data = data
        self.load_per_step = load_per_step
        self.buy_condition = buy_condition
        self.sell_condition = sell_condition
        self.buy_tp_condition = buy_tp_condition
        self.buy_sl_condition = buy_sl_condition
        self.sell_tp_condition = sell_tp_condition
        self.sell_sl_condition = sell_sl_condition
        self.quantity = quantity
        self.win_percentage = win_percentage
        self.loss_percentage = loss_percentage
        self.trades = []  # Store active trades
        self.closed_trades = []  # Store closed trades
        self.wins = []
        self.losses = []
        self.money_management = money_management
        self.graph = graph
        
    def run(self):
        
        for step in range(self.load_per_step , len(self.data)):
            self.process_step(step)
            
    def process_step(self , step):
        
        
        if self.buy_condition(self.data , step):
            
            self.open_trade(step , "buy")
        
        elif self.sell_condition(self.data , step):
            self.open_trade(step , "sell")
            
        for trade in self.trades:
            
            self.check_close_trade_condition(trade , step)
            
    def open_trade(self , step , trade_type):
        
        trade_info = {
            'entery_price':float(self.data["close"][step]),
            'step':step,
            'type' : trade_type
        }
        
        self.trades.append(trade_info)
        
        
    def check_close_trade_condition(self , trade , step):
        
        step = step
        
        if trade['type'] == "buy":
        
            if self.buy_tp_condition(self.data , step , trade['entery_price']):
            
                self.closed_trades.append({'trade': trade, 'result': 'win', 'profit': self.win_percentage})
                self.trades.remove(trade)
                self.wins.append(self.win_percentage)
            
            elif self.buy_sl_condition(self.data , step , trade["entery_price"]):
            
                self.closed_trades.append({'trade': trade, 'result': 'lose', 'profit': self.loss_percentage})
                self.trades.remove(trade)
                self.losses.append(self.loss_percentage)
        
        elif trade['type'] == "sell":
            
            if self.sell_tp_condition(self.data , step , trade['entery_price']):
            
                self.closed_trades.append({'trade': trade, 'result': 'win', 'profit': self.win_percentage})
                self.trades.remove(trade)
                self.wins.append(self.win_percentage)
            
            elif self.sell_sl_condition(self.data , step , trade["entery_price"]):
            
                self.closed_trades.append({'trade': trade, 'result': 'lose', 'profit': self.loss_percentage})
                self.trades.remove(trade)
                self.losses.append(self.loss_percentage)
        
        
    def render_graph(self):
        
        if self.money_management == SAME_QUANTITY:
            
            amount_per_win =  ((self.win_percentage / 100) * self.quantity)
            amount_per_loss = ((self.loss_percentage / 100) * self.quantity)
            
            chart_data = [self.quantity]
            
            for t in self.closed_trades:
                
                if t["result"] == "win":
                    
                    chart_data.append((chart_data[-1]+amount_per_win))
                    
                elif t["result"] == "lose":
                    
                    chart_data.append((chart_data[-1]-amount_per_loss))
                    
            x = list(range(len(chart_data)))
                
            fig , ax = plt.subplots()
            
            ax.plot(x , chart_data)
            ax.set_title("backtesting")
            ax.set_xlabel("trade")
            ax.set_ylabel("quantity")
            
            return fig
        
        elif self.money_management == NEW_QUANTITY:
            
            render_quantity = self.quantity
            
            chart_data = [self.quantity]
            
            for t in self.closed_trades:
                
                
                amount_per_win =  ((self.win_percentage / 100) * render_quantity)
                amount_per_loss = ((self.loss_percentage / 100) * render_quantity)
                
                if t["result"] == "win":
                    
                    chart_data.append((chart_data[-1]+amount_per_win))
                    
                elif t["result"] == "lose":
                    
                    chart_data.append((chart_data[-1]-amount_per_loss))
            
                render_quantity = chart_data[-1]
        
            x = list(range(len(chart_data)))
                
            fig , ax = plt.subplots()
            
            ax.plot(x , chart_data)
            ax.set_title("backtesting")
            ax.set_xlabel("trade")
            ax.set_ylabel("quantity")
            
            return fig
        
    def summary(self):
        total_wins = len(self.wins)
        total_losses = len(self.losses)
        total_closed_trades = len(self.closed_trades)
        win_rate = (len(self.wins) / total_closed_trades * 100) if total_closed_trades > 0 else 0
        
        if self.graph == NO_GRAPGH:
            pass
        
        elif self.graph == GRAPH:
            
            rendering_graph = self.render_graph()
        
        
        
        return {
        'total_wins': total_wins,
        'total_losses': total_losses,
        'win_rate': round(win_rate,2),
        'closed_trades': total_closed_trades,
        "graph" : rendering_graph
        }
        
        