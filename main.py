import uvicorn
from fastapi import FastAPI, Path
from fastapi.responses import FileResponse

app = FastAPI()


inventory = {
    1: {
        "name": "cloud1.com",
        "txt": "files/cloud1.com/cloud1.txt",
        "csv": "files/cloud1.com/cloud1.csv"
    },
    2: {
        "name": "cloud2.com",
        "txt": "files/cloud2.com/cloud2.txt",
        "csv": "files/cloud2.com/cloud2.csv"
    },
    3: {
        "name": "cloud3.com",
        "txt": "files/cloud3.com/cloud3.txt",
        "csv": "files/cloud3.com/cloud3.csv"
    }
}


@app.get("/cloud-txt")
def get_item(name: str):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return FileResponse(inventory[item_id]["txt"])
        return {"Data": "Cloud Not Found!"}


@app.get("/cloud-csv")
def get_item(name: str):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return FileResponse(inventory[item_id]["csv"])
        return {"Data": "Cloud Not Found!"}
