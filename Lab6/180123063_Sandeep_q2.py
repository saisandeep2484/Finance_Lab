import numpy as np
import math
import numpy as np
import csv
import matplotlib.pyplot as plt

nse_name = ['HDFC','TCS','Kotak Mahindra','Bharti Airtel','Nestle','Housing Development','Maruti','Asian Paints','HCL','Coal India']
bse_name = ['SBI','Titan','Reliance','ICICI','Axis','L&T','Ultratech','ITC','ONGC','Infosys']

def func_index(string,t,cent):
    c = 1
    if t=="Months":
        c = 61
    elif t=="Weeks":
        c = 261
    else:
        c = 1229
    
    S = np.zeros(shape=(1,c-1))
    with open(string) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == c:
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
                
    for ar in S:
        for ele in ar:
            if ele == 0:
                ele = ar[0]
                
                
    for ar in S:

        ret = []
        for i in range(0,len(ar)):
            if i==0:
                continue
            val = (ar[i]-ar[i-1])/ar[i-1]
            ret.append(val)
        mu = np.mean(ret)
        sigma = np.std(ret)
        ret_norm = (ret - mu)/sigma
        _, bins, _ = plt.hist(ret_norm, density=True, bins=25)
        X = np.linspace(bins[0], bins[-1])
        plt.plot(X, np.exp(-X**2 / 2)/(np.sqrt(np.pi*2)))
        plt.xlabel("x")
        plt.ylabel("Denisty")
        plt.title("Density Plot of "+cent+" index returns " + "("+t+")" )
        plt.show()
        
            

    

def func(string,arr,t,cent):
    c = 1
    if t=="Months":
        c = 61
    elif t=="Weeks":
        c = 261
    else:
        c = 1229
    
    S = np.zeros(shape=(10,c-1))
    with open(string) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == c:
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
                
    cn = 0
    for ar in S:
        ret = []
        for i in range(0,len(ar)):
            if i==0:
                continue
            val = (ar[i]-ar[i-1])/ar[i-1]
            ret.append(val)
        mu = np.mean(ret)
        sigma = np.std(ret)
        ret_norm = (ret - mu)/sigma
        _, bins, _ = plt.hist(ret_norm, density=True, bins=25)
        X = np.linspace(bins[0], bins[-1])
        plt.plot(X, np.exp(-X**2 / 2)/(np.sqrt(np.pi*2)))
        plt.xlabel("x")
        plt.ylabel("Denisty")
        plt.title("Density Plot of " + arr[cn] + "(" + cent + "-"+t + ")")
        plt.show()
        cn+=1
    
        

print("Monthly")
print("*****************************")
func_index('bsedata1_index_monthly.csv',"Months","bse")
print("*****************************")
func_index('nsedata1_index_monthly.csv',"Months","nse")
print("*****************************")
func('bsedata1_monthly.csv',bse_name,"Months","bse")
print("*****************************")
func('nsedata1_monthly.csv',nse_name,"Months","nse")

print("Weekly")
print("*****************************")
func_index('bsedata1_index_weekly.csv',"Weeks","bse")
print("*****************************")
func_index('nsedata1_index_weekly.csv',"Weeks","nse")
print("*****************************")
func('bsedata1_weekly.csv',bse_name,"Weeks","bse")
print("*****************************")
func('nsedata1_weekly.csv',nse_name,"Weeks","nse")

print("Daily")
print("*****************************")
func_index('bsedata1_index_daily.csv',"Days","bse")
print("*****************************")
func_index('nsedata1_index_daily.csv',"Days","nse")
print("*****************************")
func('bsedata1_daily.csv',bse_name,"Days","bse")
print("*****************************")
func('nsedata1_daily.csv',nse_name,"Days","nse")


