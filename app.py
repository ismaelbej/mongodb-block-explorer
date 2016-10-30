#!/usr/bin/env python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/blockchaininfo', methods=['GET'])
def get_blockchain_info():
    return jsonify({'hash': '0', 'height': 0, 'prevhash': '1', 'date': ''})

@app.route('/api/v1/block/<hash>', methods=['GET'])
def get_block(hash):
    return jsonify({'hash': hash, 'height': 0, 'prevhash': '1', 'transactions': ['0', '1']})

@app.route('/api/v1/tx/<txid>', methods=['GET'])
def get_transaction(txid):
    return jsonify({'txid': txid, 'block': '0', 'height': 0, 'confirmations': 0, 'in': [], 'out': []})

@app.route('/api/v1/address/<address>/balance', methods=['GET'])
def get_address_balance(address):
    addresses = address.split(",")
    response = {}
    for address in addresses:
        response[address] = {'confirmed': {'amount': 0},'unconfirmed': {'amount': 0}}
    return jsonify(response)

@app.route('/api/v1/address/<address>/transactions', methods=['GET'])
def get_address_transactions(address):
    addresses = address.split(",")
    response = {}
    for address in addresses:
        response[address] = ['0', '1']
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
