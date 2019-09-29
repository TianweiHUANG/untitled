#for n in range(1,10):
    #print(n)
loan = 700000 # 贷款金额
annualRate = 0.049 # 贷款年利率
monthRate = annualRate/12 # 贷款月利率
period = 30 # 贷款期限30年

print("等额本金")#等额本金
# 还款期数
month = [n for n in range(1,period*12+1)]
print("还款期数",month)
# 每月应还本金
#monthPrincipalPayment = [loan/(period*12)]*period*12
monthPrincipalPayment = [loan/(period*12) for n in range(1,period*12+1)]
print("每月应还本金",monthPrincipalPayment)
# 每月应还利息
monthInterestPayment = [(loan - loan*(n-1)/(period*12))*monthRate for n in range(1,period*12+1)]
print("每月应还利息",monthInterestPayment)
# 每月应还本息
monthPayment = [(loan - loan*(n-1)/(period*12))*monthRate+loan/(period*12) for n in range(1,period*12+1)]
print("每月应还本息",monthPayment)

print("等额本息")#等额本息
# 每月应还本息
monthPayment = (loan*monthRate*(1+monthRate)**360)/((1+monthRate)**360-1)
print("每月应还本息",monthPayment)
#print("每月应还本息{}".format(round(monthPayment,2)))
