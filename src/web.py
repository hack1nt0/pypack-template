from typing import Union
from fastapi import FastAPI
import hashlib

app = FastAPI()

x = 1

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/wx")
def connect_wx(signature, timestamp, nonce, echostr):
    try:
        token = "caonima666" #请按照公众平台官网\基本配置中信息填写
        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()
        print("handle/GET func: hashcode, signature: ", hashcode, signature)
        if hashcode == signature:
            return echostr
        else:
            return ""
    except Exception:
        return None