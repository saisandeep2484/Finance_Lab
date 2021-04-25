#import math
import math


S0 = 100
K = 105
T = 5
r = 0.05
sigma = 0.3

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
    print(m,"         ","{:.8f}".format(call_option_price),"              ","{:.8f}".format(put_option_price))
    #print(m,call_option_price,put_option_price)
    

    
print("M "," European Call Option Price "," European Put Option Price")
func(1)
func(5)
func(10)
func(20)
func(50)
func(100)
func(200)
func(400)
