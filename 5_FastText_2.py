from gensim.models import FastText
from gensim.test.utils import common_texts, get_tmpfile
model = FastText(common_texts, size=4, window=3, min_count=1, iter=10)
test_data = ['this is a positive sentence', 'this is a negative sentence']
for text in test_data:
    predicted_label = model.wv.most_similar(text)[0][0]
    print('predicted label:', predicted_label)
