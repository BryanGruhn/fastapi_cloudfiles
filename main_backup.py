import uvicorn
from fastapi import FastAPI, Path
from fastapi.responses import FileResponse

app = FastAPI()


inventory = {
    1: {
        "name": "cloud1.com",
        "xml": "files/cloud1.com/cloud1.xml",
        "csv": "files/cloud1.com/cloud1.csv"
    },
    2: {
        "name": "cloud2.com",
        "xml": "files/cloud2.com/cloud2.xml",
        "csv": "files/cloud2.com/cloud2.csv"
    },
    3: {
        "name": "cloud3.com",
        "xml": "files/cloud3.com/cloud3.xml",
        "csv": "files/cloud3.com/cloud3.csv"
    }
}


@app.get("/cloud-xml")
def get_item(name: str):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return FileResponse(inventory[item_id]["xml"])
        return {"Data": "Cloud Not Found!"}


@app.get("/cloud-csv")
def get_item(name: str):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return FileResponse(inventory[item_id]["csv"])
        return {"Data": "Cloud Not Found!"}