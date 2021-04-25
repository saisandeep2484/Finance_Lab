#import math
import math
import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def check_no_arbitrage(d0,r0,u0):
    if d0 < r0 and r0 < u0 :
        return True
    else :
        return False

def func_set1(S0,K,T,m,r,sigma):
    del_t = T/m;
    u_power = sigma*math.sqrt(del_t)
    u = math.exp(u_power)
    d_power = -sigma*math.sqrt(del_t)
    d = math.exp(d_power)

#     if check_no_arbitrage(d,math.exp(r*del_t),u) == False:
#         print("NO ARBITRAGE CONDITION FAILED FOR m = ",m);
#         return

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
#     print("European Call Option Price =","{:.8f}".format(call_option_price))
#     print("European Put Option Price =","{:.8f}".format(put_option_price))
#     print("")
    return call_option_price,put_option_price
    #print(m,call_option_price,put_option_price)


def func_set2(S0,K,T,m,r,sigma):
    del_t = T/m;
    u_power = sigma*math.sqrt(del_t) + (r-0.5*sigma*sigma)*del_t
    u = math.exp(u_power)
    d_power = -sigma*math.sqrt(del_t) + (r-0.5*sigma*sigma)*del_t
    d = math.exp(d_power)

#     if check_no_arbitrage(d,math.exp(r*del_t),u) == False:
#         print("NO ARBITRAGE CONDITION FAILED FOR m = ",m);
#         return

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
#     print("European Call Option Price =","{:.8f}".format(call_option_price))
#     print("European Put Option Price =","{:.8f}".format(put_option_price))
#     print("")
    return call_option_price,put_option_price
    #print(m,call_option_price,put_option_price)
###############################################################################################################################

print("For Set-1")
c1,c2 = func_set1(100,100,1,100,0.08,0.20)
print("European Call Option Price =","{:.8f}".format(c1))
print("European Put Option Price =","{:.8f}".format(c2))
print("For Set-2")
c1,c2 = func_set2(100,100,1,100,0.08,0.20)
print("European Call Option Price =","{:.8f}".format(c1))
print("European Put Option Price =","{:.8f}".format(c2))

###############################################################################################################################

# vary_S0
# set1
S0_arr = [*range(50, 151, 1)] 
put_arr = []
call_arr = []

for x in S0_arr:
    x1,x2 = func_set1(x,100,1,100,0.08,0.20)
    put_arr.append(x2)
    call_arr.append(x1)
    
plt.plot(S0_arr,call_arr,label = "Call Option Price")
plt.plot(S0_arr,put_arr,label = "Put Option Price")
plt.title("Plot of Option Price vs S(0) for Set1")
plt.xlabel('Stock Price at t=0') 
plt.ylabel('Option Price') 
plt.xticks([*range(50,151,10)])
plt.legend() 
plt.show()

# set2
S0_arr = [*range(50, 151, 1)] 
put_arr = []
call_arr = []

for x in S0_arr:
    x1,x2 = func_set2(x,100,1,100,0.08,0.20)
    put_arr.append(x2)
    call_arr.append(x1)
    
plt.plot(S0_arr,call_arr,label = "Call Option Price")
plt.plot(S0_arr,put_arr,label = "Put Option Price")
plt.title("Plot of Option Price vs S(0) for Set2")
plt.xlabel('Stock Price at t=0') 
plt.ylabel('Option Price') 
plt.xticks([*range(50,151,10)])
plt.legend() 
plt.show()

###############################################################################################################################

# vary_K
# set1
K_arr = [*range(50, 151, 1)] 
put_arr = []
call_arr = []

for x in K_arr:
    x1,x2 = func_set1(100,x,1,100,0.08,0.20)
    put_arr.append(x2)
    call_arr.append(x1)
    
