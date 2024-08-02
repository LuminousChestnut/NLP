from sklearn.feature_extraction.text import CountVectorizer
corpus= ['This is the first document.',
'This is the second document.',
'This is the third document.']
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
print(X.toarray())