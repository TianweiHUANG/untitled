#for n in range(1,10):
    #print(n)
loan = 700000 # 贷款金额
annualRate = 0.049 # 贷款年利率
monthRate = annualRate/12 # 贷款月利率
period = 30 # 贷款期限30年
"""
print("等额本金_list")#等额本金_list
# 还款期数
month = [n for n in range(1,period*12+1)]
print("还款期数",month)
# 每月应还本金
#monthPrincipalPayment = [round(loan/(period*12),2)]*period*12
monthPrincipalPayment = [round(loan/(period*12),2) for n in range(1,period*12+1)]
print("每月应还本金",monthPrincipalPayment)
# 每月应还利息
monthInterestPayment = [round((loan - loan*(n-1)/(period*12))*monthRate,2) for n in range(1,period*12+1)]
print("每月应还利息",monthInterestPayment)
# 每月应还本息
monthPayment = [round(loan/(period*12)+(loan - loan*(n-1)/(period*12))*monthRate,2) for n in range(1,period*12+1)]
print("每月应还本息",monthPayment)
"""

print("等额本息_list")#等额本息_list
# 还款期数
month = [n for n in range(1,period*12+1)]
print("还款期数",month)
# 每月应还本息
monthPIPayment = round((loan*monthRate*(1+monthRate)**360)/((1+monthRate)**360-1),2)#?
monthPIPayment_list=[monthPIPayment for n in range(1,period*12+1)]
print("每月应还本息",monthPIPayment_list)
#print("每月应还本息{}".format(round(monthPIPayment,2)))

##### ##### ##### ##### ##### ##### ##### ##### ##### #####
# 每月应还利息
monthInterestPayment = [round(loan*monthRate,2)]
# 每月欠款余额
loanPI = [loan*(1+monthRate)-monthPIPayment]#?
for n in range(1, period*12):
    loanPI.append((loanPI[n-1]*(1+monthRate)-monthPIPayment))
    monthInterestPayment.append(round(loanPI[n-1] * monthRate,2))
print("每月应还利息",monthInterestPayment)
##### ##### ##### ##### ##### ##### ##### ##### ##### #####

# 每月应还本金
#monthPrincipalPayment = [monthPIPayment-monthInterestPayment[n] for n in range(0,len(monthInterestPayment))]
monthPrincipalPayment = [round(monthPIPayment-monthInterestPayment[n],2) for n in range(0,period*12)]
print("每月应还本金",monthPrincipalPayment)
