import hashlib as hasher
import datetime as time


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index)) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return sha.hexdigest()

    @property
    def create_genesis_block():
        s = 1
        return Block(0, time.datetime.now(), "Block Data", "0")

    def next_block(last_block):
        this_index = last_block.index + 1
        this_timestamp = time.datetime.now()
        this_data = "Hey! I'm Block" + str(this_index)
        this_hash = last_block.hash
        return Block(this_index, this_timestamp, this_data, this_hash)

    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]
    # 生成二十个为例
    num_of_blocks_to_add = 20
    for i in range(0, num_of_blocks_to_add):
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add
        print("Block #{} has been added to the blockchain!".format(block_to_add.index))
        print("Hash:{}\n".format(block_to_add.hash))
