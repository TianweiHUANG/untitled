loan = 700000 # 贷款金额
annualRate = 0.049 # 贷款年利率
monthRate = annualRate/12 # 贷款月利率
period = 30 # 贷款期限30年

print("###### ###### ###### ###### ###### ###### 等额本金_List ###### ###### ###### ###### ###### ######")
# 还款期数
month_list_Type0 = [n for n in range(1,period*12+1)]
print("还款期数",month_list_Type0)
# 每月应还本金
monthPrincipalPayment_list_Type0 = [round(loan/(period*12),2) for n in range(1,period*12+1)]
print("每月应还本金",monthPrincipalPayment_list_Type0)
# 每月应还利息
monthInterestPayment_list_Type0 = [round((loan - loan*(n-1)/(period*12))*monthRate,2) for n in range(1,period*12+1)]
print("每月应还利息",monthInterestPayment_list_Type0)
# 每月应还本息
monthPiPayment_list_Type0 = [round(loan/(period*12)+(loan - loan*(n-1)/(period*12))*monthRate,2) for n in range(1,period*12+1)]
print("每月应还本息",monthPiPayment_list_Type0)

print("###### ###### ###### ###### ###### ###### 等额本息_List ###### ###### ###### ###### ###### ######")
# 还款期数
month_list_Type1 = [n for n in range(1,period*12+1)]
# 每月应还本息
monthPiPayment_list_Type1=[round((loan*monthRate*(1+monthRate)**(period*12))/((1+monthRate)**(period*12)-1),2) for n in range(1,period*12+1)]

# 每月应还利息
monthInterestPayment_list_Type1 = [round(loan*monthRate,2)]
# 每月应还本金
monthPrincipalPayment_list_Type1 = [round(monthPiPayment_list_Type1[0]-monthInterestPayment_list_Type1[0],2)]
# 每月本金余额
monthPrincipalBalance_list_Type1 = [loan-monthPrincipalPayment_list_Type1[0]]

for n in range(1, period*12):
    monthInterestPayment_list_Type1.append(round(
        monthPrincipalBalance_list_Type1[n-1]*monthRate,
        2))
    monthPrincipalPayment_list_Type1.append(round(
        monthPiPayment_list_Type1[n]-monthInterestPayment_list_Type1[n],
        2))
    monthPrincipalBalance_list_Type1.append(round(
        monthPrincipalBalance_list_Type1[n-1]-monthPrincipalPayment_list_Type1[n],
        2))

print("还款期数",month_list_Type1)
print("每月应还本金",monthPrincipalPayment_list_Type1)
print("每月应还利息",monthInterestPayment_list_Type1)
print("每月应还本息",monthPiPayment_list_Type1)
#print("每月本金余额",monthPrincipalBalance_list_Type1)