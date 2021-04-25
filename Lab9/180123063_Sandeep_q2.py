import pandas as pd
import math
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def func_call(data,K,T,name):
    print("3d Graphs")
    fig = plt.figure()
    ax = plt.axes(projection="3d")

    ax.scatter(data['Strike Price'], data['Maturity'], data['Call Price'])
    ax.set_xlabel('Strike Price (K)')
    ax.set_ylabel('T (Maturity Time) in Days')
    ax.set_zlabel('Call Option Price')
    ax.set_title(name + ' Call Option Price')
    plt.show()

    print("2d Graphs")
    for i in range(0,len(data['Strike Price'])):
        if data['Strike Price'][i]==K:
            plt.scatter(data['Maturity'][i],data['Call Price'][i],c='b',s=15,alpha=0.5)

    plt.xlabel('T (Maturity Time in Days)')
    plt.ylabel('Call Option Price')
    plt.title('Call Option Price vs Maturity' + '--' + name)
    plt.show()

    for i in range(0,len(data['Maturity'])):
        if data['Maturity'][i]==T:
            plt.scatter(data['Strike Price'][i],data['Call Price'][i],c='b',s=15,alpha=0.5)

    plt.xlabel('Strike Price (K)')
    plt.ylabel('Call Option Price')
    plt.title('Call Option Price vs Strike Price' + '--' + name)
    plt.show()

def func_put(data,K,T,name):
    print("3d Graphs")
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    ax.scatter(data['Strike Price'], data['Maturity'], data['Put Price'])
    ax.set_xlabel('Strike Price (K)')
    ax.set_ylabel('T (Maturity Time in Days)')
    ax.set_zlabel('Put Option Price')
    ax.set_title(name + ' Put Option Price')
    ax.view_init(30,210)
    plt.show()
    
    for i in range(0,len(data['Strike Price'])):
        if data['Strike Price'][i]==K:
            plt.scatter(data['Maturity'][i],data['Put Price'][i],c='b',s=15,alpha=0.5)

    plt.xlabel('T (Maturity Time in Days)')
    plt.ylabel('Put Option Price')
    plt.title('Put Option Price vs Maturity' + '--' + name)
    plt.show()
    
    print("2d Graphs")
    
    for i in range(0,len(data['Maturity'])):
        if data['Maturity'][i]==T:
            plt.scatter(data['Strike Price'][i],data['Put Price'][i],c='b',s=15,alpha=0.5)

    plt.xlabel('Strike Price (K)')
    plt.ylabel('Put Option Price')
    plt.title('Put Option Price vs Strike Price' + '--' + name)
    plt.show()
    
    

data = pd.read_excel('stockoptiondata/NIFTYoptiondata.xlsx')
data['Date'] = pd.to_datetime(data['Date'])
data['Expiry'] = pd.to_datetime(data['Expiry'])
data['Maturity'] = data['Expiry']-data['Date']
data['Maturity'] = pd.to_numeric(data['Maturity'])
data['Maturity'] = data['Maturity']/(24*3600*(10**9)) #convert to days

# print(data['Maturity'])

print("FOR NIFTY OPTION DATA:")
func_call(data,11600,89,'NIFTY')
func_put(data,11600,89,'NIFTY')

stocks = ['Coalindia', 'Grasim', 'NTPC']



for stock in stocks:
    stock_data = pd.read_csv('stockoptiondata/'+stock+'_CE.csv')
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])
    stock_data['Expiry'] = pd.to_datetime(stock_data['Expiry'])
    stock_data['Maturity'] = stock_data['Expiry']-stock_data['Date']
    stock_data['Maturity'] = pd.to_numeric(stock_data['Maturity'])
    stock_data['Maturity'] = stock_data['Maturity']/(24*3600*(10**9)) #convert to days
    stock_data['Strike Price'] = stock_data['Strike Price']
    stock_data['Call Price'] = stock_data['Close']
    func_call(stock_data,stock_data['Strike Price'][0],stock_data['Maturity'][0],stock)
    stock_data = pd.read_csv('stockoptiondata/'+stock+'_PE.csv')
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])
    stock_data['Expiry'] = pd.to_datetime(stock_data['Expiry'])
    stock_data['Maturity'] = stock_data['Expiry']-stock_data['Date']
    stock_data['Maturity'] = pd.to_numeric(stock_data['Maturity'])
    stock_data['Maturity'] = stock_data['Maturity']/(24*3600*(10**9)) #convert to days
    stock_data['Strike Price'] = stock_data['Strike Price']
    stock_data['Put Price'] = stock_data['Close']
    func_put(stock_data,stock_data['Strike Price'][0],stock_data['Maturity'][0],stock)
    