plt.plot(K_arr,call_arr,label = "Call Option Price")
plt.plot(K_arr,put_arr,label = "Put Option Price")
plt.title("Plot of Option Price vs K for Set1")
plt.xlabel('Strike Price (K)') 
plt.ylabel('Option Price') 
plt.xticks([*range(50,151,10)])
plt.legend() 
plt.show()

# set2
K_arr = [*range(50, 151, 1)] 
put_arr = []
call_arr = []

for x in S0_arr:
    x1,x2 = func_set2(100,x,1,100,0.08,0.20)
    put_arr.append(x2)
    call_arr.append(x1)
    
plt.plot(S0_arr,call_arr,label = "Call Option Price")
plt.plot(S0_arr,put_arr,label = "Put Option Price")
plt.title("Plot of Option Price vs K for Set2")
plt.xlabel('Strike Price (K)') 
plt.ylabel('Option Price') 
plt.xticks([*range(50,151,10)])
plt.legend() 
plt.show()

###############################################################################################################################

# vary_r
# set1
r_arr = [x / 100.0 for x in range(0, 101, 1)]
put_arr = []
call_arr = []

for x in r_arr:
    x1,x2 = func_set1(100,100,1,100,x,0.20)
    put_arr.append(x2)
    call_arr.append(x1)
    
plt.plot(r_arr,call_arr,label = "Call Option Price")
plt.plot(r_arr,put_arr,label = "Put Option Price")
plt.title("Plot of Option Price vs Interest Rate (r) for Set1")
plt.xlabel('Interest Rate (r)') 
plt.ylabel('Option Price') 
plt.xticks([x / 100.0 for x in range(0, 101, 10)])
plt.legend() 
plt.show()

# set2
r_arr = [x / 100.0 for x in range(0, 101, 1)]
put_arr = []
call_arr = []

for x in r_arr:
    x1,x2 = func_set2(100,100,1,100,x,0.20)
    put_arr.append(x2)
    call_arr.append(x1)
    
plt.plot(r_arr,call_arr,label = "Call Option Price")
plt.plot(r_arr,put_arr,label = "Put Option Price")
plt.title("Plot of Option Price vs Interest Rate (r) for Set2")
plt.xlabel('Interest Rate (r)') 
plt.ylabel('Option Price') 
plt.xticks([x / 100.0 for x in range(0, 101, 10)])
plt.legend() 
plt.show()

###############################################################################################################################

# vary_sigma
# set1
s_arr = [x / 100.0 for x in range(1, 101, 1)]
put_arr = []
call_arr = []

for x in s_arr:
    x1,x2 = func_set1(100,100,1,100,0.08,x)
    put_arr.append(x2)
    call_arr.append(x1)
    
plt.plot(s_arr,call_arr,label = "Call Option Price")
plt.plot(s_arr,put_arr,label = "Put Option Price")
plt.title("Plot of Option Price vs Sigma for Set1")
plt.xlabel('Sigma') 
plt.ylabel('Option Price') 
plt.xticks([x / 100.0 for x in range(1, 101, 10)])
plt.legend() 
plt.show()

# set2
s_arr = [x / 100.0 for x in range(1, 101, 1)]
put_arr = []
call_arr = []

for x in s_arr:
    x1,x2 = func_set2(100,100,1,100,0.08,x)
    put_arr.append(x2)
    call_arr.append(x1)
    
plt.plot(s_arr,call_arr,label = "Call Option Price")
plt.plot(s_arr,put_arr,label = "Put Option Price")
plt.title("Plot of Option Price vs Sigma for Set2")
plt.xlabel('Sigma') 
plt.ylabel('Option Price') 
plt.xticks([x / 100.0 for x in range(1, 101, 10)])
plt.legend() 
plt.show()

###############################################################################################################################

# vary_M
#K = 95

# set1
m_arr = [*range(50, 151, 1)] 
put_arr = []
call_arr = []

for x in m_arr:
    x1,x2 = func_set1(100,95,1,x,0.08,0.2)
    put_arr.append(x2)
    call_arr.append(x1)
    
