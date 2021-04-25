#import math
import time
import math
import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def isKthBitSet(n, k): 
    if n & (1 << (k - 1)): 
        return True
    else: 
        return False 
    
def conv(l,d):
    xx = ""
    for j in range(1,d+1):
        if isKthBitSet(l,j):
            xx+="U"
        else:
            xx+="D"
    
    return xx

def func(S0,T,m,r,sigma):
    del_t = T/m;
    u_power = sigma*math.sqrt(del_t) + (r-0.5*sigma*sigma)*del_t
    u = math.exp(u_power)
    d_power = -sigma*math.sqrt(del_t) + (r-0.5*sigma*sigma)*del_t
    d = math.exp(d_power)

    p = ((math.exp(r*del_t)) - d)/(u-d)
    lookback_option_price = 0
    for k in range(0,2**m):
        price = []
        price.append(S0)
        cnt = 0
        for i in range(1,m+1):
            xx = 0
            if isKthBitSet(k,i):
                cnt+=1
                xx = price[-1]*u
            else:
                xx = price[-1]*d
            price.append(xx)
        Smax = np.max(price)
        lookback_payoff = Smax-price[-1]
        lookback_option_price += math.pow(p,cnt) * math.pow((1-p),m-cnt) * lookback_payoff
        
    lookback_option_price = lookback_option_price/math.exp(r*T) 
    return lookback_option_price

def func1(S0,T,m,r,sigma,t):
    
    print("For t =",t,":")
    print("OCCURRED PATH","   LOOKBACK OPTION PRICE")
    del_t = T/m;
    u_power = sigma*math.sqrt(del_t) + (r-0.5*sigma*sigma)*del_t
    u = math.exp(u_power)
    d_power = -sigma*math.sqrt(del_t) + (r-0.5*sigma*sigma)*del_t
    d = math.exp(d_power)

    p = ((math.exp(r*del_t)) - d)/(u-d)
    
    
    t_rem = (int) (round((m - t/del_t))) #number of time periods remaining
    t_occ = (int) (round((t/del_t))) #number of time periods occurred
    
    for l in range(0,2**t_occ):
        pr = []
        pr.append(S0)
        cn = 0
        for j in range(1,t_occ+1):
            xx = 0
            if isKthBitSet(l,j):
                cn+=1
                xx = pr[-1]*u
            else:
                xx = pr[-1]*d
            pr.append(xx)
        
        S_init = S0 * math.pow(u,cn) * math.pow(d,t_occ-cn)
        S_max = np.max(pr)
        lookback_option_price = 0
        for k in range(0,2**t_rem):
            price = []
            price.append(S_init)
            cnt = 0
            for i in range(1,t_rem+1):
                xx = 0
                if isKthBitSet(k,i):
                    cnt+=1
                    xx = price[-1]*u
                else:
                    xx = price[-1]*d
                price.append(xx)
            
            Smax = np.max(price)
            Smax = max(Smax,S_max)
            lookback_payoff = Smax-price[-1]
            lookback_option_price += math.pow(p,cnt) * math.pow((1-p),t_rem-cnt) * lookback_payoff
        
        print("   ",conv(l,t_occ)," "*(15+2-t_occ),"{:.6f}".format(lookback_option_price/math.exp(r*del_t*t_rem)))
        
    
    print("")


print("q1(a)")
time_arr = []
start = time.time()
print("m =",5,",lookback option price =",func(100,1,5,0.08,0.2))
end = time.time()
time_arr.append(end-start)
start = time.time()
print("m =",10,",lookback option price =",func(100,1,10,0.08,0.2))
end = time.time()
time_arr.append(end-start)
start = time.time()
print("m =",15,",lookback option price =",func(100,1,15,0.08,0.2))
end = time.time()
time_arr.append(end-start)
start = time.time()
print("m =",20,",lookback option price =",func(100,1,20,0.08,0.2))
end = time.time()
time_arr.append(end-start)

print("")
print("For m = 5, Time Taken = ",time_arr[0])
print("For m = 10, Time Taken = ",time_arr[1])
print("For m = 15, Time Taken = ",time_arr[2])
print("For m = 20, Time Taken = ",time_arr[3])

print("")
print("q1(b)")
xx = []
yy = []

for i in range(5,21):
    xx.append(i)
    yy.append(func(100,1,i,0.08,0.2))
    
plt.scatter(xx, yy,c='r',s=10)
plt.plot(xx, yy)
plt.xlabel("Value of M")
plt.ylabel("Initial Option Price")
plt.xticks(xx)
plt.title("Lookback Option Price at t=0 vs M")
plt.grid(True)
plt.show()

print("")
print("q1(c)")
print("")
func1(100,1,5,0.08,0.2,0)
func1(100,1,5,0.08,0.2,0.2)
func1(100,1,5,0.08,0.2,0.4)
func1(100,1,5,0.08,0.2,0.6)
func1(100,1,5,0.08,0.2,0.8)
func1(100,1,5,0.08,0.2,1)
