inventory = {
    1: {
        "name": "Milk",
        "price": 3.99,
        "brand": "Regular"
    }
}

@app.get("/get-by-name")
def get_item(name: str):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
        return {"Data": "Not found"}

@app.get("/cloud1.com/cloud1.txt")
def download_crt():
    return FileResponse("files/cloud1.com/cloud1.txt")



@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="zscalertwo.net, zscalerone.net")):
    return inventory[item_id]
