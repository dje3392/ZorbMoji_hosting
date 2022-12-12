from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import json
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")

async def root():

    return {"message": "ZORBMOJI TAKEOVER"}


@app.get("/json/{file_name}")
def serve_json_file(file_name: str):
    with open(f"static/{file_name}.json", "r") as f:
        return JSONResponse(content=json.load(f))