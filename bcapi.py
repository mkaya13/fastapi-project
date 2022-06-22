# fastAPI

# Tradionally when you write your API, you have to follow certain rules that your API accepts. However, you will be able to define types of all of the data your API expect. In fastAPI all of this automatically done for you. If smn sends you wrong type of info to your API end point, it will automatically return them an error message saying hey you should have used this like this etc.
# fastAPI does all of the data validations for you.
# Autodocuments for your entire API
# We are gonna get a really good auto completion.

# GET    --> This endpoint is going to be returning information
# POST   --> U are gonne be sending information to the post endpoint or this endpoint will be creating smg new.
# PUT    --> To update smg already existing in the database. Modify info
# DELETE --> Delete smg, get rid of info.

#uvicorn bcapi:app --reload

from fastapi import FastAPI, Path,  Query, HTTPException, status
from typing import Optional   # Recommended from fastAPI docs you implement that
from pydantic import BaseModel
import json,requests
from web3 import Web3


infura_url = "https://rinkeby.infura.io/v3/1ca5ad9c22fc4bc3b088ee54d9af02a4"  # Rinkeby BC
web3 = Web3(Web3.HTTPProvider(infura_url))

sft_address = '0x3841c2edc65DF0FB7d6A632a1a0e2efbe65d32f9'
sft_abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256[]","name":"ids","type":"uint256[]"},{"indexed":false,"internalType":"uint256[]","name":"values","type":"uint256[]"}],"name":"TransferBatch","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"TransferSingle","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"value","type":"string"},{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"}],"name":"URI","type":"event"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"accounts","type":"address[]"},{"internalType":"uint256[]","name":"ids","type":"uint256[]"}],"name":"balanceOfBatch","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id_","type":"uint256"},{"internalType":"uint256","name":"amount_","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"ids_","type":"uint256[]"},{"internalType":"uint256[]","name":"amounts_","type":"uint256[]"}],"name":"burnBatch","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"countSFT","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"uri_","type":"string"},{"internalType":"uint256","name":"amount_","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"ids_","type":"uint256[]"},{"internalType":"uint256[]","name":"amounts_","type":"uint256[]"},{"internalType":"string[]","name":"uris_","type":"string[]"}],"name":"mintBatch","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256[]","name":"ids","type":"uint256[]"},{"internalType":"uint256[]","name":"amounts","type":"uint256[]"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeBatchTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId_","type":"uint256"}],"name":"uri","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"}]')

sft_contract = web3.eth.contract(address = sft_address, abi = sft_abi)


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





@app.get("/all-SFT-metadata")

def get_SFT_metadata():

    token_ids = [i for i in range(1, sft_contract.functions.countSFT().call() + 1)]

    smart_contract_metadata = []

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    for i in token_ids:
    
        try:
            url = sft_contract.functions.uri(i).call()
    
            r = requests.get(url, headers = headers)
    
            smart_contract_metadata.append(r.json())
    
        except:
            pass

    
    return smart_contract_metadata







