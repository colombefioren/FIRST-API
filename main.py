from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI()

@app.get("/")
def welcome_user():
    return JSONResponse({"message" : "Hello there !"},200)