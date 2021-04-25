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

def reduced_gen_stock_prices(Z):
    S1 = []
    S2 = []
    S1.append(S0)
    S2.append(S0)
    #S1 is risk neutral meausure (positive)
    #S2 is risk neutral meausure (negative) 
    for i in range(0,len(Z)):
        tem = S1[-1]*math.exp((r-0.5*sigma*sigma)*diff + sigma*(math.sqrt(diff))*Z[i])
        S1.append(tem)
        tem = S2[-1]*math.exp((r-0.5*sigma*sigma)*diff - sigma*(math.sqrt(diff))*Z[i])
        S2.append(tem)
        
    return S1,S2

def option_price(m,K,option):
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


def option_price2(m,K,option):
    payoffSum1=0
    for i in range(m):
        Z2 = func_Box_Muller(T)
        Spos,Sneg = reduced_gen_stock_prices(Z2)
        Ypos = np.mean(Spos)
        Yneg = np.mean(Sneg)
        if option=='Call':
            payoff1 = max(0,Ypos-K)+max(0,Yneg-K)
            payoff1=payoff1/2
        else:
            payoff1 = max(0,K-Ypos)+max(0,K-Yneg)
            payoff1=payoff1/2
            
        payoffSum1 += payoff1 
    return np.exp(-r*diff*T)*(payoffSum1/m)

print("**********************************")
option = 'Call'
for K in [90,105,110]:
    a1= []
    a2= []
    for i in range(100,1000,100):
        ar1 = option_price(m=i,K=K,option=option)
        ar2 = option_price2(m=i,K=K,option=option)
        a1.append(ar1)
        a2.append(ar2)
        
    print('Variance of '+option + ' option price without variance reduction for K = '+ str(K) +' is '+ str(np.round(np.var(a1), 5)))
    print('Variance of '+option + ' option price with variance reduction for K = '+ str(K) +' is '+ str(np.round(np.var(a2), 5)))
    
    plt.figure()
    plt.plot([*range(100,1000,100)],a1,label='No variance reduction')
    plt.plot([*range(100,1000,100)],a2,label='with variance reduction')
    plt.xlabel('Number of simulations')
    plt.ylabel('Option Price')
    plt.title(option + ' Option Prices for K = '+ str(K))
    plt.legend()
    plt.show()
    
print("**********************************")
option = 'Put'

for K in [90,105,110]:
    a1= []
    a2= []
    for i in range(100,1000,100):
        ar1 = option_price(m=i,K=K,option=option)
        ar2 = option_price2(m=i,K=K,option=option)
        a1.append(ar1)
        a2.append(ar2)
    print('Variance of '+option + ' option price without variance reduction for K = '+ str(K) +' is '+ str(np.round(np.var(a1), 5)))
    print('Variance of '+option + ' option price with variance reduction for K = '+ str(K) +' is '+ str(np.round(np.var(a2), 5)))
    plt.figure()
    plt.plot([*range(100,1000,100)],a1,label='No variance reduction')
    plt.plot([*range(100,1000,100)],a2,label='with variance reduction')
    plt.xlabel('Number of simulations')
    plt.ylabel('Option Price')
    plt.title(option + ' Option Prices for K = '+ str(K))
    plt.legend()
    plt.show()
    
    


    
    