from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse

print("Server restarted!")

app = FastAPI()

@app.get("/")
def welcome_user(request : Request, name : str = "Guest", adult : bool = False):
    accept_type = request.headers.get("Accept")
    if accept_type != "text/plain":
        return JSONResponse({"message":"Unsupported media type"},402)
    if name != "Guest":
        if adult :
            return JSONResponse({"message" : f"Hello {name}! You are a grownup!"},200)
        return JSONResponse({"message" : f"Hello {name}! You are not a grownup!"},200)
    if adult:
        return JSONResponse({"message" : f"Hello {name} ! You are a grownup!"},200)
    return JSONResponse({"message" : "Hello there !"},200)

class UserInfo(BaseModel):
    name : str
    adult : bool

@app.post("/greet")
def post_name(user_info : UserInfo):
    if user_info.adult:
        return JSONResponse({"message" : f"Hello {user_info.name}! You are a grownup!"},200)
    return JSONResponse({"message" : f"Hello {user_info.name}! You are not a grownup!"},200)



@app.post("/top_secret")
def verify_user(request : Request):
    code = request.headers.get("Authorization")
    if code == "my_secret_key":
        return JSONResponse({"message" : "Access granted"},200)
    return JSONResponse({"message" : "Access denied"},403)