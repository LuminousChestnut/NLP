from gensim.models import Word2Vec
sentences = [['this', 'is', 'the', 'first', 'sentence', '.'],
             ['this', 'is', 'the', 'second', 'sentence', '.'],
             ['this', 'is', 'the', 'third', 'sentence', '.']]
model = Word2Vec(sentences, min_count=1)
print(model.wv['sentence'])
