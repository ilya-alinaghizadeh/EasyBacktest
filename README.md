# Welcome to EasyBacktest!

Hi everyone, I wrote Easy Backtest when I was facing problems whenever I wanted to backtest my strategies but all the other libraries were too complicated


# Files



**main:**
The main file you should import and start your work on

**example:**
obviously an example for you to understand the library

**ohlcv:**
If you are having problems fetching OHLCV files for backtesting it can help you 
## Guide

Money Management:

 1. **SAME_QUANTITY**:
 It keeps the quantity as a reference for calculating your wins and losses
 
 2. **NEW_QUANTITY**:
 whenever you get a win or loss it updates the quantity and use the new quantity as a reference

Graph:

 1. **NO_GRAPH:** no graph
 
 2. **GRAPG:** will draw a graph for you

you can use the graph with using ["graph"] for summary result

    BackTest(...).summary()["graph"]
Attention, you should first run the backtest with "BackTest().run()" and after you can have access to summary
inputs:


 1. **data:** The data which you want to backtest on
 
 2. **min_load:** Where in the data do you want to start from, for example, if you are using a 20 Moving Average you should put 20
 
 3. **buy/sell_condition:** your buy/sell condition function
 
 4. **buy/sell_tp_condition:** your buy/sell tp condition function
 
 5. **buy/sell_sl_condition:**  your buy/sell sl condition 

 6. **quantity:** your test quantity
 
 7. **win_percentage:** How much you will win in each trade in percentages

 8. **loss_percentage:** how much you will lose in each trade in percentages
 
 9. **money_management:** your money management method (NEW_QUANTITY , SAME_QUANTITY)
 
 10. **GRAPGH:** your graph status (GRAPGH,NO_GRAPH)

## Tips

 - first run the backtest and then start using summary
 

       backtester =  BackTest(

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

       graph=GRAPH)
       
       backtester.run()
       summary = backtester.summary()

 - each function that you will introduce to muddle should contain step and data
     - step is where the backtest is in data and data is the data you introduced 
    -  tp/sl conditions beside step and data will contain entery_price too for easier calculation


## Donation

Thether TRC20

    TV72PWfzfw5y9AHUitmUL3dDii51qYLY3P

BTC

    bc1qawcqyeuey4f0exnh40r7jshndsrg0lnsqh225v

ETH

    0x74316cDd468Bf44605cFa173E2A9cFeCb56f2187
