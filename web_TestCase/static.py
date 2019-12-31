import os, sys
import datetime
import matplotlib.pyplot as plt
import pandas as pd
import tushare as ts

if len(sys.argv) == 2:
    code = sys.argv[1]
else:
    print('usage: python stock_price.py stockcode ')
    sys.exit(1)

if len(code) != 6:
    print('stock code length: 6')
    sys.exit(2)

# help(ts.get_hist_data) 了解参数
dh = ts.get_hist_data(code)
df = dh.sort_values(by='date')
df.reset_index(inplace=True)
# 取样 2019年以后的数据
d2 = df[df['date'] > '2019-01-01']
print(d2.head())
d2.index = pd.to_datetime(d2.date)

# 画股价走势图
fig, axes = plt.subplots(2, 1)
d2[['close', 'ma5', 'ma10', 'ma20']].plot(ax=axes[0], grid=True, title=code)
# 画股票成交量图
d2[['volume']].plot(ax=axes[1], grid=True)
plt.show()
