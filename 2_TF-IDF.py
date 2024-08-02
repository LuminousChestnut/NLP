from sklearn.feature_extraction.text import TfidfVectorizer
corpus = ['This is the first document.',
          'This is the second document.',
          'This is the third document.']
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
print(X.toarray())