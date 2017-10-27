#!/usr/bin/env python3
amount = float(input("Enter amount: ")) 
# 输 入 数 额
inrate = float(input("Enter Interest rate: "))  
# 输 入 利 率
period = int(input("Enter period: ")) 
# 输 入 期 限
value = 0
year = 1
while year <= period:
    value = amount + (inrate * amount)
    print("Year {} Rs. {:.2f}".format(year, value))
    amount = value
    year = year + 1   
