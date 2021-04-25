import time
import math
import numpy as np 
import matplotlib.pyplot as pltb

S0 = 100
T = 1
r = 0.08
sigma = 0.2
K = 100

dic = {}

def recursive_func(n,K,S_cur,u,d,p,del_t,m,ups):
    if (n,ups) in dic:
        return dic[(n,ups)]
    if n==m:
        return max(S_cur-K,0)
    up_price = recursive_func(n+1,K,S_cur*u,u,d,p,del_t,m,ups+1)
    down_price = recursive_func(n+1,K,S_cur*d,u,d,p,del_t,m,ups)
    curr_price = p*up_price + (1-p)*down_price
    curr_price *= math.exp(-r*del_t)
    dic[(n,ups)] = curr_price
    return curr_price
    
def func(m):
    dic.clear()
    del_t = T/m;
    u_power = sigma*math.sqrt(del_t) + (r-0.5*sigma*sigma)*del_t
    u = math.exp(u_power)
    d_power = -sigma*math.sqrt(del_t) + (r-0.5*sigma*sigma)*del_t
    d = math.exp(d_power)
    p = ((math.exp(r*del_t)) - d)/(u-d)
    return recursive_func(0,K,S0,u,d,p,del_t,m,0)

def func1(m):
    del_t = T/m;
    u_power = sigma*math.sqrt(del_t) + (r-0.5*sigma*sigma)*del_t
    u = math.exp(u_power)
    d_power = -sigma*math.sqrt(del_t) + (r-0.5*sigma*sigma)*del_t
    d = math.exp(d_power)
    p = ((math.exp(r*del_t)) - d)/(u-d)
    return recursive_func1(0,K,S0,u,d,p,del_t,m)

def recursive_func1(n,K,S_cur,u,d,p,del_t,m):
    if n==m:
        return max(S_cur-K,0)
    up_price = recursive_func1(n+1,K,S_cur*u,u,d,p,del_t,m)
    down_price = recursive_func1(n+1,K,S_cur*d,u,d,p,del_t,m)
    curr_price = p*up_price + (1-p)*down_price
    curr_price *= math.exp(-r*del_t)
    return curr_price
    

print("###############################################################")
print("Case1 : Exponential Calculation")
time_arr = []

start = time.time()
print("For m =",5,"Initial Option Price is",func1(5))
end = time.time()
time_arr.append(end-start)
start = time.time()
print("For m =",10,"Initial Option Price is",func1(10))
end = time.time()
time_arr.append(end-start)
start = time.time()
print("For m =",15,"Initial Option Price is",func1(15))
end = time.time()
time_arr.append(end-start)
start = time.time()
print("For m =",20,"Initial Option Price is",func1(20))
end = time.time()
time_arr.append(end-start)
# start = time.time()
# print("For m =",25,"Initial Option Price is",func1(25))
# end = time.time()
# time_arr.append(end-start)

print("")
print("For m = 5, Time Taken =",time_arr[0])
print("For m = 10, Time Taken =",time_arr[1])
print("For m = 15, Time Taken =",time_arr[2])
print("For m = 20, Time Taken =",time_arr[3])
# print("For m = 25, Time Taken =",time_arr[4])
    
print("###############################################################")
print("Case2 : Markov Based Optimized Calculation")
time_arr = []

start = time.time()
print("For m =",20,"Initial Option Price is",func(20))
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
start = time.time()
print("For m =",100,"Initial Option Price is",func(200))
end = time.time()
time_arr.append(end-start)
start = time.time()
print("For m =",400,"Initial Option Price is",func(400))
end = time.time()
time_arr.append(end-start)
start = time.time()
print("For m =",900,"Initial Option Price is",func(900))
end = time.time()
time_arr.append(end-start)

print("")
print("For m = 20, Time Taken =",time_arr[0])
print("For m = 25, Time Taken =",time_arr[1])
print("For m = 50, Time Taken =",time_arr[2])
print("For m = 200, Time Taken =",time_arr[3])
print("For m = 400, Time Taken =",time_arr[4])
print("For m = 900, Time Taken =",time_arr[5])





