import math
import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable 
from scipy.stats import norm

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

T = 1
K = 1
r = 0.05
sigma = 0.6
t = 0.5 # fix the time
x = 1 # fix the stock price

# Taking 1 at a time
# varying K
bsm_c = [];bsm_p = []

kk = np.linspace(0.5,1.5,100)
for i in kk:
    bsm_p.append(bsm_put(x,i,T,t,r,sigma))
    bsm_c.append(bsm_call(x,i,T,t,r,sigma))

myTable1 = PrettyTable(["Strike Price(K)", "Call Option Price", "Put Option Price"]) 

for i in range(0,len(kk),10):
    myTable1.add_row([round(kk[i],6),round(bsm_c[i],6),round(bsm_p[i],6)])
    
plt.plot(kk,bsm_p,label='P(t,x)',c='b')    
plt.plot(kk,bsm_c,label='C(t,x)',c='g')

plt.title('C(t,x) and P(t,x) varying K (Strike Price)')
plt.xlabel('K (Strike Price)')
plt.ylabel('Option Price')
plt.legend()
plt.show()

print(myTable1)

# varying sigma
bsm_c = [];bsm_p = []
ssigma = np.linspace(0.01,1,100)

myTable2 = PrettyTable(["Sigma", "Call Option Price", "Put Option Price"]) 
for i in ssigma:
    bsm_p.append(bsm_put(x,K,T,t,r,i))
    bsm_c.append(bsm_call(x,K,T,t,r,i))
    
for i in range(0,len(ssigma),10):
    myTable2.add_row([round(ssigma[i],6),round(bsm_c[i],6),round(bsm_p[i],6)])

plt.plot(ssigma,bsm_p,label='P(t,x)',c='b')    
plt.plot(ssigma,bsm_c,label='C(t,x)',c='g')

plt.title('C(t,x) and P(t,x) varying sigma')
plt.xlabel('Sigma')
plt.ylabel('Option Price')
plt.legend()
plt.show()


print(myTable2)

# varying r
bsm_c = [];bsm_p = []
rr = np.linspace(0,1,100)

for i in rr:
    bsm_p.append(bsm_put(x,K,T,t,i,sigma))
    bsm_c.append(bsm_call(x,K,T,t,i,sigma))
    
myTable3 = PrettyTable(["Rate (r)", "Call Option Price", "Put Option Price"]) 

for i in range(0,len(rr),10):
    myTable3.add_row([round(rr[i],6),round(bsm_c[i],6),round(bsm_p[i],6)])
plt.plot(rr,bsm_p,label='P(t,x)',c='b')    
plt.plot(rr,bsm_c,label='C(t,x)',c='g')

plt.title('C(t,x) and P(t,x) varying rate (r)')
plt.xlabel('Rate (r)')
plt.ylabel('Option Price')
plt.legend()
plt.show()

print(myTable3)
# varying T
bsm_c = [];bsm_p = []
TT = np.linspace(0.51,5,100)

for i in TT:
    bsm_p.append(bsm_put(x,K,i,t,r,sigma))
    bsm_c.append(bsm_call(x,K,i,t,r,sigma))
    
myTable4 = PrettyTable(["Final Time (T)", "Call Option Price", "Put Option Price"]) 

for i in range(0,len(TT),10):
    myTable4.add_row([round(TT[i],6),round(bsm_c[i],6),round(bsm_p[i],6)])
plt.plot(TT,bsm_p,label='P(t,x)',c='b')    
plt.plot(TT,bsm_c,label='C(t,x)',c='g')

plt.title('C(t,x) and P(t,x) varying Final Time (T)')
plt.xlabel('Final Time (T)')
plt.ylabel('Option Price')
plt.legend()
plt.show()

print(myTable4)
# Taking 2 at a time

# varying K and sigma


a1=np.linspace(0.5,1.5,20)
aa1=[]
a2=np.linspace(0.01,1,20)
aa2=[]
bsm_c={};bsm_p={}
bsm_cc=[];bsm_pp=[]

