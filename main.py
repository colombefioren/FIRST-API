from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse

app = FastAPI()

@app.get("/")
def welcome_user(request : Request):
    accept_type = request.headers.get("Accept")
    if accept_type != "text/plain":
        return JSONResponse({"message":"Unsupported media type"},402)
    return JSONResponse({"message" : "Hello there !"},200)

class UserInfo(BaseModel):
    name : str
    adult : bool

@app.post("/greet")
def post_name(user_info : UserInfo):
    if user_info.adult:
        return JSONResponse({"message" : f"Hello {user_info.name}! You are a grownup!"},200)
    return JSONResponse({"message" : f"Hello {user_info.name}! You are not a grownup!"},200)