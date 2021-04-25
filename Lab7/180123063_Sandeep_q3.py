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
x=np.linspace(0.5,1.5,100)
t=np.linspace(0,0.99,100)
bsm_c={};bsm_p={}
xx=[];TT=[]
bsm_cc=[];bsm_pp=[]

for i in range(0,len(t)):
    for j in range(0,100):
        bsm_c[i,j]=bsm_call(x[j],K,T,t[i],r,sigma)
        bsm_p[i,j]=bsm_put(x[j],K,T,t[i],r,sigma)
        xx.append(x[j]);TT.append(t[i])
        bsm_cc.append(bsm_c[i,j]);bsm_pp.append(bsm_p[i,j])
        
ax = plt.axes(projection ='3d') 
X = np.reshape(xx, (100, 100))
Y = np.reshape(TT, (100, 100))
Z = np.reshape(bsm_cc, (100, 100))
ax.plot_surface(X, Y, Z,cmap ='plasma',edgecolor='green')

ax.set_title('Smooth 3D plot - C(t,x) varying t and x' )
ax.set_xlabel('x (Stock Price)') ;ax.set_ylabel('t (Time)');ax.set_zlabel('C(t,x)',labelpad=10)
ax.view_init(40, 90)
plt.show()

ax = plt.axes(projection ='3d') 
X = np.reshape(xx, (100, 100))
Y = np.reshape(TT, (100, 100))
Z = np.reshape(bsm_pp, (100, 100))
ax.view_init(40, 90)
ax.plot_surface(X, Y, Z, cmap ='viridis',edgecolor='blue')
ax.set_title('Smooth 3D plot - P(t,x) varying t and x' )
ax.set_xlabel('x (Stock Price)') ;ax.set_ylabel('t (Time)');ax.set_zlabel('P(t,x)',labelpad=10)
plt.show()