plt.plot(m_arr,call_arr,label = "Call Option Price")
plt.title("Plot of Call Option Price vs M for Set1 and K = 95")
plt.xlabel('Number of Steps (M)') 
plt.ylabel('Call Option Price') 
plt.xticks([*range(50, 151, 10)])
plt.show()

plt.plot(m_arr,put_arr,label = "Put Option Price")
plt.title("Plot of Put Option Price vs M for Set1 and K = 95")
plt.xlabel('Number of Steps (M)') 
plt.ylabel('Put Option Price') 
plt.xticks([*range(50, 151, 10)])
plt.show()

# set2
m_arr = [*range(50, 151, 1)] 
put_arr = []
call_arr = []

for x in m_arr:
    x1,x2 = func_set2(100,95,1,x,0.08,0.2)
    put_arr.append(x2)
    call_arr.append(x1)
    
plt.plot(m_arr,call_arr,label = "Call Option Price")
plt.title("Plot of Call Option Price vs M for Set2 and K = 95")
plt.xlabel('Number of Steps (M)') 
plt.ylabel('Call Option Price') 
plt.xticks([*range(50, 151, 10)])
plt.show()

plt.plot(m_arr,put_arr,label = "Put Option Price")
plt.title("Plot of Put Option Price vs M for Set2 and K = 95")
plt.xlabel('Number of Steps (M)') 
plt.ylabel('Put Option Price') 
plt.xticks([*range(50, 151, 10)])
plt.show()

#K = 100

# set1
m_arr = [*range(50, 151, 1)] 
put_arr = []
call_arr = []

for x in m_arr:
    x1,x2 = func_set1(100,100,1,x,0.08,0.2)
    put_arr.append(x2)
    call_arr.append(x1)
    
plt.plot(m_arr,call_arr,label = "Call Option Price")
plt.title("Plot of Call Option Price vs M for Set1 and K = 100")
plt.xlabel('Number of Steps (M)') 
plt.ylabel('Call Option Price') 
plt.xticks([*range(50, 151, 10)])
plt.show()

plt.plot(m_arr,put_arr,label = "Put Option Price")
plt.title("Plot of Put Option Price vs M for Set1 and K = 100")
plt.xlabel('Number of Steps (M)') 
plt.ylabel('Put Option Price') 
plt.xticks([*range(50, 151, 10)])
plt.show()

# set2
m_arr = [*range(50, 151, 1)] 
put_arr = []
call_arr = []

for x in m_arr:
    x1,x2 = func_set2(100,100,1,x,0.08,0.2)
    put_arr.append(x2)
    call_arr.append(x1)
    
plt.plot(m_arr,call_arr,label = "Call Option Price")
plt.title("Plot of Call Option Price vs M for Set2 and K = 100")
plt.xlabel('Number of Steps (M)') 
plt.ylabel('Call Option Price') 
plt.xticks([*range(50, 151, 10)])
plt.show()

plt.plot(m_arr,put_arr,label = "Put Option Price")
plt.title("Plot of Put Option Price vs M for Set2 and K = 100")
plt.xlabel('Number of Steps (M)') 
plt.ylabel('Put Option Price') 
plt.xticks([*range(50, 151, 10)])
plt.show()

#K = 105

# set1
m_arr = [*range(50, 151, 1)] 
put_arr = []
call_arr = []

for x in m_arr:
    x1,x2 = func_set1(100,105,1,x,0.08,0.2)
    put_arr.append(x2)
    call_arr.append(x1)
    
plt.plot(m_arr,call_arr,label = "Call Option Price")
plt.title("Plot of Call Option Price vs M for Set1 and K = 105")
plt.xlabel('Number of Steps (M)') 
plt.ylabel('Call Option Price') 
plt.xticks([*range(50, 151, 10)])
plt.show()

