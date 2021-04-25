import math
import random
from decimal import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d 

m = np.array([[0.1,0.2,0.15]])
u = np.array([[1,1,1]])
C = np.array([[0.005,-0.010,0.004],[-0.010,0.040,-0.002],[0.004,-0.002,0.023]])
C_inv = np.linalg.inv(C)

mu_arr = np.linspace(0,0.5,100001)
xx1 = []
xx2 = []
SD1_arr = []
SD2_arr = []

M11 = (m.dot(C_inv)).dot(m.T)
M12 = (u.dot(C_inv)).dot(m.T)
M21 = (m.dot(C_inv)).dot(u.T)
M22 = (u.dot(C_inv)).dot(u.T)

M = np.array([[M11[0][0],M12[0][0]],[M21[0][0],M22[0][0]]])
M_inv = np.linalg.inv(M)

Global_min_mu = M12/M22

small = 0.20
big = 0.10

for mu in mu_arr:
    lamda = 2*M_inv.dot((np.array([[mu,1]])).T)
    w = (lamda[0][0]* (m.dot(C_inv)) + (lamda[1][0]*(u.dot(C_inv))))/2
    var = w.dot(C.dot(w.T))
    if mu<Global_min_mu[0][0]:
        if w[0][0]<0 or w[0][1]<0 or w[0][2]<0: 
            continue
        xx1.append(mu)
        SD1_arr.append(math.sqrt(var[0][0]))
        small = min(small,mu)
    else :
        if w[0][0]<0 or w[0][1]<0 or w[0][1]<0: 
            continue
        xx2.append(mu)
        SD2_arr.append(math.sqrt(var[0][0]))
        big = min(big,mu)
    
# Part 1
plt.plot(SD2_arr, xx2,c='r',label = "Markowitz Efficient Frontier")
plt.plot(SD1_arr, xx1,c='r',label = "Minimum Variance Curve",linestyle='dashed')
plt.xlabel("Standard Variation (sigma)")
plt.ylabel("Return Value (mu)")
plt.yticks(np.linspace(0,0.2,11))
plt.xticks(np.linspace(0,0.2,11))
plt.title("Markowitz efficient Frontier with no short sales")
plt.grid(True)
plt.legend()
plt.show()

# Part 2

wt = []
wt2 = []
def func(m,u,C,col,name):
    C_inv = np.linalg.inv(C)

    mu_arr = np.linspace(0.1,0.2,401)
    x1 = []
    S1_arr = []
    x2 = []
    S2_arr = []

    M11 = (m.dot(C_inv)).dot(m.T)
    M12 = (u.dot(C_inv)).dot(m.T)
    M21 = (m.dot(C_inv)).dot(u.T)
    M22 = (u.dot(C_inv)).dot(u.T)

    M = np.array([[M11[0][0],M12[0][0]],[M21[0][0],M22[0][0]]])
    M_inv = np.linalg.inv(M)
    
    glo_min_mu = M12/M22
    
    for mu in mu_arr:
        lamda = 2*M_inv.dot((np.array([[mu,1]])).T)
        w = (lamda[0][0]* (m.dot(C_inv)) + (lamda[1][0]*(u.dot(C_inv))))/2
        var = w.dot(C.dot(w.T))
        
        if mu<glo_min_mu[0][0]:
            if math.sqrt(var[0][0])>0.201:
                continue
                
            x1.append(mu)
            S1_arr.append(math.sqrt(var[0][0]))
        else :
            if math.sqrt(var[0][0])>0.21:
                continue
            
            x2.append(mu)
            S2_arr.append(math.sqrt(var[0][0]))
            
        if len(w[0])==3:
            if w[0][0]<0 or w[0][1]<0 or w[0][2]<0: 
                continue
            wt.append((w[0][0],w[0][1],w[0][2]))
        if len(w[0])==2:
            if w[0][0]<0 or w[0][1]<0: 
                continue
            wt2.append((w[0][0],w[0][1]))
        
    
            
    plt.plot(S2_arr, x2,c=col,label = "EF-"+name)
    plt.plot(S1_arr, x1,c=col,label = "MVC-"+name,linestyle='dashed')
    plt.xlabel("Standard Variation (sigma)")
    plt.ylabel("Return Value (mu)")
    plt.grid(True)
    plt.legend()

def populate():
    for i in range(0,1000):
        i1 = random.randint(0,1000)
        i2 = random.randint(0,1000-i1)
        w1 = i1/1000
        w2 = i2/1000
        w3 = 1-w1-w2
        w = np.array([[w1,w2,w3]])
        sig_ins = math.sqrt( (w.dot(C.dot(w.T)))[0][0] )
        mu_ins = m.dot(w.T)
        plt.scatter(sig_ins,mu_ins,c='k',s=1)
        
    plt.xlabel("Standard Variation (sigma)")
    plt.ylabel("Return Value (mu)")
    plt.grid(True)
    plt.legend()
    

func(m,u,C,'r'," w1,w2,w3")

m12 = np.array([[0.1,0.2]])
u12 = np.array([[1,1]])
C12 = np.array([[0.005,-0.010],[-0.010,0.040]])
func(m12,u12,C12,'g'," w1,w2")

m23 = np.array([[0.2,0.15]])
u23 = np.array([[1,1]])
C23 = np.array([[0.040,-0.002],[-0.002,0.023]])
func(m23,u23,C23,'b'," w2,w3")

m31 = np.array([[0.1,0.15]])
u31 = np.array([[1,1]])
C31 = np.array([[0.005,0.004],[0.004,0.023]])
func(m31,u31,C31,'y'," w3,w1")

populate()

plt.title("MVCs with No Short Sales")
plt.show()


# Part 3

fig = plt.figure() 
ax = plt.axes(projection ='3d') 

for ele in wt:
    ax.scatter(ele[0], ele[1], ele[2],c='g',s=5,label="weights")
    
ax.set_title('3d plot of weights (No Short Sales Allowed)')
ax.set(xlabel = "w1",ylabel="w2",zlabel="w3")
normal = np.array([1, 1, 1])
xx, yy = np.meshgrid(np.linspace(0,1,100),np.linspace(0,1,100))
z = (-normal[0] * xx - normal[1] * yy +1) * 1. /normal[2]

ax.plot_surface(xx, yy, z, alpha=0.4,label="w1+w2+w3=1")
ax.view_init(45,45)
plt.show() 

ele = wt[0]
ww = np.array([[ele[0]],[ele[1]],[ele[2]]])
val1 = w.dot(C)[0][0]
val2 = w.dot(C)[0][1]
val3 = w.dot(C)[0][2]
cons_gamma = (m[0][0]-m[0][1])/(val1-val2)
cons_mu = m[0][0] - cons_gamma*val1 
print("The value of gamma for weights equation is:",cons_gamma)
print("The value of mu for weights equation is:",cons_mu)


arr1 = []
arr2 = []
for ele in wt2:
    arr1.append(ele[0])
    arr2.append(ele[1])
    
plt.plot(arr1,arr2)
plt.xlabel("w1")
plt.ylabel("w2")
plt.title("w1 vs w2 (No Short Sales)")
plt.grid(True)
plt.show()