for i in range(0,len(a2)):
    for j in range(0,len(a1)):
        bsm_c[i,j] = bsm_call(x,a1[j],T,t,r,a2[i])
        bsm_p[i,j] = bsm_put(x,a1[j],T,t,r,a2[i])
        aa1.append(a1[j]);aa2.append(a2[i]);
        bsm_cc.append(bsm_c[i,j]);bsm_pp.append(bsm_p[i,j])
        
tab = PrettyTable(["Strike Price (K)","Sigma","Call Option Price", "Put Option Price"])

for i in range(0,20,2):
    tab.add_row([round(a1[i],6),round(a2[i],6),round(bsm_c[i,i],6),round(bsm_p[i,i],6)])
ax = plt.axes(projection ='3d') 
X = np.reshape(aa1, (len(a2), len(a1)))
Y = np.reshape(aa2, (len(a2), len(a1)))
Z = np.reshape(bsm_cc, (len(a2), len(a1)))
ax.plot_surface(X, Y, Z,cmap ='plasma', edgecolor ='green')

ax.set_title('3D plot of C(t,x) varying K and sigma' )
ax.set_xlabel('K (Strike Price)') 
ax.set_ylabel('sigma')
ax.set_zlabel('C(t,x)')
ax.view_init(40, 60)
plt.show()

ax = plt.axes(projection ='3d') 
X = np.reshape(aa1, (len(a2), len(a1)))
Y = np.reshape(aa2, (len(a2), len(a1)))
Z = np.reshape(bsm_pp, (len(a2), len(a1)))
ax.view_init(40, 210)
ax.plot_surface(X, Y, Z, cmap ='viridis', edgecolor='pink')
ax.set_title('3D plot of P(t,x) varying K and sigma' )
ax.set_xlabel('K (Strike Price)') 
ax.set_ylabel('sigma')
ax.set_zlabel('P(t,x)')
plt.show()
print(tab)
# varying K and rate


a1=np.linspace(0.5,1.5,20)
aa1=[]
a2=np.linspace(0,1,20)
aa2=[]
bsm_c={};bsm_p={}
bsm_cc=[];bsm_pp=[]

for i in range(0,len(a2)):
    for j in range(0,len(a1)):
        bsm_c[i,j] = bsm_call(x,a1[j],T,t,a2[i],sigma)
        bsm_p[i,j] = bsm_put(x,a1[j],T,t,a2[i],sigma)
        aa1.append(a1[j]);aa2.append(a2[i]);
        bsm_cc.append(bsm_c[i,j]);bsm_pp.append(bsm_p[i,j])
tab = PrettyTable(["Strike Price (K)","Rate (r)","Call Option Price", "Put Option Price"])

for i in range(0,20,2):
    tab.add_row([round(a1[i],6),round(a2[i],6),round(bsm_c[i,i],6),round(bsm_p[i,i],6)])
    
ax = plt.axes(projection ='3d') 
X = np.reshape(aa1, (len(a2), len(a1)))
Y = np.reshape(aa2, (len(a2), len(a1)))
Z = np.reshape(bsm_cc, (len(a2), len(a1)))
ax.plot_surface(X, Y, Z,cmap ='plasma', edgecolor ='green')

ax.set_title('3D plot of C(t,x) varying K and r' )
ax.set_xlabel('K (Strike Price)') 
ax.set_ylabel('r (rate)')
ax.set_zlabel('C(t,x)')
ax.view_init(40, 60)
plt.show()

ax = plt.axes(projection ='3d') 
X = np.reshape(aa1, (len(a2), len(a1)))
Y = np.reshape(aa2, (len(a2), len(a1)))
Z = np.reshape(bsm_pp, (len(a2), len(a1)))
ax.view_init(40, 60)
ax.plot_surface(X, Y, Z, cmap ='viridis', edgecolor='pink')
ax.set_title('3D plot of P(t,x) varying K and r' )
ax.set_xlabel('K (Strike Price)') 
ax.set_ylabel('r (rate)')
ax.set_zlabel('P(t,x)')
plt.show()
print(tab)
# varying K and T


a1=np.linspace(0.5,1.5,20)
aa1=[]
a2=np.linspace(0.5,5,20)
aa2=[]
bsm_c={};bsm_p={}
bsm_cc=[];bsm_pp=[]

