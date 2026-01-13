from web3 import Web3
import pandas as pd
from solcx import compile_standard, set_solc_version, install_solc
import json
import time

# Install solc only if needed (run once in your environment) for new user only so pleaase take attention
try:
    set_solc_version('0.8.0')
except:
    install_solc('0.8.0')
    set_solc_version('0.8.0')

#Solidity contract
with open("ReviewStorage.sol", "r") as file:
    contract_source_code = file.read()

compiled_sol = compile_standard({
    "language": "Solidity",
    "sources": {"ReviewStorage.sol": {"content": contract_source_code}},
    "settings": {"outputSelection": {"*": {"*": ["abi", "evm.bytecode"]}}}
})

abi = compiled_sol['contracts']['ReviewStorage.sol']['ReviewStorage']['abi']
bytecode = compiled_sol['contracts']['ReviewStorage.sol']['ReviewStorage']['evm']['bytecode']['object']

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 1337
my_address = w3.eth.accounts[0]
private_key = "0xa4ad6a946564d189f7d64d89dc7520229bc4886ec51b9dcc7b6def46ea46741b"  # Make sure this matches your Ganache account

ReviewContract = w3.eth.contract(abi=abi, bytecode=bytecode)
nonce = w3.eth.get_transaction_count(my_address)
tx = ReviewContract.constructor().build_transaction({
    "chainId": chain_id,
    "from": my_address,
    "nonce": nonce,
    "gas": 2000000,
    "gasPrice": w3.eth.gas_price
})

signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Contract deployed at:", tx_receipt.contractAddress)

contract = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
df = pd.read_csv("reviews_with_predictions.csv")
df_valid = df[df["Predicted"].notna()] 

for _, row in df_valid.iterrows(): 
    # Force prediction to bool (0/1 only, not string)
    predicted_bool = True if int(row["Predicted"]) == 1 else False
    tx = contract.functions.addReview(int(row["ReviewID"]), row["ReviewText"], predicted_bool).build_transaction({
        "chainId": chain_id,
        "from": my_address,
        "nonce": w3.eth.get_transaction_count(my_address),
        "gas": 200000,
        "gasPrice": w3.eth.gas_price
    })
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    w3.eth.wait_for_transaction_receipt(tx_hash)
    time.sleep(0.1)

print("All reviews stored securely on blockchain!")

import json

with open('ReviewStorage_abi.json', 'w') as f:
    json.dump(abi, f)

