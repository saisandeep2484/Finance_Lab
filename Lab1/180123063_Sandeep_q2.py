#import math
#pip install matplotlib 
import math
import matplotlib.pyplot as plt

S0 = 100
K = 105
T = 5
r = 0.05
sigma = 0.3

put_1 = [] #to store put option prices when m increments by 1
put_5 = [] #to store put option prices when m increments by 5
call_1 = [] #to store put option prices when m increments by 1
call_5 = [] #to store put option prices when m increments by 5

def check_no_arbitrage(d0,r0,u0):
    if d0 < r0 and r0 < u0 :
        return True
    else :
        return False
    


def func(m):
    del_t = T/m;
    u_power = sigma*math.sqrt(del_t) + (r-0.5*sigma*sigma)*del_t
    u = math.exp(u_power)
    d_power = -sigma*math.sqrt(del_t) + (r-0.5*sigma*sigma)*del_t
    d = math.exp(d_power)
    
    if check_no_arbitrage(d,math.exp(r*del_t),u) == False:
        print("NO ARBITRAGE CONDITION FAILED FOR m = ",m);
        return
    
    p = ((math.exp(r*del_t)) - d)/(u-d)
    put_option_price = 0
    call_option_price = 0
    for k in range(0,m+1):
        ST = S0 * math.pow(u,k) * math.pow(d,m-k)
        put_payoff = max(K-ST,0)
        call_payoff = max(ST-K,0)
        put_option_price += math.comb(m,k) * math.pow(p,k) * math.pow((1-p),m-k) * put_payoff
        call_option_price += math.comb(m,k) * math.pow(p,k) * math.pow((1-p),m-k) * call_payoff
        
    put_option_price = put_option_price/math.exp(r*T)
    call_option_price = call_option_price/math.exp(r*T)
    put_1.append(put_option_price)
    call_1.append(call_option_price)
    if m%5==0:
        put_5.append(put_option_price)
        call_5.append(call_option_price)

x1 = []
x5 = []

for i in range(1,201):
    x1.append(i)
    func(i)
    if i%5==0:
        x5.append(i)
    




plt.plot(x1,call_1)
plt.ylabel('European Call Option Price')
plt.xlabel('M (1 Step Increment)')
plt.show()

plt.plot(x5,call_5)
plt.ylabel('European Call Option Price')
plt.xlabel('M (5 Step Increment)')
plt.show()

plt.plot(x1,put_1)
plt.ylabel('European Put Option Price')
plt.xlabel('M (1 Step Increment)')
plt.show()

plt.plot(x5,put_5)
plt.ylabel('European Put Option Price')
plt.xlabel('M (5 Step Increment)')
plt.show()
