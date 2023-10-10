import nlopt
from numpy import *
from flask import Flask, jsonify, request
import os

port = 5003

def myfunc(x, grad):
    if grad.size > 0:
        grad[0] = 0.0
        grad[1] = 0.5 / sqrt(x[1])
    return sqrt(x[1]) 

def myconstraint(x, grad, a, b):
    if grad.size > 0:
        grad[0] = 3 * a * (a*x[0] + b)**2
        grad[1] = -1.0
    return (a*x[0] + b)**3 - x[1]

opt = nlopt.opt(nlopt.LD_MMA, 2)
opt.set_lower_bounds([-float('inf'), 0])
opt.set_min_objective(myfunc)
opt.add_inequality_constraint(lambda x,grad: myconstraint(x,grad,2,0), 1e-8)
opt.add_inequality_constraint(lambda x,grad: myconstraint(x,grad,-1,1), 1e-8)
opt.set_xtol_rel(1e-4)


# print("optimum at ", x[0], x[1])
# print("minimum value = ", minf)
# print("result code = ", opt.last_optimize_result())

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  nums = request.args

  x = opt.optimize([nums['num1'], nums['num2']])
  minf = opt.last_optimum_value()
  
  return jsonify({
    "optimum at ": [x[0], x[1]],
    "minumum value": minf,
    "result code": opt.last_optimize_result()
  })

app.run(port=port, host='0.0.0.0', debug=True)