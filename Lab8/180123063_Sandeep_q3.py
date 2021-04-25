import numpy as np
import math
import csv
import matplotlib.pyplot as plt
from scipy.stats import norm

TRADING_DAYS = 252

nse_name = ['HDFC','TCS','Kotak Mahindra','Bharti Airtel','Nestle','Housing Development','Maruti','Asian Paints','HCL','Coal India']
bse_name = ['SBI','Titan','Reliance','ICICI','Axis','L&T','Ultratech','ITC','ONGC','Infosys']

def func_index(string,st):
    c = 1230
    S = np.zeros(shape=(st,c-1))
    with open(string) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        lis = list(csv_reader)
        line_count = 1
        for row in lis[1:]:
            if line_count == c:
                break
            
            cn = 0
            for val in row[1:]:
                if val=='':
                    continue
                S[cn][line_count-1] = float(val)
                cn=cn+1
            
            line_count += 1
    return S

bse_stocks = func_index("bsedata1_daily.csv",10)
nse_stocks = func_index("nsedata1_daily.csv",10)
bse_index = func_index("bsedata1_index_daily.csv",1)
nse_index = func_index("nsedata1_index_daily.csv",1)

def annual_volatility(daily_prices, days):
    prices = daily_prices[:days]
    rets = (prices[1:]-prices[:-1])/prices[:-1]
    return rets.std()*math.sqrt(TRADING_DAYS)


print("****************** Question 3 *********************")

def d_positive(S,K,del_t,r,sigma):
    val = math.log(S/K) + (r+(sigma*sigma/2))*(del_t)
    if sigma == 0:
        sigma = 0.01
    return val/(sigma*math.sqrt(del_t))


def d_negative(S,K,del_t,r,sigma):
    val = math.log(S/K) + (r-(sigma*sigma/2))*(del_t)
    if sigma == 0:
        sigma = 0.01
    return val/(sigma*math.sqrt(del_t))

def bsm_call(S,K,T,t,r,sigma):
    if(t==T):
        return np.maximum(S-K,0)
    term1 = S*norm.cdf(d_positive(S,K,T-t,r,sigma)) 
    term2 = K*math.exp(-r*(T-t))*norm.cdf(d_negative(S,K,T-t,r,sigma))
    return term1-term2
  
def bsm_put(S,K,T,t,r,sigma):
    if(t==T):
        return np.maximum(K-S,0)
    return K*math.exp(-r*(T-t))-S+bsm_call(S,K,T,t,r,sigma)

T=0.5
r = 0.05

print("")
print("*************************BSE STOCKS***********************")
print("")
i=0
days = [x*30 for x in range(1, 13)]

for stock in bse_stocks:
    prices = stock
    S0 = prices[-1]
    vol = [annual_volatility(prices, d) for d in days]

    plt.title(f'{bse_name[i]} ({"BSE"}) - Volatility')
    plt.plot(days, vol, '.-')
    plt.xlabel('Time (in days)')
    plt.ylabel('Estimated Volatility')
    plt.show()

    for iterat, option in enumerate(['Call','Put']):
        for ind, A in enumerate([1,0.5,0.1,1.5]):
            plots = []
            for d in days:
                if iterat != 1:
                    p = bsm_call(S0,A*S0,d/365,0,r,annual_volatility(prices,d))
                else:
                    p = bsm_put(S0,A*S0,d/365,0,r,annual_volatility(prices,d))
                plots.append(p)
            plt.plot(days,plots,'.-', label=f'A={A}',alpha=0.6)

        plt.title(f'{bse_name[i]} ({"BSE"}): {option} Option Prices')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.xlabel('Time (days)')
        plt.ylabel(f'{option} price')
        plt.show()
    i+=1

print("")
print("*************************NSE STOCKS***********************")
print("")
i=0
days = [x*30 for x in range(1, 13)]

for stock in nse_stocks:
    prices = stock
    S0 = prices[-1]
    vol = [annual_volatility(prices, d) for d in days]

    plt.title(f'{nse_name[i]} ({"NSE"}) - Volatility')
    plt.plot(days, vol, '.-')
    plt.xlabel('Time (in days)')
    plt.ylabel('Estimated Volatility')
    plt.show()

    for iterat, option in enumerate(['Call','Put']):
        for ind, A in enumerate([1,0.5,0.1,1.5]):
            plots = []
            for d in days:
                if iterat != 1:
                    p = bsm_call(S0,A*S0,d/365,0,r,annual_volatility(prices,d))
                else:
                    p = bsm_put(S0,A*S0,d/365,0,r,annual_volatility(prices,d))
                plots.append(p)
            plt.plot(days,plots,'.-', label=f'A={A}',alpha=0.6)

        plt.title(f'{nse_name[i]} ({"NSE"}): {option} Option Prices')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.xlabel('Time (days)')
        plt.ylabel(f'{option} price')
        plt.show()
    i+=1

print("")
print("*************************BSE INDEX***********************")
print("")

i = 0
days = [x*30 for x in range(1, 13)]
for stock in bse_index:
    prices = stock
    S0 = prices[-1]
    vol = [annual_volatility(prices, d) for d in days]

    plt.title(f'{"SENSEX"} ({"BSE"}) - Volatility')
    plt.plot(days, vol, '.-')
    plt.xlabel('Time (in days)')
    plt.ylabel('Estimated Volatility')
    plt.show()

    for iterat, option in enumerate(['Call','Put']):
        for ind, A in enumerate([1,0.5,0.1,1.5]):
            plots = []
            for d in days:
                if iterat != 1:
                    p = bsm_call(S0,A*S0,d/365,0,r,annual_volatility(prices,d))
                else:
                    p = bsm_put(S0,A*S0,d/365,0,r,annual_volatility(prices,d))
                plots.append(p)
            plt.plot(days,plots,'.-', label=f'A={A}',alpha=0.6)

        plt.title(f'{"SENSEX"} ({"BSE"}): {option} Option Prices')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.xlabel('Time (days)')
        plt.ylabel(f'{option} price')
        plt.show()
    i+=1

print("")
print("*************************NSE INDEX***********************")
print("")

i = 0
days = [x*21 for x in range(1, 13)]
for stock in nse_index:
    prices = stock
    S0 = prices[-1]
    vol = [annual_volatility(prices, d) for d in days]

    plt.title(f'{"NIFTY"} ({"NSE"}) - Volatility')
    plt.plot(days, vol, '.-')
    plt.xlabel('Time (in days)')
    plt.ylabel('Estimated Volatility')
    plt.show()

    for iterat, option in enumerate(['Call','Put']):
        for ind, A in enumerate([1,0.5,0.1,1.5]):
            plots = []
            for d in days:
                if iterat != 1:
                    p = bsm_call(S0,A*S0,d/365,0,r,annual_volatility(prices,d))
                else:
                    p = bsm_put(S0,A*S0,d/365,0,r,annual_volatility(prices,d))
                plots.append(p)
            plt.plot(days,plots,'.-', label=f'A={A}',alpha=0.6)

        plt.title(f'{"NIFTY"} ({"NSE"}): {option} Option Prices')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.xlabel('Time (days)')
        plt.ylabel(f'{option} price')
        plt.show()
    i+=1

