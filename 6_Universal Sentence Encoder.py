import tensorflow_hub as hub
import tensorflow_text
# 加载模型
module_url = "https://tfhub.dev/google/universal-sentence-encoder-multilingual/3"
model = hub.load(module_url)
sentences = ["This is the first sentence.", "This is the second sentence.", "This is the third sentence."]
embeddings = model(sentences)
print(embeddings)
