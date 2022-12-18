### Author: Soulacex ###

import hashlib
import datetime

"""
    This code takes from some of the simple_blockchain module in order to set up a very basic type of crytocurrency within Python
"""

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.generate_hash()
    
    def generate_hash(self):
        """Generate the hash for the current block using SHA-256"""
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        """Create the first block in the chain (also known as the Genesis block)"""
        return Block(0, datetime.datetime.now(), "Genesis block", "0")
    
    def add_block(self, data):
        """Add a new block to the chain"""
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), datetime.datetime.now(), data, previous_block.hash)
        self.chain.append(new_block)
    
    def is_chain_valid(self):
        """Verify that the chain is valid by checking the hashes of each block"""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block.generate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

def main():
### This code will create an instance of the Blockchain class, add three blocks to it, and then print the entire chain and verify its validity. ### 
### When you run the code, you should see something similiar to the following output: ###

### [<__main__.Block object at 0x7f958f3b3e80>, <__main__.Block object at 0x7f958f3b3ef0>, <__main__.Block object at 0x7f958f3b3f60>, <__main__.Block object at 0x7f958f3b3fd0>] ###
### True ### 

    blockchain = Blockchain()
    blockchain.add_block("First block")
    blockchain.add_block("Second block")
    blockchain.add_block("Third block")
    
    print(blockchain.chain)
    print(blockchain.is_chain_valid())

if __name__ == "__main__":
    main()