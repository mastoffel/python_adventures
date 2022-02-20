import collections

c = Counter(['a', 'b', 'c', 'a', 'b', 'b'])

def count_unique_words(filename):
    with open(filename, 'r') as words:
        contents = words.read()
    words = contents.replace('\n', ' ').replace(',', ' ').replace('.', ' ').split(' ')
    words_count = collections.Counter(words)
    words_count.pop('', None)
    words_sorted = sorted(words_count.items(), key=lambda x: x[1], reverse=True)
    for keys, values in words_sorted:
        print(keys, values)

def count_unique_words(filename):
    words = collections.Counter()
    with open(filename) as f:
        for line in f:
            words.update(line.split())
    for word, count in words.most_common(10):
        print(word, count)

sorted(words_count.items(), key=lambda x: x[1], reverse=True)
count_unique_words('test_words.txt')

