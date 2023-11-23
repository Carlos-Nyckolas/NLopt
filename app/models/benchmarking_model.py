from pydantic import BaseModel

class Benchmarking(BaseModel):
    functionx: int 
    x: list[float]