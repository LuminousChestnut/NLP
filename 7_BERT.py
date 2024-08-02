from transformers import BertTokenizer, BertModel
# 1.1 加载预训练模型和分词器
tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')
model = BertModel.from_pretrained('bert-base-chinese')
# 1.2 输入句子
sentence = "这是一个使用BERT生成句向量的例子"
# 1.3 对句子进行编码
inputs = tokenizer(sentence, return_tensors='pt')
# 1.4 通过BERT模型获取输出
outputs = model(**inputs)
# 1.5 提取句向量，通常使用[CLS]标记对应的隐藏状态
sentence_vector = outputs.last_hidden_state[:, 0, :]