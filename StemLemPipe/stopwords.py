
from stop_words import get_stop_words


stop_words_dict = {}


def stopwords(language = 'ru'):

    global stop_words_dict

    if language in stop_words_dict:
        return stop_words_dict[language]

    words = set(get_stop_words(language))
    stop_words_dict[language] = words

    return words




