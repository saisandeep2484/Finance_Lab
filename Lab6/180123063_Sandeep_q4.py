import numpy as np
import math
import numpy as np
import csv
import matplotlib.pyplot as plt

nse_name = ['HDFC','TCS','Kotak Mahindra','Bharti Airtel','Nestle','Housing Development','Maruti','Asian Paints','HCL','Coal India']
bse_name = ['SBI','Titan','Reliance','ICICI','Axis','L&T','Ultratech','ITC','ONGC','Infosys']

def func(string,tt,cent,vall,arr):
    c = 1
    c2 = 1
    if tt=="Months":
        c = 61
        c2 = 49
    elif tt=="Weeks":
        c = 261
        c2 = 206
    else:
        c = 1229
        c2 = 985
    
    S = np.zeros(shape=(10,c-1))
    if vall==0:
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
                
                
    for q in range(0,len(S)):
        stock=S[q][0:c2]
        n=len(stock)
        u=[]
        for i in range(1,n):
            if stock[i]==0:
                stock[i]=stock[i-1]
            ui=np.log(stock[i]/stock[i-1])
            u.append(ui)
            
        E=np.mean(u)

        variance=0

        for i in u:
            t=(i-E)*(i-E)
            variance+=t

        variance/=(len(u)-1)
        mu=E+variance/2
        sigma=math.sqrt(variance)
        if(tt=="Days"):
            print(mu,sigma,arr[q])
        S_0=S[q][c2]
        lamb_arr=[.05]
        m = c-c2-1
        for lamb in lamb_arr:
            N=np.random.poisson(lamb,m-1)
            Z=np.random.normal(0,1,m-1)
            X=[]
            X.append(math.log(S_0))
            for i in range(m-1):
                M=0
                if(N[i]!=0):
                    LY=np.random.normal(mu,sigma,N[i])
                    M=np.sum(LY)
                x=X[-1]+E+sigma*Z[i]+M
                X.append(x)
            
            
            SS=np.exp(X)
            y = np.array(SS) 
            
            if vall==1:
                plt.title("Simulated Path of Stock price of "+arr[q] + "("+tt+")")  
            else:
                plt.title("Simulated Path of Index price of "+cent+ "("+tt+")")  
            xx = "Time in "+tt
            plt.xlabel(xx)  
            plt.ylabel("Stock price")  
            plt.plot([*range(1,c-c2,1)], y, c ='g',label='Estimated')
            plt.plot([*range(1,c-c2,1)],S[q][c2:],c='r',label='Actual')
            plt.legend()
            plt.grid()  
            plt.show()
            
    
print("Monthly")
print("*****************************")
func('bsedata1_index_monthly.csv',"Months","bse",0,bse_name)
print("*****************************")
func('nsedata1_index_monthly.csv',"Months","nse",0,nse_name)
print("*****************************")
func('bsedata1_monthly.csv',"Months","bse",1,bse_name)
print("*****************************")
func('nsedata1_monthly.csv',"Months","nse",1,nse_name)

print("Weekly")
print("*****************************")
func('bsedata1_index_weekly.csv',"Weeks","bse",0,bse_name)
print("*****************************")
func('nsedata1_index_weekly.csv',"Weeks","nse",0,nse_name)
print("*****************************")
func('bsedata1_weekly.csv',"Weeks","bse",1,bse_name)
print("*****************************")
func('nsedata1_weekly.csv',"Weeks","nse",1,nse_name)

print("Daily")
print("*****************************")
func('bsedata1_index_daily.csv',"Days","bse",0,bse_name)
print("*****************************")
func('nsedata1_index_daily.csv',"Days","nse",0,nse_name)
print("*****************************")
func('bsedata1_daily.csv',"Days","bse",1,bse_name)
print("*****************************")
func('nsedata1_daily.csv',"Days","nse",1,nse_name)



            

