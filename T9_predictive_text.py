# text on 9 keys, like in the old days
import helper
from collections import defaultdict
from functools import reduce
import operator

def parse_content(content):
    text = content.split('\n')
    text_dict = {i.split()[0]: int(''.join(i.split()[1:])) for i in text}
    return text_dict

def make_tree(words):
    '''
    Idea: Condense the tree so that each internal node is a number. 
    This leads to a single subtree for every combination of numbers.
    '''
    keymap_switched = {y:x for x,y in helper.keymap.items()}
    root = dict()
    for word in words:
        current_dict = root
        for l in word:
            num_key = ''.join([value for key, value in keymap_switched.items() if l in list(key)])
            current_dict = current_dict.setdefault(num_key, {})
        current_dict['$'+word] = words[word]
    return root

tree = make_tree(parse_content('ngrams-10k.txt'))

reduce(operator.getitem, ['2', '3', '5'], tree)

def recursive_lookup(sub_tree, prefix = '$', words = []):
    for k, v in sub_tree.items():
        if '$' in k:
            words.append((k.replace('$', ''), v))
        if hasattr(v, 'items'): # check if value is again a dictionary
            recursive_lookup(v, prefix = '$', words = words)
    return words

def predict(tree, numbers):
    num_list = list(str(numbers))
    # get relevant subtree
    sub_tree = reduce(operator.getitem, num_list, tree)
    # find and retrieve all keys with $ in sub_tree
    out = recursive_lookup(sub_tree, prefix = '$', words = [])
    out_sorted = sorted(out, key = lambda x: x[1], reverse = True)
    return out_sorted
    
if __name__ == '__main__':
    content = helper.read_content(filename='ngrams-10k.txt')

    # When you've finished implementing a part, remove the `gold.` prefix to check your own code.

    # PART 1: Parsing a string into a dictionary.
    words = parse_content(content)

    # PART 2: Building a trie from a collection of words.
    tree = make_tree(words)

    while True:
        # PART 3: Predict words that could follow
        numbers = helper.ask_for_numbers()
        predictions = predict(tree, numbers)

        if not predictions:
            print('No words were found that match those numbers. :(')
        else:
            for prediction, frequency in predictions[:10]:
                print(prediction, frequency)

        response = input('Want to go again? [y/N] ')
        again = response and response[0] in ('y', 'Y')
        if not again:
            break
    



