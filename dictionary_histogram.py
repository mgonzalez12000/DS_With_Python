# Marco Gonzalez
# CS 3035-01
# Consists of a function that is in charge of iterating through the list,
# storing it in a dictionary, and keeping track of its key and corresponding value
# returns a dictionary with its keys and values being populated

import timeit
from text_processing import list_text


def word_dictionary():
    list_of_words = list_text.copy()
    dictionary = {}

    start = timeit.default_timer()
    for word in list_of_words:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
    end = timeit.default_timer()

    for key, value in sorted(dictionary.items()):
        print("'{}': {}".format(key, value))

    print('Word count for dictionary:', len(dictionary))
    print('Dictionary took:', end - start)