plt.plot(m_arr,put_arr,label = "Put Option Price")
plt.title("Plot of Put Option Price vs M for Set1 and K = 105")
plt.xlabel('Number of Steps (M)') 
plt.ylabel('Put Option Price') 
plt.xticks([*range(50, 151, 10)])
plt.show()

# set2
m_arr = [*range(50, 151, 1)] 
put_arr = []
call_arr = []

for x in m_arr:
    x1,x2 = func_set2(100,105,1,x,0.08,0.2)
    put_arr.append(x2)
    call_arr.append(x1)
    
plt.plot(m_arr,call_arr,label = "Call Option Price")
plt.title("Plot of Call Option Price vs M for Set2 and K = 105")
plt.xlabel('Number of Steps (M)') 
plt.ylabel('Call Option Price') 
plt.xticks([*range(50, 151, 10)])
plt.show()

plt.plot(m_arr,put_arr,label = "Put Option Price")
plt.title("Plot of Put Option Price vs M for Set2 and K = 105")
plt.xlabel('Number of Steps (M)') 
plt.ylabel('Put Option Price') 
plt.xticks([*range(50, 151, 10)])
plt.show()

################################################################################################################################


#S(0) and K
#Set 1
  
x = np.linspace(1,200,20) 
y = np.linspace(200,1,20)

fig = plt.figure()
ax = plt.axes(projection='3d')
for xx in x:
    for yy in y:
        zz1 = func_set1(xx,yy,1,100,0.08,0.2)
        ax.scatter(xx,yy,zz1[0],c='g',linewidths=0.5)
        ax.scatter(xx,yy,zz1[1],c='r',linewidths=0.5)
            

ax.view_init(30,60)


ax.set_xlabel('Stock Price at t = 0 (S(0))')
ax.set_ylabel('Strike Price')
ax.set_zlabel('Option Price')

ax.set_title("Option Price with S(0) and K with set 1")
plt.show()
  
#Set 2
x = np.linspace(1,200,20) 
y = np.linspace(200,1,20)

fig = plt.figure()
ax = plt.axes(projection='3d')
for xx in x:
    for yy in y:
        zz1 = func_set2(xx,yy,1,100,0.08,0.2)
        ax.scatter(xx,yy,zz1[0],c='g',linewidths=0.5)
        ax.scatter(xx,yy,zz1[1],c='r',linewidths=0.5)
            
ax.view_init(30,60)

ax.set_xlabel('Stock Price at t = 0 (S(0))')
ax.set_ylabel('Strike Price')
ax.set_zlabel('Option Price')

ax.set_title("Option Price with S(0) and K with set 2")
plt.show()

###########################################################################################################################
#S(0) and r
#Set 1
  
x = np.linspace(1,200,20) 
y = np.linspace(0.05,1,20)

fig = plt.figure()
ax = plt.axes(projection='3d')
for xx in x:
    for yy in y:
        zz1 = func_set1(xx,100,1,100,yy,0.2)
        ax.scatter(xx,yy,zz1[0],c='g',linewidths=0.5)
        ax.scatter(xx,yy,zz1[1],c='r',linewidths=0.5)
            

ax.view_init(30,210)


ax.set_xlabel('Stock Price at t = 0 (S(0))')
ax.set_ylabel('Interest rate (r)')
ax.set_zlabel('Option Price')

ax.set_title("Option Price with S(0) and r with set 1")
plt.show()

#S(0) and r
#Set 2 
x = np.linspace(1,200,20) 
y = np.linspace(0.05,1,20)

fig = plt.figure()
ax = plt.axes(projection='3d')
for xx in x:
    for yy in y:
        zz1 = func_set2(xx,100,1,100,yy,0.2)
        ax.scatter(xx,yy,zz1[0],c='g',linewidths=0.5)
        ax.scatter(xx,yy,zz1[1],c='r',linewidths=0.5)
            


