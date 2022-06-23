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
import re

app = FastAPI()

@app.get("/all-SFT-metadata")

def get_SFT_metadata():

    infura_url = "https://rinkeby.infura.io/v3/1ca5ad9c22fc4bc3b088ee54d9af02a4"  # Rinkeby BC

    web3 = Web3(Web3.HTTPProvider(infura_url))

    sft_address = '0x3841c2edc65DF0FB7d6A632a1a0e2efbe65d32f9'
    sft_abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256[]","name":"ids","type":"uint256[]"},{"indexed":false,"internalType":"uint256[]","name":"values","type":"uint256[]"}],"name":"TransferBatch","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"TransferSingle","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"value","type":"string"},{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"}],"name":"URI","type":"event"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"accounts","type":"address[]"},{"internalType":"uint256[]","name":"ids","type":"uint256[]"}],"name":"balanceOfBatch","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id_","type":"uint256"},{"internalType":"uint256","name":"amount_","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"ids_","type":"uint256[]"},{"internalType":"uint256[]","name":"amounts_","type":"uint256[]"}],"name":"burnBatch","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"countSFT","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"uri_","type":"string"},{"internalType":"uint256","name":"amount_","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"ids_","type":"uint256[]"},{"internalType":"uint256[]","name":"amounts_","type":"uint256[]"},{"internalType":"string[]","name":"uris_","type":"string[]"}],"name":"mintBatch","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256[]","name":"ids","type":"uint256[]"},{"internalType":"uint256[]","name":"amounts","type":"uint256[]"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeBatchTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId_","type":"uint256"}],"name":"uri","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"}]')

    sft_contract = web3.eth.contract(address = sft_address, abi = sft_abi)

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

@app.get("/all-petros-holders")

def get_all_petros_holders():

    total_petros_holders = []

    headers = {
    'authority': 'rinkeby.etherscan.io',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    }

    params = {
    'a': '0xD8AFa55703A442a127761E5CA897e060Cb3dcb2b',
    'p': '1',
    }

    response = requests.get('https://rinkeby.etherscan.io/token/generic-tokenholders2', params=params, headers=headers)


    total_token_holder_count = int(re.findall(r"nA total of(.*?) token holders\\", str(response.content))[0].strip(' '))
    petros_holders = re.findall(r"a=(.*?)\\", str(response.content))

    total_petros_holders.append(petros_holders)

    page_count = 1 + total_token_holder_count//50

    if(page_count == 1):
        pass
    else:
        for i in range(2,(page_count+1)):
        
            params['p'] = f'{i}'
        
            response = requests.get('https://rinkeby.etherscan.io/token/generic-tokenholders2', params=params, headers=headers)
        
            petros_holders = re.findall(r"a=(.*?)\\", str(response.content))

            total_petros_holders.append(petros_holders)
        
    total_petros_holders = [i for ix in total_petros_holders for i in ix]

    return total_petros_holders



@app.get("/all-petros-holder-count")

def get_all_petros_holders():

    headers = {
    'authority': 'rinkeby.etherscan.io',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    }

    params = {
    'a': '0xD8AFa55703A442a127761E5CA897e060Cb3dcb2b',
    'p': '1',
    }

    response = requests.get('https://rinkeby.etherscan.io/token/generic-tokenholders2', params=params, headers=headers)

    total_token_holder_count = int(re.findall(r"nA total of(.*?) token holders\\", str(response.content))[0].strip(' '))

    return total_token_holder_count


@app.get("/all-petros-holders-sorted-ETH")

def all_petros_sorted_ETH():

    total_petros_holders = []

    headers = {
        'authority': 'rinkeby.etherscan.io',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    }

    params = {
        'a': '0xD8AFa55703A442a127761E5CA897e060Cb3dcb2b',
        'p': '1',
    }

    response = requests.get('https://rinkeby.etherscan.io/token/generic-tokenholders2', params=params, headers=headers)


    total_token_holder_count = int(re.findall(r"nA total of(.*?) token holders\\", str(response.content))[0].strip(' '))
    petros_holders = re.findall(r"a=(.*?)\\", str(response.content))

    total_petros_holders.append(petros_holders)

    page_count = 1 + total_token_holder_count//50

    if(page_count == 1):
        pass
    else:
        for i in range(2,(page_count+1)):

            params['p'] = f'{i}'

            response = requests.get('https://rinkeby.etherscan.io/token/generic-tokenholders2', params=params, headers=headers)

            petros_holders = re.findall(r"a=(.*?)\\", str(response.content))

            print(petros_holders)


            total_petros_holders.append(petros_holders)

    total_petros_holders = [i for ix in total_petros_holders for i in ix]


    h_eth_list = []

    infura_url = "https://rinkeby.infura.io/v3/1ca5ad9c22fc4bc3b088ee54d9af02a4"  # Rinkeby BC
    web3 = Web3(Web3.HTTPProvider(infura_url))

    for i in total_petros_holders:
        h_add =  web3.toChecksumAddress(i)
        eth = web3.eth.getBalance(h_add)
        h_eth_list.append(round((eth * 10**(-18 )),4))


    h_sorting_dict = {}
    for i in range(len(total_petros_holders)):
            h_sorting_dict[total_petros_holders[i]] = h_eth_list[i]

    h_sorting_dict = {k: v for k, v in sorted(h_sorting_dict.items(), key=lambda item: item[1], reverse = True)}

#   holders_sorted_largest_to_smallest = list(h_sorting_dict.keys())

    return h_sorting_dict
        







