import sys
import operator
import codecs


def load_data(filepath):
    with codecs.open(filepath, encoding='UTF-8') as shops:
        return shops.read()


def get_most_frequent_words(data):
    dict_words = {}
    for word in data:
        word = word.lower()
        if word in dict_words.keys():
            dict_words[word] += 1
        else:
            dict_words[word] = 1
    return sorted(dict_words.items(), key=operator.itemgetter(1), reverse=True)


if __name__ == '__main__':
    data_from_file = load_data(sys.argv[1]).split()
    frequent_words = get_most_frequent_words(data_from_file)[0:9]
    for pair in frequent_words:
        print("Слово '%s' встречалось в тексте %s раз(а)" % (pair[0], pair[1]))
