# Marco Gonzalez
# CS 3035-01
# Takes user input, and calls other modules and its respective functions. Can be considered the "Driver"
# Video explanation link: https://calstatela.instructuremedia.com/embed/08a4c517-74ca-412a-a5c0-238aa6963784

import text_processing
import dictionary_histogram
import list_histogram


def main():
    user_input = input('Please input a txt file: ')
    return text_processing.read_file(user_input)


if __name__ == "__main__":
    main()
    print('This is a list of tuples:')
    list_histogram.word_tuple()
    print('This is dictionary:')
    dictionary_histogram.word_dictionary()
