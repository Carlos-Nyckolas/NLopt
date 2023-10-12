from fastapi import FastAPI
from .nlopt_calc import *
from .nums import Nums

app = FastAPI()

@app.get("/")
def index(nums: Nums):
    return calc(nums.num1, nums.num2)
