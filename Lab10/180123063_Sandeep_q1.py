import numpy as np
import matplotlib.pyplot as plt
import math
import random

mu = 0.1
r = 0.05
sigma = 0.2
diff = 1.0/365
T = 180
S0 = 100

def func_Box_Muller(num):
    ans = []
    while len(ans)<num:
        u1 = random.random()
        u2 = random.random()
        r1 = -2*(math.log(u1))
        v = 2*(math.pi)*u2
        z1 = (math.sqrt(r1))*(math.cos(v))
        z2 = (math.sqrt(r1))*(math.sin(v))
        ans.append(z1)
        ans.append(z2)
    return ans
    
def gen_stock_prices(Z):
    S1 = []
    S2 = []
    S1.append(S0)
    S2.append(S0)
    #S1 is risk neutral meausure
    #S2 is real world
    for i in range(0,len(Z)):
        tem = S1[-1]*math.exp((r-0.5*sigma*sigma)*diff + sigma*(math.sqrt(diff))*Z[i])
        S1.append(tem)
        tem = S2[-1]*math.exp((mu-0.5*sigma*sigma)*diff + sigma*(math.sqrt(diff))*Z[i])
        S2.append(tem)
        
    return S1,S2

arr1 = []
arr2 = []

for i in range(0,10):
    Z1 = func_Box_Muller(T)
    S_Risk_Neutral, S_Real = gen_stock_prices(Z1)
    arr1.append(S_Risk_Neutral)
    arr2.append(S_Real)
print("**********************************")    
fig = plt.figure() 
for i in range(0,10):
    plt.plot(arr1[i])
    
plt.xlabel('Time (in Days)')
plt.ylabel('Simulated Stock Price')
plt.title('10 Stock Simulation in Risk Neutral World')
plt.show()
print("**********************************")
fig = plt.figure() 
for i in range(0,10):
    plt.plot(arr2[i])

plt.xlabel('Time (in Days)')
plt.ylabel('Simulated Stock Price')
plt.title('10 Stock Simulation in Real World')
plt.show()
print("**********************************")

plt.plot(arr1[0])
plt.plot(arr2[0])
plt.legend(['Risk neutral','Real'])
plt.title('Comparison of Stock Prices in Real and Risk Neutral Framework')
plt.show()



def option_price(m=500,K=100,option='Call',T = 180,r = 0.05,sigma=0.2,mu=0.1,diff=1.0/365,S0=100):
    payoffSum1=0
    for i in range(m):
        Z2 = func_Box_Muller(T)
        Srn,Sr = gen_stock_prices(Z2)
        Yrn = np.mean(Srn)
        if option=='Call':
            payoff1 = max(0,Yrn-K)
        else:
            payoff1 = max(0,K-Yrn)   
        payoffSum1 += payoff1 
    return np.exp(-r*diff*T)*(payoffSum1/m)

print("**********************************")
option = 'Call'
for K in [90,105,110]:
    a1= []
    for i in range(500,3000,250):
        ar = option_price(m=i,K=K,option=option)
        a1.append(ar)
    print('Average ' + option + ' option price for K = '+ str(K) +' is '+ str(np.round(np.mean(ar), 5)))
    plt.figure()
    plt.plot([*range(500,3000,250)],a1)
    plt.xlabel('Number of simulations')
    plt.ylabel('Option Price')
    plt.title(option + ' Option Prices for K = '+ str(K))
    plt.show()
    
print("**********************************")
option = 'Put'
for K in [90,105,110]:
    a1= []
    for i in range(500,3000,250):
        ar = option_price(m=i,K=K,option=option)
        a1.append(ar)
    print('Average ' + option + ' option price for K = '+ str(K) +' is '+ str(np.round(np.mean(ar), 5)))
    plt.figure()
    plt.plot([*range(500,3000,250)],a1)
    plt.xlabel('Number of simulations')
    plt.ylabel('Option Price')
    plt.title(option + ' Option Prices for K = '+ str(K))
    plt.show()
    
    
print("**********************************")

#varying K
option = 'Call'
KK = [*range(50,150,5)]

res = []

for k in KK:
    res.append(option_price(m=100,K=k,option=option))
    
plt.figure()
plt.plot(KK,res)
plt.xlabel('Strike price')
plt.ylabel(option + ' Option Price')
plt.title(option + ' Option Price vs K')
plt.show()
print("**********************************")

option = 'Put'
KK = [*range(50,150,5)]

res = []

for k in KK:
    res.append(option_price(m=100,K=k,option=option))
    
plt.figure()
plt.plot(KK,res)
plt.xlabel('Strike price')
plt.ylabel(option + ' Option Price')
plt.title(option + ' Option Price vs K')
plt.show()

print("**********************************")

#varying r

option = 'Call'
RR = [*range(2,100,2)]
for elem in RR:
    elem = elem/100

res = []

for rr in RR:
    res.append(option_price(m=100,r=rr,option=option))
    
plt.figure()
plt.plot(RR,res)
plt.xlabel('Rate (r)')
plt.ylabel(option + ' Option Price')
plt.title(option + ' Option Price vs r')
plt.show()
print("**********************************")
option = 'Put'

res = []

for rr in RR:
    res.append(option_price(m=100,r=rr,option=option))
    
plt.figure()
plt.plot(RR,res)
plt.xlabel('Rate (r)')
plt.ylabel(option + ' Option Price')
plt.title(option + ' Option Price vs r')
plt.show()


print("**********************************")


#varying simga

option = 'Call'
SS = [*range(2,100,2)]
for elem in SS:
    elem = elem/100

res = []

for ss in SS:
    res.append(option_price(m=100,sigma=ss,option=option))
    
plt.figure()
plt.plot(SS,res)
plt.xlabel('sigma')
plt.ylabel(option + ' Option Price')
plt.title(option + ' Option Price vs sigma')
plt.show()
print("**********************************")
option = 'Put'

res = []

for ss in SS:
    res.append(option_price(m=100,sigma=ss,option=option))
    
plt.figure()
plt.plot(SS,res)
plt.xlabel('sigma')
plt.ylabel(option + ' Option Price')
plt.title(option + ' Option Price vs sigma')
plt.show()


print("**********************************")

#varying T

option = 'Call'
TT = [*range(60,365,1)]

res = []

for t in TT:
    res.append(option_price(m=100,T=t,option=option))
    
plt.figure()
plt.plot(TT,res)
plt.xlabel('sigma')
plt.ylabel(option + ' Option Price')
plt.title(option + ' Option Price vs T')
plt.show()

print("**********************************")
option = 'Put'

res = []

for t in TT:
    res.append(option_price(m=100,T=t,option=option))
    
plt.figure()
plt.plot(TT,res)
plt.xlabel('Maturity Time(T)')
plt.ylabel(option + ' Option Price')
plt.title(option + ' Option Price vs T')
plt.show()


print("**********************************")


    
    