for i in range(0,len(a2)):
    for j in range(0,len(a1)):
        bsm_c[i,j] = bsm_call(x,a1[j],a2[i],t,r,sigma)
        bsm_p[i,j] = bsm_put(x,a1[j],a2[i],t,r,sigma)
        aa1.append(a1[j]);aa2.append(a2[i]);
        bsm_cc.append(bsm_c[i,j]);bsm_pp.append(bsm_p[i,j])
tab = PrettyTable(["Strike Price (K)","Final Time (T)","Call Option Price", "Put Option Price"])

for i in range(0,20,2):
    tab.add_row([round(a1[i],6),round(a2[i],6),round(bsm_c[i,i],6),round(bsm_p[i,i],6)])

ax = plt.axes(projection ='3d') 
X = np.reshape(aa1, (len(a2), len(a1)))
Y = np.reshape(aa2, (len(a2), len(a1)))
Z = np.reshape(bsm_cc, (len(a2), len(a1)))
ax.plot_surface(X, Y, Z,cmap ='plasma', edgecolor ='green')

ax.set_title('3D plot of C(t,x) varying K and T(Final Time)' )
ax.set_xlabel('K (Strike Price)') 
ax.set_ylabel('T (Final Time)')
ax.set_zlabel('C(t,x)')
ax.view_init(40, 60)
plt.show()

ax = plt.axes(projection ='3d') 
X = np.reshape(aa1, (len(a2), len(a1)))
Y = np.reshape(aa2, (len(a2), len(a1)))
Z = np.reshape(bsm_pp, (len(a2), len(a1)))
ax.view_init(40, 210)
ax.plot_surface(X, Y, Z, cmap ='viridis', edgecolor='pink')
ax.set_title('3D plot of P(t,x) varying K and T(Final Time)' )
ax.set_xlabel('K (Strike Price)') 
ax.set_ylabel('T (Final Time)')
ax.set_zlabel('P(t,x)')
plt.show()
print(tab)

# varying r and T

a1=np.linspace(0,1,100)
aa1=[]
a2=np.linspace(0.5,5,20)
aa2=[]
bsm_c={};bsm_p={}
bsm_cc=[];bsm_pp=[]

for i in range(0,len(a2)):
    for j in range(0,len(a1)):
        bsm_c[i,j] = bsm_call(x,K,a2[i],t,a1[j],sigma)
        bsm_p[i,j] = bsm_put(x,K,a2[i],t,a1[j],sigma)
        aa1.append(a1[j]);aa2.append(a2[i]);
        bsm_cc.append(bsm_c[i,j]);bsm_pp.append(bsm_p[i,j])
tab = PrettyTable(["Rate (r)","Final Time (T)","Call Option Price", "Put Option Price"])
for i in range(0,20,2):
    tab.add_row([round(a1[5*i],6),round(a2[i],6),round(bsm_c[i,5*i],6),round(bsm_p[i,5*i],6)])
    
ax = plt.axes(projection ='3d') 
X = np.reshape(aa1, (len(a2), len(a1)))
Y = np.reshape(aa2, (len(a2), len(a1)))
Z = np.reshape(bsm_cc, (len(a2), len(a1)))
ax.plot_surface(X, Y, Z,cmap ='plasma', edgecolor ='green')

ax.set_title('3D plot of C(t,x) varying r (rate) and T(Final Time)' )
ax.set_xlabel('r (rate)') 
ax.set_ylabel('T (Final Time)')
ax.set_zlabel('C(t,x)')
# ax.view_init(40, 60)
plt.show()

ax = plt.axes(projection ='3d') 
X = np.reshape(aa1, (len(a2), len(a1)))
Y = np.reshape(aa2, (len(a2), len(a1)))
Z = np.reshape(bsm_pp, (len(a2), len(a1)))
# ax.view_init(40, 60)
ax.plot_surface(X, Y, Z, cmap ='viridis', edgecolor='pink')
ax.set_title('3D plot of P(t,x) varying r(rate) and T(Final Time)' )
ax.set_xlabel('r (rate)') 
ax.set_ylabel('T (Final Time)')
ax.set_zlabel('P(t,x)')
plt.show()
print(tab)
# varying r and sigma

