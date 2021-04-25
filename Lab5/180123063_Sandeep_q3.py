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

nse_name = ['HDFC','TCS','Kotak Mahindra','Bharti Airtel','Nestle','Housing Development','Maruti','Asian Paints','HCL','Coal India']
bse_name = ['SBI','Titan','Reliance','ICICI','Axis','L&T','Ultratech','ITC','ONGC','Infosys']
non_bse_name = ['Suzlon','Godfrey Phillips','Engineers India','Maharashtra Scooters','KEI Industries','Sun Pharma','Travancore Ferilizers','Responsive Industries','Gujrat Raffia','VST Industries']
non_nse_name = ['Suzlon','Godfrey Phillips','Engineers India','Maharashtra Scooters','KEI Industries','Sun Pharma','Travancore Ferilizers','Responsive Industries','Heidelcore Cement','VST Industries']


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
    
    if string=="nsedata1.csv":
        for i in range(0,10):
            req_val = sum((a - nse_mean) * (b - m[0][i]) for (a,b) in zip(nse_ret,S[i])) / len(nse_ret)
            req_val = (req_val)/vall2
            beta_nse.append(req_val)
    elif string=="bsedata1.csv":
        for i in range(0,10):
            req_val = sum((a - bse_mean) * (b - m[0][i]) for (a,b) in zip(bse_ret,S[i])) / len(bse_ret)
            req_val = (req_val)/vall2
            beta_bse.append(req_val)
    elif string=="bse_non_index_data1.csv":
        for i in range(0,10):
            req_val = sum((a - bse_mean) * (b - m[0][i]) for (a,b) in zip(bse_ret,S[i])) / len(bse_ret)
            req_val = (req_val)/vall2
            beta_non_bse.append(req_val)
    elif string=="nse_non_index_data1.csv":
        for i in range(0,10):
            req_val = sum((a - nse_mean) * (b - m[0][i]) for (a,b) in zip(nse_ret,S[i])) / len(nse_ret)
            req_val = (req_val)/vall2
            beta_non_nse.append(req_val)


func("bsedata1.csv","10 Stocks of BSE SENSEX",bse_mean,bse_var)

func("nsedata1.csv","10 Stocks of NSE NIFTY",nse_mean,nse_var)

func("nse_non_index_data1.csv","10 Stocks not in BSE SENSEX",bse_mean,bse_var)

func("bse_non_index_data1.csv","10 Stocks not in NSE NIFTY",nse_mean,nse_var)


actual_bse_beta = []
actual_nse_beta = []
actual_non_nse_beta = []
actual_non_bse_beta = []

with open('bse_beta.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 2:
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
                    actual_bse_beta.append((val))
                    cn=cn+1

                line_count += 1
                
                
with open('nse_beta.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 2:
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
                    actual_nse_beta.append((val))
                    cn=cn+1

                line_count += 1

with open('non_bse_beta.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 2:
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
                    actual_non_bse_beta.append((val))
                    cn=cn+1

                line_count += 1
                
                
with open('non_nse_beta.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 2:
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
                    actual_non_nse_beta.append((val))
                    cn=cn+1

                line_count += 1


print("")
print("Considering 10 Stocks in Sensex")
for i in range(0,len(bse_name)):
    beta_bse[i] = round(beta_bse[i],3)
    print("Calculated and Actual Beta Values for",bse_name[i],":","|",beta_bse[i],"|",actual_bse_beta[i],"|")

print("")
print("Considering 10 Stocks in Nifty")
for i in range(0,len(nse_name)):
    beta_nse[i] = round(beta_nse[i],3)
    print("Calculated and Actual Beta Values for",nse_name[i],":","|",beta_nse[i],"|",actual_nse_beta[i],"|")
    
print("")
print("Considering 10 Stocks not in Sensex")
for i in range(0,len(non_bse_name)):
    beta_non_bse[i] = round(beta_non_bse[i],3)
    print("Calculated and Actual Beta Values for",non_bse_name[i],":","|",beta_non_bse[i],"|",actual_non_bse_beta[i],"|")



print("")
print("Considering 10 Stocks not in Nifty")
for i in range(0,len(non_nse_name)):
    beta_non_nse[i] = round(beta_non_nse[i],3)
    print("Calculated and Actual Beta Values for",non_nse_name[i],":","|",beta_non_nse[i],"|",actual_non_nse_beta[i],"|")

    