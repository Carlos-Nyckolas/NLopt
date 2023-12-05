import sys
import nlopt
import numpy as np
import random


def execute(p_type, x):
    pass

def rand_option(limits):
    limits[0] = 3
    limits[1] = lb
    limits[2] = ub
    limits[3] = 0
    limits[4] = 1
    limits[5] = 10
    limits[6] = 1
    return limits

def myvfunc(x, grad, my_func_data):
    global cont, fit, outfile, outfile_fulldata
    cont += 1
    fit = execute(p_type, x)
    
    if cont < 3000:
        outfile.write(f"{cont} {fit}\n")
        outfile_fulldata.write(f"{cont} {fit}")
        for contp in range(dimensions):
            outfile_fulldata.write(f" {x[contp]}\n")

    return fit

def myvconstraint(x, grad, data):
    global cont
    a, b = data[0], data[1]
    if grad:
        grad[0] = 3 * a * (a * x[0] + b) * (a * x[0] + b)
        grad[1] = -1.0
    return ((a * x[0] + b) * (a * x[0] + b) * (a * x[0] + b) - x[1])

cont = 0
lb = sys.argv[1] #Lower bounder = valor mínimo
ub = sys.argv[2] #Up bounder = valor máximo
p_type = sys.argv[3] #problem type = tipo de problema ex:Ackeley,Michal,sphere
xtol = sys.argv[4] #interval = intervalo ex:1e-4
dimensions = sys.argv[5] #number of dimensios = número de dimenções
num_test = sys.argv[6] #number of tests = número de quantos teste serão feitos
fit = 0.0
outfile = None
outfile_fulldata = None

for i in range(p_type):
    limits[1] = lb[i] = lb
    limits[2] = ub[i] = ub
    x[i] = rand_option(limits)

    optx.set_lower_bounds(lb)
    optx.set_upper_bounds(ub)
    optx.set_min_objective(myvfunc)
    optx.set_xtol_rel(1e-4)
    optx.set_maxeval(3000)

    result = optx.optimize(x)
    
    for i in range(cont, 3000):
        outfile.write(f"{i} {fit}\n")
        outfile_fulldata.write(f"{i} {fit}")

    outfile.close()
    outfile_fulldata.close()
    cont = 0