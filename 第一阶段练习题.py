# 股价计算小程序
name = "传智播客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
print(
    f"公司:{name},股票代码:{stock_code},当前股价:{stock_price},每日增长系数:{stock_price_daily_growth_factor},经过{growth_days}天的增长后,"
    f"股价到达了%.2f" % (stock_price * stock_price_daily_growth_factor**growth_days))
