
from hashlib import sha256
import json
import time 

class Block:
    def __init__(self,index,transactions,timestamp,previous_hash,nonce=0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce

    def compute_hash(self):
        block_string = json.dumps(self.__dict__,sort_keys=True)
        return sha256(block_string.encode()).hexdigest()




class Blockchain:
    difficulty = 2
    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_gensis_block()

    def create_gensis_block(self):
        gensis_block = Block(0,[],time.time(), "0") 
        gensis_block.hash = gensis_block.compute_hash()
        self.chain.append(gensis_block)
    
    @property 
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self,block):
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0'* Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash

    def add_block(self,block,proof):
        prev_hash = self.last_block.hash
        if prev_hash != block.previous_hash:
            return False
        if not self.is_valid_proof(block,proof):
            return False
        block.hash = proof
        self.chain.append(block)
        return True
    def is_valid_proof(self,block,block_hash):
        return (block_hash.startswith('0' * Blockchain.difficulty) and block_hash == block.compute_hash())
    def add_new_transaction(self,transaction):
        self.unconfirmed_transactions.append(transaction)

    def mine(self):
        if not self.unconfirmed_transactions:
            return False 
        last_block = self.last_block
        new_block = Block(index = last_block.index + 1, transactions = self.unconfirmed_transactions, timestamp = time.time(), previous_hash = last_block.hash)
        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)
        self.unconfirmed_transactions = []
        return new_block.index






from flask import Flask, request
import requests

app = Flask(__name__)

blockchain = Blockchain()

@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)

    return json.dumps({"length":len(chain_data), "chain": chain_data})

@app.route('/chain', methods =['Post'])
def mineBlock():
    #This is a dumb function that adds random "data"
    #feel free to adjust it so that you can get actual transaction from the json response. 
    
    blockchain.add_new_transaction({"data":450141})

    response = blockchain.mine()

    return f"\(response)",204

app.run(debug=True, port = 5000)


