from gensim.models.keyedvectors import KeyedVectors
from gensim.models.word2vec import Word2Vec

model = Word2Vec.load('./ko.bin')
print(model)
model.wv.save_word2vec_format('./ko.txt', binary=False)