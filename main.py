from typing import Union

from fastapi import FastAPI
from app.config_reader import settings
import hashlib

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/wx")
def wx(signature: str, timestamp:str, nonce:str, echostr:str):
    token = "bingchengtoken"
    list = [token, timestamp, nonce]
    list.sort()
    sha1 = hashlib.sha1()
    map(sha1.update, list)
    hashcode = sha1.hexdigest()
    print("handle/GET func: hashcode, signature: ", hashcode, signature)
    return echostr

@app.get("/info")
def info():
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user,
    }