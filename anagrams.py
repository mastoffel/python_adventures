from wordsets import english_words, english_words_small

''.join(sorted("hello"))

wors = ['hello', 'its', 'me', 'tsi']

words = {'peon', 'nope', 'stone', 'notes', 'onset',
                       'tones', 'cone', 'pots', 'post', 'stop', 'opts', 'tops'}

canonical = [''.join(sorted(word)) for word in words]
anagrams = {}
{anagrams[can].append({word}) for can,word in zip(canonical, words)}

anagrams = {}
for word in words:
    word_can = ''.join(sorted(word))
    if word_can in anagrams:
        anagrams[word_can].add(word)
    else:
        anagrams[word_can] = {word}
        
anagrams[''.join(sorted("stone"))]