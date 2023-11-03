import hashlib
from datetime import datetime


class Block:
    """
        区块链结构：
            prev_hash：      父区块哈希值
            data：           区块内容
            timestamp：      区块创建时间
            hash：           区块哈希值
    """

    def __init__(self, data, prev_hash):
        # 将传入的父区块哈希值和数据保存到变量中
        self.prev_hash = prev_hash
        self.data = data

        # 获得当前的时间
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 计算区块哈希值
        # 获取哈希对象
        message = hashlib.sha256()
        # 先将数据内容转为字符串并进行编码，再将它们哈希
        # 注意：update() 方法现在只接受 bytes 类型的数据，不接收 str 类型
        message.update(str(self.prev_hash).encode('utf-8'))
        message.update(str(self.prev_hash).encode('utf-8'))
        message.update(str(self.prev_hash).encode('utf-8'))
        # update() 更新 hash 对象，连续的调用该方法相当于连续的追加更新
        # 返回字符串类型的消息摘要
        self.hash = message.hexdigest()