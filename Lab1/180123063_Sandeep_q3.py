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
    


def func_call(m,t):
    print("t = ",t)
    
    print("UPS"," DOWNS","   CALL OPTION PRICE")
    del_t = T/m;
    u_power = sigma*math.sqrt(del_t) + (r-0.5*sigma*sigma)*del_t
    u = math.exp(u_power)
    d_power = -sigma*math.sqrt(del_t) + (r-0.5*sigma*sigma)*del_t
    d = math.exp(d_power)
    
    if check_no_arbitrage(d,math.exp(r*del_t),u) == False:
        print("NO ARBITRAGE CONDITION FAILED FOR m = ",m);
        return
    
    p = ((math.exp(r*del_t)) - d)/(u-d)
    call_option_price = 0
    t_rem = (int) (m - t/del_t) #number of time periods remaining
    t_occ = (int) (t/del_t) #number of time periods occurred
    
    for i in range(0,t_occ+1):
        ups = i
        downs = t_occ - i
        S_init = S0 * math.pow(u,ups) * math.pow(d,downs)  
        for k in range(0,t_rem+1):
            ST = S_init * math.pow(u,k) * math.pow(d,t_rem-k)
            call_payoff = max(ST-K,0)
            call_option_price += math.comb(t_rem,k) * math.pow(p,k) * math.pow((1-p),t_rem-k) * call_payoff
        
        print(ups,"    ",downs,"    ",call_option_price/math.exp(r*del_t*t_rem))
        call_option_price = 0
        
    
    print("")
    
    
    
def func_put(m,t):
    print("t = ",t)
    
    print("UPS"," DOWNS","   PUT OPTION PRICE")
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
    t_rem = (int) (m - t/del_t) #number of time periods remaining
    t_occ = (int) (t/del_t) #number of time periods occurred
    
    for i in range(0,t_occ+1):
        ups = i
        downs = t_occ - i
        S_init = S0 * math.pow(u,ups) * math.pow(d,downs)  
        for k in range(0,t_rem+1):
            ST = S_init * math.pow(u,k) * math.pow(d,t_rem-k)
            put_payoff = max(K-ST,0)
            put_option_price += math.comb(t_rem,k) * math.pow(p,k) * math.pow((1-p),t_rem-k) * put_payoff
        
        print(ups,"    ",downs,"    ",put_option_price/math.exp(r*del_t*t_rem))
        put_option_price = 0
        
    
    print("")
    
    
print("M=20")

func_call(20,0)
func_call(20,0.5)
func_call(20,1)
func_call(20,1.5)
func_call(20,3)
func_call(20,4.5)

print("-------------------------------------------")
print("M=20")

func_put(20,0)
func_put(20,0.5)
func_put(20,1)
func_put(20,1.5)
func_put(20,3)
func_put(20,4.5)
