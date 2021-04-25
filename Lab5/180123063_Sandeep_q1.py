import math
import numpy as np
import csv
import matplotlib.pyplot as plt

    
bse_mean = 0
bse_var = 0

nse_mean = 0
nse_var = 0

bse_arr = []
nse_arr = []   

with open('bse_index.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 61:
                break
            if line_count == 0:
                line_count += 1
            else:
                bse_arr.append(float(row[1]))
                line_count += 1
                
bse_ret = []
for i in range(1,len(bse_arr)):
    bse_ret.append(12*(bse_arr[i]-bse_arr[i-1])/bse_arr[i-1])
    
    
bse_mean = np.mean(bse_ret)
bse_var = np.var(bse_ret)

with open('nse_index.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 61:
                break
            if line_count == 0:
                line_count += 1
            else:
                nse_arr.append(float(row[1]))
                line_count += 1
                
nse_ret = []
for i in range(1,len(nse_arr)):
    nse_ret.append(12*(nse_arr[i]-nse_arr[i-1])/nse_arr[i-1])
    

nse_mean = np.mean(nse_ret)
nse_var = np.var(nse_ret)
   
print("Mean Return for NIFTY is:",nse_mean)
print("Standard Variation (Risk) for NIFTY is:",math.sqrt(nse_var)*100,'%')

print("")
print("Mean Return for SENSEX is:",bse_mean)
print("Standard Variation (Risk) for SENSEX is:",math.sqrt(nse_var)*100,'%')



beta_bse = []
beta_nse = []


beta_non_bse = []
beta_non_nse = []


def func(string,string2,vall,vall2):
    S = np.zeros(shape=(10,60))

    with open(string) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 61:
                break
            if line_count == 0:
                line_count += 1
            else:
                cn = -1
                for val in row:
                    if cn==-1:
                        cn+=1
                        continue
                    if val=='':
                        continue
                    S[cn][line_count-1] = float(val)
                    cn=cn+1

                line_count += 1
                
    m = np.array([[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]])
    u = np.array([[1,1,1,1,1,1,1,1,1,1]])
    C = np.zeros(shape=(10,10))

    for i in range(0,10):
        for j in range(0,60):
            if j+1<60:
                S[i][j] = (S[i][j+1]-S[i][j])/(S[i][j])
            else:
                S[i][j] = S[i][j-1]
                
            S[i][j] *= 12



    cn = 0
    for arr in S:
        m[0][cn] = arr.mean()
        cn+=1

    for i in range(0,10):
        for j in range(0,10):
            val = 0
            for k in range(0,60):
                val+= (S[i][k]-m[0][i])*(S[j][k]-m[0][j])
            C[i][j] = val/60



    C_inv = np.linalg.inv(C)
    mu_arr = np.linspace(-0.30,2.20,401)
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

    for mu in mu_arr:
        lamda = 2*M_inv.dot((np.array([[mu,1]])).T)
        w = (lamda[0][0]* (m.dot(C_inv)) + (lamda[1][0]*(u.dot(C_inv))))/2
        var = w.dot(C.dot(w.T))
        if mu<Global_min_mu[0][0]:
            xx1.append(mu)
            SD1_arr.append(math.sqrt(var[0][0]))
        else :
            xx2.append(mu)
            SD2_arr.append(math.sqrt(var[0][0]))

    # Part A
    Global_min_mu = M12/M22
    lamda = 2*M_inv.dot((np.array([[Global_min_mu[0][0],1]])).T)
    lam1 = lamda[0][0]
    lam2 = lamda[1][0]
    w = lam1*(m.dot(C_inv)) + lam2*(u.dot(C_inv))
    w = w/2
    Global_min_var = w.dot(C.dot(w.T))

    
    plt.scatter(math.sqrt(Global_min_var[0][0]),Global_min_mu[0][0],label="Global Min Variance Portfolio")
#     plt.scatter(math.sqrt(val2),val,label="Index Portfolio")
    plt.plot(SD2_arr, xx2,c='r',label = "Markowitz Efficient Frontier")
    plt.plot(SD1_arr, xx1,c='r',label = "Minimum Variance Curve",linestyle='dashed')
    plt.xlabel("Standard Variation (sigma)")
    plt.ylabel("Return Value (mu)")
    plt.title("Efficient Frontier for "+string2)
    plt.grid(True)
    plt.legend()
    plt.show()

    # Part B
    rf = 0.05

    num = (m-rf*u).dot(C_inv)
    denom = (m-rf*u).dot(C_inv.dot(u.T))
    w = num/denom
    mu = w.dot(m.T)
    var = w.dot(C.dot(w.T))

    print("")
    print("The risk-free rate = 0.05 = 5% (Yearly)")
    print("The return on market portfolio is",round((mu[0][0]),4))
    print("The risk on market portfolio is",round(math.sqrt(var[0][0]),4),"(",round(100*math.sqrt(var[0][0]),4),"% )")


    # Part C
    
    point1 = (0,rf)
    point2 = (math.sqrt(var[0][0]),mu[0][0])

    x_values = [point1[0],point2[0],4]

    y_values = [point1[1], point2[1],rf+4*(point2[1]-rf)/point2[0]]


    plt.plot(x_values, y_values,label="CML")
    plt.scatter([math.sqrt(vall2)],[vall],c='b',label="Market Portfolio-Index")
    plt.plot(SD2_arr, xx2,c='r',label = "Markowitz Efficient Frontier")
    plt.plot(SD1_arr, xx1,c='r',label = "Minimum Variance Curve",linestyle='dashed')
    plt.scatter([math.sqrt(var[0][0])],[mu[0][0]],c='g',label="Market Portfolio-CML")
    plt.xlabel("Standard Variation (sigma)")
    plt.ylabel("Return Value (mu)")
#     plt.yticks(np.linspace(-0.10,0.20,11))
    plt.title("Markowitz efficient Frontier and CML for "+string2)
    plt.grid(True)
    plt.legend()
    plt.show()   
    
    # Part D
    if string=="nse_non_index_data1.csv" or string =="bse_non_index_data1.csv":
        return
        
    beta = np.linspace(-2,2,401)
    mu_v = rf + (vall - rf)*beta;

    plt.plot(beta, mu_v)

    plt.xlabel("Beta Coefficient (beta)")
    plt.ylabel("Return Value (mu)")
    plt.title("Security Market Line for BSE")
    if string=="nsedata1.csv":
        plt.title("Security Market Line for NSE")
    
    plt.grid(True)
    plt.show()
    
    

print("")
print("Considering 10 Stocks of BSE SENSEX")
func("bsedata1.csv","10 Stocks of BSE SENSEX",bse_mean,bse_var)

print("")
print("Considering 10 Stocks of NSE NIFTY")
func("nsedata1.csv","10 Stocks of NSE NIFTY",nse_mean,nse_var)

print("")
print("Considering 10 Stocks not included in SENSEX, but sill listed in BSE")
func("nse_non_index_data1.csv","10 Stocks not in SENSEX",bse_mean,bse_var)

print("")
print("Considering 10 Stocks not included in NIFTY, but still listed in NSE")
func("bse_non_index_data1.csv","10 Stocks not in NIFTY",nse_mean,nse_var)

