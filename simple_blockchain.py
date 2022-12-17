### Author: Carolus ###

"""
This code defines a Block class, which represents a single block in the blockchain. Each block has a timestamp, some data, the hash of the previous block, and a hash that is calculated from the block's data and previous hash.

The Blockchain class represents the entire blockchain and contains a list of blocks. It has a method add_block that adds a new block to the blockchain, and a method get_genesis_block that returns the first block in the blockchain (also known as the "genesis block").

The code creates a new Blockchain object and adds three blocks to it. Finally, it iterates over the blocks and prints their contents.
"""
import hashlib
import time

class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self.timestamp) + str(self.data) + str(self.previous_hash)
        sha.update(hash_str.encode('utf-8'))
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.blocks = [self.get_genesis_block()]

    def get_genesis_block(self):
        return Block("Genesis Block", "0")

    def add_block(self, data):
        previous_hash = self.blocks[-1].hash
        new_block = Block(data, previous_hash)
        self.blocks.append(new_block)

blockchain = Blockchain()
blockchain.add_block("Block 1")
blockchain.add_block("Block 2")
blockchain.add_block("Block 3")

for block in blockchain.blocks:
    print("Timestamp:", block.timestamp)
    print("Data:", block.data)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)
    print()