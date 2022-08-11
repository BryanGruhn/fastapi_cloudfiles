from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/csv")
def images():
    out = []
    for filename in os.listdir("static/csv"):
        out.append({
            "name": filename.split(".")[0],
            "path": "/static/csv/" + filename
        })
    return out


@app.get("/xml")
def xml():
    out = []
    for filename in os.listdir("static/xml"):
        out.append({
            "name": filename.split(".")[0],
            "path": "/static/xml/" + filename
        })
    return out
