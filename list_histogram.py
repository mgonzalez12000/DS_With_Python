# Marco Gonzalez
# CS 3035-01
# Has a function where it iterates through a list and is in charge
# of returning a list of tuples with its corresponding key and value

import timeit
from text_processing import list_text


def word_tuple():
    list_of_words = list_text.copy()
    dictionary = {}

    start = timeit.default_timer()
    for word in list_of_words:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
    list_tuple = [(key, value) for key, value in (dictionary.items())]
    end = timeit.default_timer()

    for items in sorted(list_tuple):
        print(items)

    print('Word count for the list of tuples:', len(list_tuple))
    print('The list of tuples took:', end - start)
    print('--------------------------------------------------------')
