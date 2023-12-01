"""
    execute(function, x)
    - function: parameter associate to benchmarking funcion from https://www.sfu.ca/~ssurjano/ 
    - x: data vector with n dimensions (elements) whose range values must be defined according 
         to selected benchmarking function 
    Returns:
        r: is number returned from the optimization benchmarking selected, whose value in 
        Genetic Algorithms is called fitness, in Evolutionary Strategy affinity, Cuckoo nest distance and so on
"""
from math import pi
import numpy as np
#https://www.sfu.ca/~ssurjano/ackley.html
# xi ∈ [-32.768, 32.768], for all i = 1, …, d, 
def Ackley(x):
    n = len(x)
    sum1 = 0
    sum2 = 0
    for i in range(n):
        sum1 = sum1 + np.sqrt(x[i])
        sum2 = sum2 + np.cos(2 * pi * x[i])
    resultado = -20.0 * np.exp(-0.2 * np.sqrt(1/sum1))-np.exp(1/sum2) + 20 + np.exp(1)
    return resultado
#https://www.sfu.ca/~ssurjano/griewank.html
# xi ∈ [-600, 600] 
def Griewank(x):
    n = len(x)
    sumx = 0
    prodx= 1
    for ii in range(n):
        xi = x[ii]
        sumx = sumx + (xi*xi)/4000
        prodx = prodx * np.cos(xi/np.sqrt(ii+1))
    return sumx - prodx + 1
#https://www.sfu.ca/~ssurjano/levy.html
# xi ∈ [-10, 10],
def Levy(x):
    n = len(x)
    w = np.zeros(n)
    for ii in range(n):
        w[ii] = 1 + (x[ii]-1)/4
    term1 = np.power(np.sin(pi*w[0]),2)
    term3 = np.power(w[n-1]-1,2) * np.power(1+(np.sin(2*pi*w[n-1])),2)
    sumx = 0
    for ii  in range(n-1):
        wi = w[ii]
        new = np.power(wi-1,2) * np.power(1+10*(np.sin(pi*wi+1)),2)
        sumx = sumx + new
        return term1 + sumx + term3
#https://www.sfu.ca/~ssurjano/rastr.html
# xi ∈ [-5.12, 5.12], 
def Rastrigin(x):
    n = len(x)
    sumx = 0
    for ii in range(n):
        xi = x[ii]
        sumx = sumx + (xi*xi - 10*np.cos(2*pi*xi))
    return 10*n + sumx
#https://www.sfu.ca/~ssurjano/schwef.html
# xi ∈ [-500, 500],
def Schwefel(x):
    n = len(x)
    sumx = 0
    for ii in range(n):
        xi = x[ii]
        sumx = sumx + xi*np.sin(np.sqrt(np.abs(xi)))
    return 418.9829*n - sumx
#https://www.sfu.ca/~ssurjano/perm0db.html
# xi ∈ [-d, d], being d the vector x dimension
def Perm0db(x):
    b = 10
    n = len(x)
    outer = 0
    for ii in range(n):
        inner = 0
        for jj in  range(n):
            xj = x[jj]
        inner = inner + (jj+b)*(np.power(xj,ii)-np.power(1/jj,ii))
    outer = outer + np.power(inner,2)
    return outer
# https://www.sfu.ca/~ssurjano/spheref.html
# xi ∈ [-5.12, 5.12]
def Sphere(x):
    n = len(x)
    sumx = 0
    for i in range(n):
        sumx = sumx + np.power(x[i],2)
    return  sumx
#https://www.sfu.ca/~ssurjano/zakharov.html
# xi ∈ [-5, 10],
def Zakharov(x):
    n = len(x)
    sum1 = 0
    sum2 = 0
    for i in range(n):
        xi = x[i]
        sum1 = sum1 + np.power(xi,2)
        sum2 = sum2 + 0.5 * i * xi
    return sum1 + np.power(sum2,2) + np.power(sum2,4)
# https://www.sfu.ca/~ssurjano/dixonpr.html
# xi ∈ [-10, 10]
def DixonPr(x):
    x1 = x[0]
    n = len(x)
    term1 = np.power(x1-1,2)
    sumx = 0
    for i in range(1,n):
        xi = x[i]
        xold = x[i-1]
        new = i * np.power(2* xi * xi - xold,2)
        sumx = sumx + new
    return term1 + sumx
# https://www.sfu.ca/~ssurjano/Code/michalm.html
# xi ∈ [0, π]
def Michal(x):
    m = 10
    n = len(x)
    sumx = 0
    for i in range(n):
        xi = x[i]
        newx = np.sin(xi) * np.power(np.sin(i*xi*xi/pi),2*m)
        sumx = sumx + newx
    return -sumx
def execute (functionx, x):
    if functionx==1:
        r = Ackley(x)
    elif functionx==2:
        r = Griewank(x)
    elif functionx==3:
        r = Levy(x)
    elif functionx==4:
        r = Rastrigin(x)
    elif functionx==5:
        r = Schwefel(x)
    elif functionx==6:
        r = Perm0db(x)
    elif functionx==7:
        r = Sphere(x)
    elif functionx==8:
        r = Zakharov(x)
    elif functionx==9:
        r = DixonPr(x)
    elif functionx==10:
        r = Michal(x)
    else:
        print("erro")
    return r
# example - vectorx is a 3rd order vector with values from 0 to 1
# vectorx = np.random.uniform(0,1,3)
# for algorithm in range(1,11):
#     print(execute(algorithm, vectorx))