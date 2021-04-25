import time
import math
import numpy as np 
import matplotlib.pyplot as plt

S0 = 100
T = 1
r = 0.08
sigma = 0.2

dic = {}

def recursive_func(n,maxx,S_cur,u,d,p,del_t,m):
    if (maxx,S_cur) in dic:
        return dic[(maxx,S_cur)]
    
    if n==m:
        return maxx-S_cur
    up_price = recursive_func(n+1,max(maxx,S_cur*u),S_cur*u,u,d,p,del_t,m)
    down_price = recursive_func(n+1,max(maxx,S_cur*d),S_cur*d,u,d,p,del_t,m)
    curr_price = p*up_price + (1-p)*down_price
    curr_price *= math.exp(-r*del_t)
    dic[(maxx,S_cur)] = curr_price
    return curr_price
    
def func(m):
    dic.clear()
    del_t = T/m;
    u_power = sigma*math.sqrt(del_t) + (r-0.5*sigma*sigma)*del_t
    u = math.exp(u_power)
    d_power = -sigma*math.sqrt(del_t) + (r-0.5*sigma*sigma)*del_t
    d = math.exp(d_power)
    p = ((math.exp(r*del_t)) - d)/(u-d)
    return recursive_func(0,S0,S0,u,d,p,del_t,m)
    

time_arr = []

start = time.time()
print("For m =",5,"Initial Option Price is",func(5))
end = time.time()
time_arr.append(end-start)
start = time.time()
print("For m =",10,"Initial Option Price is",func(10))
end = time.time()
time_arr.append(end-start)
start = time.time()
print("For m =",15,"Initial Option Price is",func(15))
end = time.time()
time_arr.append(end-start)
start = time.time()
print("For m =",25,"Initial Option Price is",func(25))
end = time.time()
time_arr.append(end-start)
start = time.time()
print("For m =",50,"Initial Option Price is",func(50))
end = time.time()
time_arr.append(end-start)

print("")
print("For m = 5, Time Taken =",time_arr[0])
print("For m = 10, Time Taken =",time_arr[1])
print("For m = 15, Time Taken =",time_arr[2])
print("For m = 25, Time Taken =",time_arr[3])
print("For m = 50, Time Taken =",time_arr[4])



xx = []
yy = []

for i in range(5,51):
    xx.append(i)
    yy.append(func(i))
    
plt.scatter(xx, yy,c='r',s=10)
plt.plot(xx, yy)
plt.xlabel("Value of M")
plt.ylabel("Initial Option Price")
plt.xticks([*range(5,51,5)])
plt.title("Lookback Option Price at t=0 vs M")
plt.grid(True)
plt.show()