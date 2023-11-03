from Block import Block


class BlockChain:
    """
        区块链结构体
            blocks：         包含区块的列表
    """

    def __init__(self):
        self.blocks = []

    def add_block(self, block):
        """
        添加区块
        :param block:
        :return:
        """
        self.blocks.append(block)


# 新建区块
genesis_block = Block(data="创世区块", prev_hash="")
new_block1 = Block(data="张三转给李四一个比特币", prev_hash=genesis_block.hash)
new_block2 = Block(data="张三转给王五三个比特币", prev_hash=genesis_block.hash)

# 新建一个区块链对象
blockChain = BlockChain()
# 将刚才新建的区块加入区块链
blockChain.add_block(genesis_block)
blockChain.add_block(new_block1)
blockChain.add_block(new_block2)

# 打印区块链信息
print("区块链包含区块个数为：%d\n" % len(blockChain.blocks))
blockHeight = 0
for block in blockChain.blocks:
    print(f"本区块高度为：{blockHeight}")
    print(f"父区块哈希：{block.prev_hash}")
    print(f"区块内容：{block.data}")
    print(f"区块哈希：{block.hash}")
    print()
    blockHeight += 1