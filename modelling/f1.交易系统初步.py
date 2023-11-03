import pandas as pd
import numpy as np

# 读取历史数据，包括价格和成交量信息
data = pd.read_csv('data.csv')
close_price = data['close'].values
volume = data['volume'].values
# 计算均线指标
ma5 = talib.SMA(close_price, timeperiod=5)
ma10 = talib.SMA(close_price, timeperiod=10)
# 判断买入卖出条件
buy_signal = (close_price > ma5) & (ma5 > ma10) & (volume > np.mean(volume))
sell_signal = close_price < ma5
# 设定止损和止盈条件
stop_loss = -0.03
take_profit = 0.1
# 初始化账户信息，包括初始资金、持仓信息和收益统计等。
capital = 1000000.0
position = 0.0
profit_record = []
trade_record = []
# 开始循环遍历历史数据，并执行交易策略。
for i in range(len(data)):
    if buy_signal[i]:
        # 计算可购买数量，并更新账户信息。
        position += capital * 0.2 / close_price[i]
        capital -= capital * 0.2

        # 记录交易记录。
        trade_record.append(('buy', close_price[i], position))

    elif sell_signal[i]:
        # 计算卖出数量，并更新账户信息。
        capital += position * close_price[i]
        position = 0.0

        # 记录交易记录。
        trade_record.append(('sell', close_price[i], position))

    # 检查止损和止盈条件，并更新账户信息。
    if position > 0:
        profit = (close_price[i] - trade_record[-1][1]) / trade_record[-1][1]

        if profit < stop_loss or profit > take_profit:
            capital += position * close_price[i]
            position = 0.0
            profit_record.append(profit)

    # 记录收益统计信息。
    if len(trade_record) == 0:
        profit_record.append(0)
    else:
        total_profit = sum(profit_record)
        avg_profit = np.mean(profit_record)