a1=np.linspace(0,1,100)
aa1=[]
a2=np.linspace(0.01,1,20)
aa2=[]
bsm_c={};bsm_p={}
bsm_cc=[];bsm_pp=[]

for i in range(0,len(a2)):
    for j in range(0,len(a1)):
        bsm_c[i,j] = bsm_call(x,K,T,t,a1[j],a2[i])
        bsm_p[i,j] = bsm_put(x,K,T,t,a1[j],a2[i])
        aa1.append(a1[j]);aa2.append(a2[i]);
        bsm_cc.append(bsm_c[i,j]);bsm_pp.append(bsm_p[i,j])
tab = PrettyTable(["Rate (r)","sigma","Call Option Price", "Put Option Price"])
for i in range(0,20,2):
    tab.add_row([round(a1[5*i],6),round(a2[i],6),round(bsm_c[i,5*i],6),round(bsm_p[i,5*i],6)])
ax = plt.axes(projection ='3d') 
X = np.reshape(aa1, (len(a2), len(a1)))
Y = np.reshape(aa2, (len(a2), len(a1)))
Z = np.reshape(bsm_cc, (len(a2), len(a1)))
ax.plot_surface(X, Y, Z,cmap ='plasma', edgecolor ='green')

ax.set_title('3D plot of C(t,x) varying r (rate) and sigma' )
ax.set_xlabel('r (rate)') 
ax.set_ylabel('sigma')
ax.set_zlabel('C(t,x)')
ax.view_init(40, 210)
plt.show()

ax = plt.axes(projection ='3d') 
X = np.reshape(aa1, (len(a2), len(a1)))
Y = np.reshape(aa2, (len(a2), len(a1)))
Z = np.reshape(bsm_pp, (len(a2), len(a1)))
ax.view_init(40, 30)
ax.plot_surface(X, Y, Z, cmap ='viridis', edgecolor='pink')
ax.set_title('3D plot of P(t,x) varying r(rate) and sigma' )
ax.set_xlabel('r (rate)') 
ax.set_ylabel('sigma')
ax.set_zlabel('P(t,x)')
plt.show()
print(tab)
# varying T and sigma

a1=np.linspace(0.5,5,20)
aa1=[]
a2=np.linspace(0.01,1,20)
aa2=[]
bsm_c={};bsm_p={}
bsm_cc=[];bsm_pp=[]

for i in range(0,len(a2)):
    for j in range(0,len(a1)):
        bsm_c[i,j] = bsm_call(x,K,T,t,a1[j],a2[i])
        bsm_p[i,j] = bsm_put(x,K,T,t,a1[j],a2[i])
        aa1.append(a1[j]);aa2.append(a2[i]);
        bsm_cc.append(bsm_c[i,j]);bsm_pp.append(bsm_p[i,j])
tab = PrettyTable(["Final Time (T)","sigma","Call Option Price", "Put Option Price"])
for i in range(0,20,2):
    tab.add_row([round(a1[i],6),round(a2[i],6),round(bsm_c[i,i],6),round(bsm_p[i,i],6)])
ax = plt.axes(projection ='3d') 
X = np.reshape(aa1, (len(a2), len(a1)))
Y = np.reshape(aa2, (len(a2), len(a1)))
Z = np.reshape(bsm_cc, (len(a2), len(a1)))
ax.plot_surface(X, Y, Z,cmap ='plasma', edgecolor ='green')

ax.set_title('3D plot of C(t,x) varying T (Final time) and sigma' )
ax.set_xlabel('T (Final Time)') 
ax.set_ylabel('sigma')
ax.set_zlabel('C(t,x)')
ax.view_init(40, 210)
plt.show()

ax = plt.axes(projection ='3d') 
X = np.reshape(aa1, (len(a2), len(a1)))
Y = np.reshape(aa2, (len(a2), len(a1)))
Z = np.reshape(bsm_pp, (len(a2), len(a1)))
ax.view_init(40, 30)
ax.plot_surface(X, Y, Z, cmap ='viridis', edgecolor='pink')
ax.set_title('3D plot of P(t,x) varying T (Final time) and sigma' )
ax.set_xlabel('T (Final time)') 
ax.set_ylabel('sigma')
ax.set_zlabel('P(t,x)')
plt.show()
print(tab)