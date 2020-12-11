import datetime
import hashlib
import json
from flask import Flask, jsonify


# creating a Black

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 'data': None
                 }
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        while 1:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                return new_proof
            else:
                new_proof += 1

    def hash(self, block):
        return hashlib.sha256(json.dumps(block, sort_keys = True).encode()).hexdigest()


    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False

            previous_block = block
            block_index += 1

        return True


############
#creating a web app
##########
app = Flask(__name__)
##########

#creating a blockchain

blockchain = Blockchain()

#mining a new block

@app.route('/mine_block', methods= ['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {'message': 'Congo u created a new block',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash']}
    # print(response)
    return jsonify(response), 200

#getting full blockchain

@app.route('/get_chain', methods= ['GET'])
def get_chain():
    response = {'chain_key': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200

#checking is vaild
@app.route('/isvalid', methods=['GET'])
def isvalid():
    response = {'Blockchain Valid':blockchain.is_chain_valid(blockchain.chain)}
    return response, 200

#runnig the webapp
host, port = '0.0.0.0', 5000
# mine_block()
app.run(host, port, debug=True)