ax.set_xlabel('Stock Price at t = 0 (S(0))')
ax.set_ylabel('Interest rate (r)')
ax.set_zlabel('Option Price')

ax.set_title("Option Price with S(0) and r with set 2")
plt.show()

###########################################################################################################################
#S(0) and sigma
#Set 1
  
x = np.linspace(1,200,20) 
y = np.linspace(0.05,1,20)

fig = plt.figure()
ax = plt.axes(projection='3d')
for xx in x:
    for yy in y:
        zz1 = func_set1(xx,100,1,100,0.08,yy)
        ax.scatter(xx,yy,zz1[0],c='g',linewidths=0.5)
        ax.scatter(xx,yy,zz1[1],c='r',linewidths=0.5)
            

ax.view_init(30,210)


ax.set_xlabel('Stock Price at t = 0 (S(0))')
ax.set_ylabel('Sigma')
ax.set_zlabel('Option Price')

ax.set_title("Option Price with S(0) and Sigma with set 1")
plt.show()

#S(0) and sigma
#Set 2
x = np.linspace(1,200,20) 
y = np.linspace(0.05,1,20)

fig = plt.figure()
ax = plt.axes(projection='3d')
for xx in x:
    for yy in y:
        zz1 = func_set2(xx,100,1,100,0.08,yy)
        ax.scatter(xx,yy,zz1[0],c='g',linewidths=0.5)
        ax.scatter(xx,yy,zz1[1],c='r',linewidths=0.5)
            


ax.set_xlabel('Stock Price at t = 0 (S(0))')
ax.set_ylabel('Sigma')
ax.set_zlabel('Option Price')

ax.set_title("Option Price with S(0) and Sigma with set 2")
plt.show()

###########################################################################################################################
#S(0) and M
#Set 1
  
x = np.linspace(1,200,20) 
y = [*range(1,200,20)]

fig = plt.figure()
ax = plt.axes(projection='3d')
for xx in x:
    for yy in y:
        zz1 = func_set1(xx,100,1,yy,0.08,0.2)
        ax.scatter(xx,yy,zz1[0],c='g',linewidths=0.5)
        ax.scatter(xx,yy,zz1[1],c='r',linewidths=0.5)
            


ax.set_xlabel('Stock Price at t = 0 (S(0))')
ax.set_ylabel('M')
ax.set_zlabel('Option Price')

ax.set_title("Option Price with S(0) and M with set 1")
plt.show()

#S(0) and M
#Set 2
x = np.linspace(1,200,20) 
y = [*range(1,200,20)]

fig = plt.figure()
ax = plt.axes(projection='3d')
for xx in x:
    for yy in y:
        zz1 = func_set2(xx,100,1,yy,0.08,0.2)
        ax.scatter(xx,yy,zz1[0],c='g',linewidths=0.5)
        ax.scatter(xx,yy,zz1[1],c='r',linewidths=0.5)
            


ax.set_xlabel('Stock Price at t = 0 (S(0))')
ax.set_ylabel('M')
ax.set_zlabel('Option Price')

ax.set_title("Option Price with S(0) and M with set 2")
plt.show()

##########################################################################################################################
#K and r 
#Set 1
  
x = np.linspace(200,1,20)
y = np.linspace(0.05,1,20)

fig = plt.figure()
ax = plt.axes(projection='3d')
for xx in x:
    for yy in y:
        zz1 = func_set1(100,xx,1,100,yy,0.2)
        ax.scatter(xx,yy,zz1[0],c='g',linewidths=0.5)
        ax.scatter(xx,yy,zz1[1],c='r',linewidths=0.5)
            


ax.set_xlabel('Strike Price K')
ax.set_ylabel('Interest Rate (r)')
ax.set_zlabel('Option Price')
ax.view_init(30,90)

ax.set_title("Option Price with K and r with set 1")
plt.show()

#K and r
#Set 2
x = np.linspace(200,1,20)
y = np.linspace(0.05,1,20)

