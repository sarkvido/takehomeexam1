#Exercise 1
#T = maturity date of the option 
#K = price at T
#S = strike price
KList = [8000,8500,9000]
SList = [8200,9700,10000,12100]
PayOffList = []
SPlotList = []
PayOffPlotList = []


import numpy as np 
import matplotlib.pyplot as plt

def OptionEval ( S , K ):
	return np.maximum(0,S-K)   
#OptionEval( 8200 , 8000 ) 

for k in KList:
    for s in SList:
        PayOffList.append(OptionEval(s,k))
                       
print(PayOffList)

for s in SList:
      PayOffPlotList.append(OptionEval(s,8000))

print(PayOffPlotList)

x = SList
y = PayOffPlotList
plt.ylabel('inner value of European call option')
plt.plot(x,y) 
plt.grid()
plt.show()
