import math
import numpy as np
import matplotlib.pyplot as plt

m = np.array([[0.1,0.2,0.15]])
u = np.array([[1,1,1]])
C = np.array([[0.005,-0.010,0.004],[-0.010,0.040,-0.002],[0.004,-0.002,0.023]])
C_inv = np.linalg.inv(C)

mu_arr = np.linspace(0,0.5,101)
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

sample = [] # for part B
cn = 0
Global_min_mu = M12/M22

for mu in mu_arr:
    lamda = 2*M_inv.dot((np.array([[mu,1]])).T)
    w = (lamda[0][0]* (m.dot(C_inv)) + (lamda[1][0]*(u.dot(C_inv))))/2
    var = w.dot(C.dot(w.T))
    if mu<Global_min_mu[0][0]:
        xx1.append(mu)
        SD1_arr.append(math.sqrt(var[0][0]))
        if cn%10 ==0:
            sample.append((mu,SD1_arr[-1],w[0][0],w[0][1],w[0][2]))
        cn+=1
    else :
        xx2.append(mu)
        SD2_arr.append(math.sqrt(var[0][0]))
        if cn%10 ==0:
            sample.append((mu,SD2_arr[-1],w[0][0],w[0][1],w[0][2]))
        cn+=1
    
# Part A
Global_min_mu = M12/M22
lamda = 2*M_inv.dot((np.array([[Global_min_mu[0][0],1]])).T)
lam1 = lamda[0][0]
lam2 = lamda[1][0]
w = lam1*(m.dot(C_inv)) + lam2*(u.dot(C_inv))
w = w/2
Global_min_var = w.dot(C.dot(w.T))

plt.scatter(math.sqrt(Global_min_var[0][0]),Global_min_mu[0][0],label="Global Min Variance Portfolio")
plt.plot(SD2_arr, xx2,c='r',label = "Markowitz Efficient Frontier")
plt.plot(SD1_arr, xx1,c='r',label = "Minimum Variance Curve",linestyle='dashed')
plt.xlabel("Standard Variation (sigma)")
plt.ylabel("Return Value (mu)")
plt.yticks(np.linspace(0,0.5,11))
plt.xticks(np.linspace(0,1,11))
plt.title("Markowitz efficient Frontier")
plt.grid(True)
plt.legend()
plt.show()
 
# Part B    
print("Return     Risk (SD)        w1            w2            w3")
for ele in sample:
    for j in range(0,5):
        print(round(ele[j],3),end = "         ")
    print("")
    

# Part C
# max
sig = 0.15

val = M22.dot(M11) - M12.dot(M21)

tem = 4*(M12.dot(M12)) - 4*(M22.dot(M11 - sig*sig*val))
tem = tem[0][0]
mu = (2*M12 + np.array([[math.sqrt(tem)]]))/(2*M22)

y = np.array([[mu[0][0],1]])

M = np.array([[M11[0][0],M12[0][0]],[M21[0][0],M22[0][0]]])
M_inv = np.linalg.inv(M)

lamda = 2*M_inv.dot(y.T)

w = (lamda[0][0]*m.dot(C_inv) + lamda[1][0]*u.dot(C_inv))/2

print("")
print("For a 15% risk, the maximum return is",round(mu[0][0],4))
print("Corresponding Portfolio :","w1 =",round(w[0][0],4),"w2 =",round(w[0][1],4),"w3 =",round(w[0][2],4))

# min
mu = (2*M12 - np.array([[math.sqrt(tem)]]))/(2*M22)

y = np.array([[mu[0][0],1]])

M = np.array([[M11[0][0],M12[0][0]],[M21[0][0],M22[0][0]]])
M_inv = np.linalg.inv(M)

lamda = 2*M_inv.dot(y.T)

w = (lamda[0][0]*m.dot(C_inv) + lamda[1][0]*u.dot(C_inv))/2

print("")
print("For a 15% risk, the minimum return is",round(mu[0][0],4))
print("Corresponding Portfolio :","w1 =",round(w[0][0],4),"w2 =",round(w[0][1],4),"w3 =",round(w[0][2],4))

# Part D

mu = 0.18
lamda = 2*M_inv.dot((np.array([[mu,1]])).T)
    
lam1 = lamda[0][0]
lam2 = lamda[1][0]
w = lam1* (m.dot(C_inv)) + lam2* (u.dot(C_inv))
w = w/2
var = w.dot(C.dot(w.T))
print("")
print("For a 18% return, the minimum risk is",round(math.sqrt(var[0][0])*100,4),"%")
print("Corresponding Portfolio :","w1 =",round(w[0][0],4),"w2 =",round(w[0][1],4),"w3 =",round(w[0][2],4))

# Part E
rf = 0.10

num = (m-rf*u).dot(C_inv)
denom = (m-rf*u).dot(C_inv.dot(u.T))
w = num/denom
mu = w.dot(m.T)
var = w.dot(C.dot(w.T))

print("")
print("For a 10% risk free return, the return on market portfolio is",round((mu[0][0]),4))
print("For a 10% risk free return, the risk on market portfolio is",round(math.sqrt(var[0][0])*100,4),"%")
print("Corresponding Portfolio :","w1 =",round(w[0][0],4),"w2 =",round(w[0][1],4),"w3 =",round(w[0][2],4))

point1 = (0,0.1)
point2 = (math.sqrt(var[0][0]),mu[0][0])

x_values = [point1[0], point2[0],0.8]

y_values = [point1[1], point2[1],0.1+0.8*(point2[1]-0.1)/point2[0]]


plt.plot(x_values, y_values,label="CML")
plt.plot(SD2_arr, xx2,c='r',label = "Markowitz Efficient Frontier")
plt.plot(SD1_arr, xx1,c='r',label = "Minimum Variance Curve",linestyle='dashed')
plt.scatter([math.sqrt(var[0][0])],[mu[0][0]],c='g',label="Market Portfolio")
plt.xlabel("Standard Variation (sigma)")
plt.ylabel("Return Value (mu)")
plt.yticks(np.linspace(0,0.8,9))
plt.xticks(np.linspace(0,0.8,9))
plt.title("Markowitz efficient Frontier and CML")
plt.grid(True)
plt.legend()
plt.show()

# part F

sig = 0.1
ratio_risk = sig/math.sqrt(var[0][0])
w_risk = (ratio_risk)*w

print("")
print("For a 10% risk free return, the required portfolio is:")
print("Corresponding Portfolio (Risky Asset):","w1 =",round(w_risk[0][0],4),"w2 =",round(w_risk[0][1],4),"w3 =",round(w_risk[0][2],4))
print("Corresponding Portfolio (RiskFree Asset):","w =",round((1-w_risk[0][0]-w_risk[0][1]-w_risk[0][2]),4))

sig = 0.25
ratio_risk = sig/math.sqrt(var[0][0])
w_risk = (ratio_risk)*w

print("")
print("For a 25% risk free return, the required portfolio is:")
print("Corresponding Portfolio (Risky Asset):","w1 =",round(w_risk[0][0],4),"w2 =",round(w_risk[0][1],4),"w3 =",round(w_risk[0][2],4))
print("Corresponding Portfolio (RiskFree Asset):","w =",round((1-w_risk[0][0]-w_risk[0][1]-w_risk[0][2]),4))


