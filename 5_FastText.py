from gensim.models.fasttext import FastText
sentences = [['this', 'is', 'the', 'first', 'sentence', '.'],
['this', 'is', 'the', 'second', 'sentence', '.'],
['this', 'is', 'the', 'third', 'sentence', '.']]
model = FastText(sentences, size=5, window=2, min_count=1, workers=4, sg=1)
print(model.wv['sentence'])
