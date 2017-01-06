import os
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


if __name__ == '__main__':
    data_from_file = load_data(sys.argv[1]).split()
    frequent_words = get_most_frequent_words(data_from_file)
    for pair in frequent_words:
        print("Слово '%s' встречалось в тексте %s раз(а)" % (pair[0], pair[1]))


