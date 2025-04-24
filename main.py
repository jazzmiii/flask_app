from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return JSONResponse(content={"message": "Hello from Render!"})

@app.get("/hello/{name}")
def say_hello(name: str):
    return JSONResponse(content={"message": f"Hello, {name}!"})
