from transformers import GPT2Tokenizer, GPT2LMHeadModel
# 3.1 加载预训练模型和分词器
tokenizer = GPT2Tokenizer.from_pretrained('gpt2-medium')
model = GPT2LMHeadModel.from_pretrained('gpt2-medium')
# 3.2 输入句子
sentence = "这是一个使用GPT生成文本的例子"
# 3.3 对句子进行编码
inputs = tokenizer(sentence, return_tensors='pt')
# 3.4 通过GPT模型获取输出
outputs = model(**inputs)
# 3.5 GPT不直接提供句向量，但可以通过平均词向量得到近似结果
sentence_vector = outputs.last_hidden_state.mean(dim=1)
