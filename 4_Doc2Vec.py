from gensim.models.doc2vec import Doc2Vec, TaggedDocument
documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(['This is the first document.',
                                                               'This is the second document.',
                                                               'This is the third document.'])]
model = Doc2Vec(documents, vector_size=5, window=2, min_count=1, workers=4, epochs=100)
print(model.docvecs[0])
