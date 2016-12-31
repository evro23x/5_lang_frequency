import sys
import pprint
import operator
import codecs


def load_data(filepath):
    with codecs.open(filepath, encoding='UTF-8') as shops:
        return shops.read()


def get_most_frequent_words(text):
    requent_words = {}
    for word in text:
        if word in requent_words.keys():
            requent_words[word] += 1
        else:
            requent_words[word] = 1
    return sorted(requent_words.items(), key=operator.itemgetter(1), reverse=True)


if __name__ == '__main__':
    data = load_data(sys.argv[1]).split()
    pprint.pprint(get_most_frequent_words(data)[0:9])
