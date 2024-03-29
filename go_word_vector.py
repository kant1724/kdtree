import numpy as np
from scipy.spatial import KDTree

def get_coefs(word, *arr):
    return word, np.asarray(arr, dtype='float32')

def load_embeddings(path):
    with open(path, encoding='utf8', errors='ignore') as f:
        dict = {}
        for line in f:
            try:
                word, arr = get_coefs(*line.strip().split(' '))
                dict[word] = arr
            except:
                pass
        return dict

'''
    Load Word Embeddings
'''
embedding_data = load_embeddings('./my.ko.300.vec')

'''
    제품 키워드
'''
my = ['연필']
my_vector = [embedding_data[my[0]]]

'''
    창고 키워드
'''
others = ['자동차', '하드웨어', '과일', '사무용품', '가전기기']
others_vector = []
for other in others:
    others_vector.append(embedding_data[other])

# KDTree알고리즘으로 매칭되는 키워드를 유사도 순으로 가져옴 (k는 가져올 갯수)
dist_idx = [KDTree(others_vector).query(my_vector, k=5)]

print(dist_idx)

for from_idx, (distance, index) in enumerate(dist_idx):
    distance = distance[0]
    index = index[0]
    for i in range(len(distance)):
        d = distance[i]
        nm = others[index[i]]
        print('`' + my[from_idx] + '`으로부터 ' + str(i + 1) + '번째로 유사한 키워드: ' + nm)