fig = plt.figure()
ax = plt.axes(projection='3d')
for xx in x:
    for yy in y:
        zz1 = func_set2(100,xx,1,100,yy,0.2)
        ax.scatter(xx,yy,zz1[0],c='g',linewidths=0.5)
        ax.scatter(xx,yy,zz1[1],c='r',linewidths=0.5)
            


ax.set_xlabel('Strike Price K')
ax.set_ylabel('Interest Rate (r)')
ax.set_zlabel('Option Price')
ax.view_init(30,90)

ax.set_title("Option Price with K and r with set 2")
plt.show()

#########################################################################################################################
#K and sigma 
#Set 1
  
x = np.linspace(200,1,20)
y = np.linspace(0.05,1,20)

fig = plt.figure()
ax = plt.axes(projection='3d')
for xx in x:
    for yy in y:
        zz1 = func_set1(100,xx,1,100,0.08,yy)
        ax.scatter(xx,yy,zz1[0],c='g',linewidths=0.5)
        ax.scatter(xx,yy,zz1[1],c='r',linewidths=0.5)
            


ax.set_xlabel('Strike Price K')
ax.set_ylabel('Sigma')
ax.set_zlabel('Option Price')
# ax.view_init(30,90)

ax.set_title("Option Price with K and Sigma with set 1")
plt.show()

#K and sigma
#Set 2
x = np.linspace(200,1,20)
y = np.linspace(0.05,1,20)

fig = plt.figure()
ax = plt.axes(projection='3d')
for xx in x:
    for yy in y:
        zz1 = func_set2(100,xx,1,100,0.08,yy)
        ax.scatter(xx,yy,zz1[0],c='g',linewidths=0.5)
        ax.scatter(xx,yy,zz1[1],c='r',linewidths=0.5)
            


ax.set_xlabel('Strike Price K')
ax.set_ylabel('Sigma')
ax.set_zlabel('Option Price')
# ax.view_init(30,90)

ax.set_title("Option Price with K and Sigma with set 2")
plt.show()

#########################################################################################################################
#K and M 
#Set 1
  
x = np.linspace(200,1,20)
y = [*range(1,200,20)]

fig = plt.figure()
ax = plt.axes(projection='3d')
for xx in x:
    for yy in y:
        zz1 = func_set1(100,xx,1,yy,0.08,0.2)
        ax.scatter(xx,yy,zz1[0],c='g',linewidths=0.5)
        ax.scatter(xx,yy,zz1[1],c='r',linewidths=0.5)
            


ax.set_xlabel('Strike Price K')
ax.set_ylabel('M')
ax.set_zlabel('Option Price')
# ax.view_init(30,90)

ax.set_title("Option Price with K and M with set 1")
plt.show()

#K and sigma
#Set 2
x = np.linspace(200,1,20)
y = [*range(1,200,20)]

fig = plt.figure()
ax = plt.axes(projection='3d')
for xx in x:
    for yy in y:
        zz1 = func_set2(100,xx,1,yy,0.08,0.2)
        ax.scatter(xx,yy,zz1[0],c='g',linewidths=0.5)
        ax.scatter(xx,yy,zz1[1],c='r',linewidths=0.5)
            


ax.set_xlabel('Strike Price K')
ax.set_ylabel('M')
ax.set_zlabel('Option Price')
# ax.view_init(30,90)

ax.set_title("Option Price with K and M with set 2")
plt.show()

#########################################################################################################################
#r and sigma 
#Set 1
  
x = np.linspace(0.1,0.5,20)
y = np.linspace(0.1,0.5,20)

fig = plt.figure()
ax = plt.axes(projection='3d')
for xx in x:
    for yy in y:
        zz1 = func_set1(100,100,1,100,xx,yy)
        ax.scatter(xx,yy,zz1[0],c='g',linewidths=0.5)
        ax.scatter(xx,yy,zz1[1],c='r',linewidths=0.5)
            


