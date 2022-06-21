# fastAPI

# Tradionally when you write your API, you have to follow certain rules that your API accepts. However, you will be able to define types of all of the data your API expect. In fastAPI all of this automatically done for you. If smn sends you wrong type of info to your API end point, it will automatically return them an error message saying hey you should have used this like this etc.
# fastAPI does all of the data validations for you.
# Autodocuments for your entire API
# We are gonna get a really good auto completion.

# GET    --> This endpoint is going to be returning information
# POST   --> U are gonne be sending information to the post endpoint or this endpoint will be creating smg new.
# PUT    --> To update smg already existing in the database. Modify info
# DELETE --> Delete smg, get rid of info.

from fastapi import FastAPI, Path,  Query, HTTPException, status
from typing import Optional   # Recommended from fastAPI docs you implement that
from pydantic import BaseModel


class Item(BaseModel):  # To create a new item!!
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):  # To create a new item!!
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None


app = FastAPI()

@app.get("/")                                # Now we can create an endpoint
def home():
    return {"Data":"Test"}

@app.get("/about")
def about():
    return {"Data": "About"}

inventory = {}


#@app.get("/get-item/{item_id}")
#def get_item(item_id: int):
#    return inventory[item_id]

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description = "Returns ID of an item",gt = 0, lt = 1000000)):
    return inventory[item_id]

#http://127.0.0.1:8000
#http://127.0.0.1:8000/docs

# "facebook.com/home?redirect=/tim&msg=fail"          #query parameters are coming after ? mark

#@app.get("/get-by-name")
#def get_item(name: str):          # We define query parameter here
#    for item_id in inventory:
#        if inventory[item_id]["name"] == name:
#            return inventory[item_id]
#        else:
#            return {"Data": "Not found"}



@app.get("/get-by-name/{item_id}")      # here we combine path and query arguments!!
def get_item(*, item_id : int, name: Optional[str] = None, test : int):          # We define query parameter here #                                         
    for item_id in inventory:                                     # * means let this function accept unlimited 
        if inventory[item_id].name == name:                    # keyword arguments.
            return inventory[item_id]
        else:
            return {"Data": "Not found"}


@app.post("/create-item/{item_id}")

def create_item(item_id: int,item: Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists."}

    inventory[item_id] = item

   # inventory[item_id] = {"name": item.name, "brand": item.price, "price": item.price}

    return inventory[item_id]


@app.put("/update-item/{item_id}")

def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:

        return {"Error": "Item ID does not exists."}

    if item.name!=None:
        inventory[item_id].name = item.name

    if item.price!=None:
        inventory[item_id].price = item.price

    if item.brand!=None:
        inventory[item_id].brand = item.brand
    
    return inventory[item_id]


@app.delete("/delete-item")

def delete_item(item_id: int = Query(..., description = "The ID of the item to delete")):
    if item_id not in inventory:
        return {"Error": "ID does not exist"}

    del inventory[item_id]
    return { "Desired item is deleted"}







