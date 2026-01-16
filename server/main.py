from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/ping")
async def ping():
    return "pong"



class ScanRequest(BaseModel):
    url: str
    # visibility: str = ""
    # customagent: str = ""
    # referer = str = ""
    # tags: list  # limited to 10
    # overrideSafety # unimplemented
    # country # unimplmented

@app.get("/api/v1/scan/")
async def scan_url(
    data: ScanRequest):
   


    return "oki?"




