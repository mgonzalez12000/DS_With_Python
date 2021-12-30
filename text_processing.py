# Marco Gonzalez
# CS 3035-01
# Is in charge of fFile IO and returns a list with all the words (in lowercase) of the file.

import string

list_text = []


def read_file(user_input):
    with open(user_input, encoding='UTF-8-sig') as file:
        for line in file:
            for word in line.split():
                word = word.lower()
                translation_table = word.maketrans(dict.fromkeys(string.punctuation + '“”’‘'))
                word_2 = word.translate(translation_table)
                if word_2 == '':
                    continue
                else:
                    list_text.append(word_2)
