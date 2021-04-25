import numpy as np
import math
import matplotlib.pyplot as plt

def yld(beta, mu, sigma, r, fin_t,model):
    if model=='vas':
        y = np.zeros(fin_t+1)
        y[0] = r
        a = beta
        b = mu*beta
        for t in range(1,fin_t+1):
            B = (1-math.exp(-a*t))/a
            A = (B-t)*((a*b-0.5*sigma**2)/(a**2))-(((a*B)*(a*B))/(4*a)) 
            p = math.exp(A-B*r) 
            y[t] = -1*math.log(p)/t
        return y
    else:
        y = np.zeros(fin_t+1) 
        y[0] = r
        a = beta
        b = mu*beta
        gamma = ((a*a)+2*math.sqrt((sigma*sigma)))
        for t in range(1,fin_t+1):
            D = ((gamma+a)*(math.exp(gamma*t)-1)+2*gamma)
            B = 2*(math.exp(gamma*t)-1)/D
            A = (2*gamma*math.exp((a+gamma)*(t/2))/D)**(2*a*b/(sigma*sigma))

            p = A*math.exp(-B*r)
            y[t] = -1*math.log(p)/t
        return y
    
def yield_vs_time_plot(model, parameters, time_units,name):
    plt.figure()
    for p in parameters:
        beta, mu, sigma, r = p
        if model == 'vas':
            y = yld(beta, mu, sigma, r, time_units,'vas')
        elif model == 'cir':
            y = yld(beta, mu, sigma, r, time_units,'cir')
        plt.plot(y, label=str(p))
    plt.title(name+' Model')
    plt.xlabel('Maturity Time')
    plt.ylabel('Yield Curve')
    plt.legend()
    plt.show()
    
def yield_vs_maturity_plot(model, parameters, time_units,name):
    for p in parameters:
        plt.figure()
        for r in np.arange(0.1,1.1,0.1):
            r = np.round_(r, 1)
            beta, mu, sigma, _ = p
            if model == 'vas':
                y = yld(beta, mu, sigma, r, time_units,'vas')
            elif model == 'cir':
                y = yld(beta, mu, sigma, r, time_units,'cir')
            plt.plot(y, label='r = '+str(r))
        if model == 'vas':
            plt.title(name + " Model with \u03B2, \u03BC, \u03C3 = "+str(p[:-1])+" (10 diffirent values of r)")
        else:
            plt.title(name + " Model with \u03B2, \u03BC, \u03C3 = "+str(p[:-1])+" r = 0.1 to 1")
        plt.xlabel('Maturity Time')
        plt.ylabel('Yield Curve')
        plt.legend()
        plt.show()
    
    
p1 = [0.02, 0.7, 0.02, 0.1]
p2 = [0.7, 0.1, 0.3, 0.2]
p3 = [0.06, 0.09, 0.5, 0.02]
yield_vs_time_plot('cir', [p1, p2, p3], 10,'CIR')
yield_vs_maturity_plot('cir', [p1], 600,'CIR')
# yield_vs_maturity_plot('cir', [p1, p2, p3], 25,'CIR')
    
    


        
