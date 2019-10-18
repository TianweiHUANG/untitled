loan = 700000 # 贷款金额
annualRate = 0.049 # 贷款年利率
monthRate = annualRate/12 # 贷款月利率
period = 30 # 贷款期限30年

print("###### ###### ###### ###### ###### ###### 等额本金_List ###### ###### ###### ###### ###### ######")
# 还款期数
month_list_Type0 = [n for n in range(1,period*12+1)]
# 每月应还本金
monthPrincipalPayment_list_Type0 = [loan/(period*12) for n in range(1,period*12+1)]
# 每月应还利息
monthInterestPayment_list_Type0 = [(loan - (n-1)*loan/(period*12))*monthRate for n in range(1,period*12+1)]
# 每月应还本息
monthPiPayment_list_Type0 = [loan/(period*12)+(loan - (n-1)*loan/(period*12))*monthRate for n in range(1,period*12+1)]
# 每月本金余额
monthPrincipalBalance_list_Type0 = [loan - n*loan/(period*12) for n in range(1,period*12+1)]

for n in range(0, period*12):
    month_list_Type0[n] = round(month_list_Type0[n], 2)
    monthPrincipalPayment_list_Type0[n] = round(monthPrincipalPayment_list_Type0[n], 2)
    monthInterestPayment_list_Type0[n] = round(monthInterestPayment_list_Type0[n], 2)
    monthPiPayment_list_Type0[n] = round(monthPiPayment_list_Type0[n], 2)
    monthPrincipalBalance_list_Type0[n] = round(monthPrincipalBalance_list_Type0[n], 2)
print("还款期数",month_list_Type0)
print("每月应还本金",monthPrincipalPayment_list_Type0)
print("每月应还利息",monthInterestPayment_list_Type0)
print("每月应还本息",monthPiPayment_list_Type0)
print("每月本金余额",monthPrincipalBalance_list_Type0)

print("期数","月供","月供本金","月供利息","本金余额")
for n in range(0, period*12):
    print(month_list_Type0[n], monthPiPayment_list_Type0[n], monthPrincipalPayment_list_Type0[n], monthInterestPayment_list_Type0[n], monthPrincipalBalance_list_Type0[n])

print("###### ###### ###### ###### ###### ###### 等额本息_List ###### ###### ###### ###### ###### ######")
# 还款期数
month_list_Type1 = [n for n in range(1,period*12+1)]
# 每月应还本息
monthPiPayment_list_Type1=[(loan*monthRate*(1+monthRate)**(period*12))/((1+monthRate)**(period*12)-1) for n in range(1,period*12+1)]

# 每月应还利息
monthInterestPayment_list_Type1 = [loan*monthRate]
# 每月应还本金
monthPrincipalPayment_list_Type1 = [monthPiPayment_list_Type1[0]-monthInterestPayment_list_Type1[0]]
# 每月本金余额
monthPrincipalBalance_list_Type1 = [loan-monthPrincipalPayment_list_Type1[0]]

for n in range(1, period*12):
    monthInterestPayment_list_Type1.append(
        monthPrincipalBalance_list_Type1[n-1]*monthRate)
    monthPrincipalPayment_list_Type1.append(
        monthPiPayment_list_Type1[n]-monthInterestPayment_list_Type1[n])
    monthPrincipalBalance_list_Type1.append(
        monthPrincipalBalance_list_Type1[n-1]-monthPrincipalPayment_list_Type1[n])

for n in range(0, period*12):
    month_list_Type1[n] = round(month_list_Type1[n], 2)
    monthPrincipalPayment_list_Type1[n] = round(monthPrincipalPayment_list_Type1[n], 2)
    monthInterestPayment_list_Type1[n] = round(monthInterestPayment_list_Type1[n], 2)
    monthPiPayment_list_Type1[n] = round(monthPiPayment_list_Type1[n], 2)
    monthPrincipalBalance_list_Type1[n] = round(monthPrincipalBalance_list_Type1[n], 2)
print("还款期数",month_list_Type1)
print("每月应还本金",monthPrincipalPayment_list_Type1)
print("每月应还利息",monthInterestPayment_list_Type1)
print("每月应还本息",monthPiPayment_list_Type1)
print("每月本金余额",monthPrincipalBalance_list_Type1)

print("期数","月供","月供本金","月供利息","本金余额")
for n in range(0, period*12):
    print(month_list_Type1[n], monthPiPayment_list_Type1[n], monthPrincipalPayment_list_Type1[n], monthInterestPayment_list_Type1[n], monthPrincipalBalance_list_Type1[n])
