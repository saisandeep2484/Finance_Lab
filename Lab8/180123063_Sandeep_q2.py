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
    
    arr = np.zeros(shape=(st,21))
    for i in range(0,st):
        arr[i] = S[i][-21:]
    return arr

bse_stocks = func_index("bsedata1_daily.csv",10)
nse_stocks = func_index("nsedata1_daily.csv",10)
bse_index = func_index("bsedata1_index_daily.csv",1)
nse_index = func_index("nsedata1_index_daily.csv",1)

def annual_volatility(daily_prices):
    prices = daily_prices
    rets = (prices[1:]-prices[:-1])/prices[:-1]
    return rets.std()*math.sqrt(TRADING_DAYS)


print("****************** Question 2 *********************")

def d_positive(S,K,del_t,r,sigma):
    val = math.log(S/K) + (r+(sigma*sigma/2))*(del_t)
    return val/(sigma*math.sqrt(del_t))


def d_negative(S,K,del_t,r,sigma):
    val = math.log(S/K) + (r-(sigma*sigma/2))*(del_t)
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

r = 0.05
T = 0.5

i=0
for stock in bse_stocks:
    print("")
    print("Stock:",bse_name[i],"[BSE]")
    i+=1
    prices = stock
    S0 = prices[-1]
    sigma = annual_volatility(prices)
    for A in [1., 0.5, 0.1, 1.5]:
        callp = bsm_call(S0,S0*A,T,0,r,sigma)
        putp = bsm_put(S0,S0*A,T,0,r,sigma)
        print(f'For A={A}, Call Price = {callp} \t Put Price = {putp}')
        
i=0
for stock in nse_stocks:
    print("")
    print("Stock:",nse_name[i],"[NSE]")
    i+=1
    prices = stock
    S0 = prices[-1]
    sigma = annual_volatility(prices)
    for A in [1., 0.5, 0.1, 1.5]:
        callp = bsm_call(S0,S0*A,T,0,r,sigma)
        putp = bsm_put(S0,S0*A,T,0,r,sigma)
        print(f'For A={A}, Call Price = {callp} \t Put Price = {putp}')
    
i=0
for stock in bse_index:
    print("")
    print("SENSEX","[BSE]")
    i+=1
    prices = stock
    S0 = prices[-1]
    sigma = annual_volatility(prices)
    for A in [1., 0.5, 0.1, 1.5]:
        callp = bsm_call(S0,S0*A,T,0,r,sigma)
        putp = bsm_put(S0,S0*A,T,0,r,sigma)
        print(f'For A={A}, Call Price = {callp} \t Put Price = {putp}')  
        
i=0
for stock in nse_index:
    print("")
    print("NIFTY","[NSE]")
    i+=1
    prices = stock
    S0 = prices[-1]
    sigma = annual_volatility(prices)
    for A in [1., 0.5, 0.1, 1.5]:
        callp = bsm_call(S0,S0*A,T,0,r,sigma)
        putp = bsm_put(S0,S0*A,T,0,r,sigma)
        print(f'For A={A}, Call Price = {callp} \t Put Price = {putp}')  
        
