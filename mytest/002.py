#coding=utf-8
#个税计算
#输入利润
profit=int(input('输入利润：'))
#提成变量
bonus=0
thresholds=[100000,100000,200000,200000,400000]
rates=[0.1,0.075,0.05,0.03,0.015,0.01]
for i in range(len(thresholds)):
    if profit<=thresholds[I]:
        bonus+=profit*rates[i]:
        profit=0
        break
    else:
        bonus+=thresholds[i]*rates[i]
        profit-=thresholds[i]
bonus+=profit*rates[-1]