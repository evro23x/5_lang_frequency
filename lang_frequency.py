import os
import re
import sys
import codecs
from collections import Counter

MAX_COUNT = 10


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with codecs.open(filepath, encoding='UTF-8') as shops:
        return shops.read().lower()


def get_most_frequent_words(data):
    return Counter(data).most_common(MAX_COUNT)


def get_all_words(text):
    words = re.findall(r'[^\W|\d]+', text)
    return words

if __name__ == '__main__':
    data_from_file = load_data(sys.argv[1])
    words_list = get_all_words(data_from_file)
    frequent_words = get_most_frequent_words(words_list)
    for pair in frequent_words:
        print("Слово '%s' встречалось в тексте %s раз(а)" % (pair[0], pair[1]))


