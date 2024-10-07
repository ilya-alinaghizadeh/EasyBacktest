import ccxt
import pandas as pd

ex = ccxt.binance()

symbol = "BTC/USDT"
timeframe = "1h"

ohlcv_data = ex.fetch_ohlcv(symbol , timeframe)

columns = ["timestamp" , "open" , "high" , "low" , "close" , "volume"]

df = pd.DataFrame(ohlcv_data , columns=columns)

df["timestamp"] = pd.to_datetime(df["timestamp"] , unit='ms')

out = "ohlcv.xlsx"
df.to_excel(out,index=False)
print("Done")