ax.set_xlabel('Interest Rate (r)')
ax.set_ylabel('Sigma')
ax.set_zlabel('Option Price')
# ax.view_init(30,90)

ax.set_title("Option Price with r and sigma with set 1")
plt.show()

#r and sigma 
#Set 2
  
x = np.linspace(0.01,0.5,20)
y = np.linspace(0.01,0.5,20)

fig = plt.figure()
ax = plt.axes(projection='3d')
for xx in x:
    for yy in y:
        zz1 = func_set2(100,100,1,100,xx,yy)
        ax.scatter(xx,yy,zz1[0],c='g',linewidths=0.5)
        ax.scatter(xx,yy,zz1[1],c='r',linewidths=0.5)
            


ax.set_xlabel('Interest Rate (r)')
ax.set_ylabel('Sigma')
ax.set_zlabel('Option Price')
# ax.view_init(30,90)

ax.set_title("Option Price with r and sigma with set 2")
plt.show()

#########################################################################################################################
#r and M
#Set 1
  
x = np.linspace(0.1,0.5,20)
y = [*range(1,200,20)]

fig = plt.figure()
ax = plt.axes(projection='3d')
for xx in x:
    for yy in y:
        zz1 = func_set1(100,100,1,yy,xx,0.2)
        ax.scatter(xx,yy,zz1[0],c='g',linewidths=0.5)
        ax.scatter(xx,yy,zz1[1],c='r',linewidths=0.5)
            


ax.set_xlabel('Interest Rate (r)')
ax.set_ylabel('M')
ax.set_zlabel('Option Price')
# ax.view_init(30,90)

ax.set_title("Option Price with r and M with set 1")
plt.show()

#r and sigma 
#Set 2
  
x = np.linspace(0.01,0.5,20)
y = [*range(1,200,20)]

fig = plt.figure()
ax = plt.axes(projection='3d')
for xx in x:
    for yy in y:
        zz1 = func_set2(100,100,1,yy,xx,0.2)
        ax.scatter(xx,yy,zz1[0],c='g',linewidths=0.5)
        ax.scatter(xx,yy,zz1[1],c='r',linewidths=0.5)
            


ax.set_xlabel('Interest Rate (r)')
ax.set_ylabel('M')
ax.set_zlabel('Option Price')
# ax.view_init(30,90)

ax.set_title("Option Price with r and M with set 2")
plt.show()

########################################################################################################################
#sigma and M
#Set 1
  
x = np.linspace(0.1,0.5,20)
y = [*range(1,200,20)]

fig = plt.figure()
ax = plt.axes(projection='3d')
for xx in x:
    for yy in y:
        zz1 = func_set1(100,100,1,yy,0.08,xx)
        ax.scatter(xx,yy,zz1[0],c='g',linewidths=0.5)
        ax.scatter(xx,yy,zz1[1],c='r',linewidths=0.5)
            


ax.set_xlabel('Sigma')
ax.set_ylabel('M')
ax.set_zlabel('Option Price')
# ax.view_init(30,90)

ax.set_title("Option Price with Sigma and M with set 1")
plt.show()

#sigma and M 
#Set 2
  
x = np.linspace(0.01,0.5,20)
y = [*range(1,200,20)]

fig = plt.figure()
ax = plt.axes(projection='3d')
for xx in x:
    for yy in y:
        zz1 = func_set2(100,100,1,yy,0.08,xx)
        ax.scatter(xx,yy,zz1[0],c='g',linewidths=0.5)
        ax.scatter(xx,yy,zz1[1],c='r',linewidths=0.5)
            


ax.set_xlabel('Sigma')
ax.set_ylabel('M')
ax.set_zlabel('Option Price')
# ax.view_init(30,90)

ax.set_title("Option Price with Sigma and M with set 2")
plt.show()


