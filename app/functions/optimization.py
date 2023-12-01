import sys
import nlopt
from numpy import *
from benchmarking_fuctions import execute

def my_func(): #main function
    
    return

lb = sys.argv[1] #Lower bounder = valor mínimo
ub = sys.argv[2] #Up bounder = valor máximo
p_type = sys.argv[3] #problem type = tipo de problema ex:Ackeley,Michal,sphere
xtol = sys.argv[4] #interval = intervalo ex:1e-4
dimensions = sys.argv[5] #number of dimensios = número de dimenções
num_test = sys.argv[6] #number of tests = número de quantos teste serão feitos

execute(p_type,x) #função de execução das funções

opt = nlopt.opt(nlopt.LD_MMA,dimensions) #NLopt class
opt.set_lower_bounds(lb) #setando os pontos mínimos
opt.set_upper_bounds(ub) #setando os pontos máximos
opt.set_min_objective(my_func,None) #??
opt.get_xtol_rel(xtol) #get interval = pegando o intervalo 
opt.set_maxeval(num_test) #how many times will the code run = quantas vezes o codigo vai rodar