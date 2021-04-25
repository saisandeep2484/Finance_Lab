import numpy as np
import matplotlib.pyplot as plt
import math

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

T = 1;K = 1;r = 0.05;sigma = 0.6
t = [0,0.2,0.4,0.6,0.8,1]
x = np.linspace(0.1,2.1,25)

for tt in t:
    bsm_c = [];bsm_p = []
    
    for i in x:
        bsm_p.append(bsm_put(i,K,T,tt,r,sigma))
        bsm_c.append(bsm_call(i,K,T,tt,r,sigma))
        
    plt.plot(x,bsm_p,label='P(t,x)',c='b')    
    plt.plot(x,bsm_c,label='C(t,x)',c='g')
    
    plt.title('C(t,x) and P(t,x) for t = '+str(tt)+' (BSM Model)')
    plt.xlabel('x (Stock Price)')
    plt.ylabel('Option Price')
    plt.legend()
    plt.show()

bsm_c={};bsm_p={}
xx=[];TT=[]
bsm_cc=[];bsm_pp=[]


for i in range(0,len(t)):
    for j in range(0,25):
        bsm_c[i,j] = bsm_call(x[j],K,T,t[i],r,sigma)
        bsm_p[i,j] = bsm_put(x[j],K,T,t[i],r,sigma)
        xx.append(x[j]);TT.append(t[i]);
        bsm_cc.append(bsm_c[i,j]);bsm_pp.append(bsm_p[i,j])

ax = plt.axes(projection ='3d') 
X = np.reshape(xx, (6, 25))
Y = np.reshape(TT, (6, 25))
Z = np.reshape(bsm_cc, (6, 25))
ax.plot_wireframe(X, Y, Z, edgecolor ='green',rstride=1, cstride=0)
ax.plot_surface(X, Y, Z, edgecolor ='None',facecolor='green',alpha = 0.2)

for i in range(0,len(t)):
    for j in range(0,25):
        ax.scatter(x[j],t[i],bsm_c[i,j],marker='x',color='black')
        
ax.set_title('3D plot of C(t,x)' )
ax.set_xlabel('x (Stock Price)') 
ax.set_ylabel('t (Time)')
ax.set_zlabel('Call Option Price = C(t,x)')
ax.zaxis.labelpad = 20
ax.view_init(40, 90)
plt.show()

ax = plt.axes(projection ='3d') 
X = np.reshape(xx, (6,25 ))
Y = np.reshape(TT, (6,25))
Z = np.reshape(bsm_pp, (6, 25))
ax.view_init(40, 90)

for i in range(0,len(t)):
    for j in range(0,25):
        ax.scatter(x[j],t[i],bsm_p[i,j],marker='x',color='black')

ax.plot_wireframe(X, Y, Z, edgecolor ='blue',rstride=1, cstride=0)
ax.plot_surface(X, Y, Z, edgecolor ='None',alpha = 0.2)
ax.set_title('3D plot of P(t,x)' )
ax.set_xlabel('x (Stock Price)') 
ax.set_ylabel('t (Time)')
ax.set_zlabel('Put Option Price = P(t,x)')
ax.zaxis.labelpad = 20
plt.show()