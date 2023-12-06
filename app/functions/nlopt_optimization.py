import nlopt
import numpy as np
import math
import benchmarking_fuctions as functions 

class NLoptOptimization:
    def __init__(self):
        self.__parameters__ = np.zeros(2)
        self.__algorithm__ = nlopt.LD_MMA
        self.__lb__ = 0
        self.__ub__ = 1
        self.__flag_lb = False
        self.__min_max = "MIN"
    
    # ESTATICO
    def inequality(self, x, grad=0, la=2, ua=0, lb=-1, ub=1, precision=1e-8):
        opt = nlopt.opt(self.getAlgorithmType(), self.getDimensionProblem())
        opt.add_inequality_constraint(lambda x,grad: self.myconstraint(x,grad,la,ua), precision)
        opt.add_inequality_constraint(lambda x,grad: self.myconstraint(x,grad,lb,ub), precision)
        self.__x__ = x
        self.__grad__ = grad

    # ESTATICO
    def my_func(self, x): #main function
        functions[self.getAlgorithmType](x)
        return functions
    
    # ESTATICO
    def my_constraint(self, x,grad,):
        self.__parameters__ = x
        if functions[1] <= 0:
            return functions
    
    def getDimensionProblem(self):
        return len(self.__x__)
    def setX(self,x):
        self.__x__ = x
    def getX(self):
        return self.__x__
    def setGrad(self,grad):
        self.__grad__ = grad
    def getGrad(self):
        return self.__grad__
    def setLB(self, lb):
        self.__flag_lb = True
        self.__lb__ = lb
    def getLB(self):
        return self.__lb__
    def setUB(self, ub):
        self.__ub__ = ub
    def getUB(self):
        return self.__ub__
    def setXTol(self, xtol):
        self.__xtol__ = xtol
    def getXTol(self):
        return self.__xtol__
    def setNTests(self, ntests):
        self.__ntests__ = ntests
    def getNTests(self):
        return self.__ntests__
    def setFunctionOptimization(self, funcx):
        self.__function_optimization__ = funcx
    def getFunctionOptimization(self):
        return self.__function_optimization__
    def setAlgorithmType(self, funcx):
        self.__algorithm__ = funcx
    def getAlgorithmType(self):
        return self.__algorithm__
    
    # ESTATICO
    def executeOptimization(self):
        #functions[p_type](x) #função de execução das funções
        opt = nlopt.opt(self.getAlgorithmType(),self.getDimensionProblem()) #NLopt class
        if self.__flag_lb == True:
            opt.set_lower_bounds(self.getLB()) #setando os pontos mínimos
        #opt.set_upper_bounds(self.getUB()) #setando os pontos máximos
        if self.__min_max == "MIN":
            opt.set_min_objective(self.my_func) #??
        elif self.__min_max == "MAX":
            opt.set_max_objective(self.my_func)
        opt.set_xtol_rel(self.getXTol()) #get interval = pegando o intervalo 
        opt.set_maxeval(self.getNTests()) #how many times will the code run = quantas vezes o codigo vai rodar]
        print(self.getXTol())
        posicao = opt.optimize(self.getX(), None)
        print("result code =" + opt.last_optimize_result())