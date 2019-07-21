import numpy as np

words = {
    '연필': True,
    '딸기': True,
    '자동차': True,
    '하드웨어': True,
    '과일': True,
    '사무용품': True,
    '가전기기': True,
    '청소기': True,
    '컴퓨터': True,
    '수박': True,
    '사과': True,
    '종이': True
}

with open('./cc.ko.300.vec', encoding='utf8', errors='ignore') as f:
    with open('./my.ko.300.vec', 'w', encoding='utf8') as fw:
        for line in f:
            key = line.strip().split(' ')[0]
            if words.get(key, None):
                fw.write(line)
