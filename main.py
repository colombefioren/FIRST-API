from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse

app = FastAPI()

@app.get("/")
def welcome_user(request : Request):
    accept_type = request.headers.get("Accept")
    if accept_type != "text/plain":
        return JSONResponse({"message":"Unsupported media type"},402)
    return JSONResponse({"message" : "Hello there !"},200)

