from fastapi import FastAPI
from .models.benchmarking_model import Benchmarking
from .functions.benchmarking_fuctions import execute

app = FastAPI()

@app.get("/")
def index(benchmarking_data: Benchmarking):
    return execute(benchmarking_data.functionx, benchmarking_data.x)
