words = {}

with open('./word_list.txt', encoding='utf8') as f:
    for line in f:
        words[line.replace('\n', '')] = True

with open('./cc.ko.300.vec', encoding='utf8', errors='ignore') as f:
    with open('./my.ko.300.vec', 'w', encoding='utf8') as fw:
        for line in f:
            key = line.strip().split(' ')[0]
            if words.get(key, None):
                fw.write(line)
