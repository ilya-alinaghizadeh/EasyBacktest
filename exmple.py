import pandas as pd
from main import BackTest,SAME_QUANTITY,NEW_QUANTITY,GRAPH



data = pd.read_excel('ohlcv.xlsx')

# Define your conditions
def buy_condition(data, step):

    return data['close'][step] > data['close'][step - 1]  # Buy if current close > previous close

def sell_condition(data, step):
    return data['close'][step] < data['close'][step - 1]  # Sell if current close < previous close

def buy_tp_condition(data, step, entry_price):

    return data['close'][step] >= float(entry_price) + 1 

def buy_sl_condition(data, step, entry_price):
    return data['close'][step] <= entry_price - 1

def sell_tp_condition(data, step, entry_price):
    return data['close'][step] >= entry_price - 1

def sell_sl_condition(data, step, entry_price):
    return data['close'][step] <= entry_price + 1

# Initialize backtester
backtester = BackTest(
    data=data,
    min_load=1,
    buy_condition=buy_condition,
    sell_condition=sell_condition,
    buy_tp_condition=buy_tp_condition,
    buy_sl_condition=buy_sl_condition,
    sell_sl_condition=sell_sl_condition,
    sell_tp_condition=sell_tp_condition,
    quantity=100,
    win_percentage=30,
    loss_percentage=10,
    money_management=NEW_QUANTITY,
    graph=GRAPH

)

# Run backtest
backtester.run()

# Print summary
summary = backtester.summary()
summary["graph"].savefig("graph")
