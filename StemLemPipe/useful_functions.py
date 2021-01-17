
import re

def remove_urls (vTEXT):
    return re.sub(r'((https|http)?:\/\/|www\.)(\w|\.|\/|\?|\=|\&|\%|-)*', '', vTEXT, flags=re.MULTILINE)

def remove_mails(text):
    return re.sub(r"\S*@\w*\.\w*(\s?|,|\.)",'',text)

def remove_bots(text):
    return re.sub(r"\@[\w\d]*",'',text)


def get_ngrams(arr, n=2):
    """
    Делает n-grams из набора слов.
    Аналогичный метод из TextBlob почему-то автоматом ещё удаляет символы типа # 
    """
    if len(arr)<n:
        yield []
    elif len(arr) == n:
        yield arr
    else:
        for k in range(n,len(arr)+1):
            yield arr[(k-n):k]

def words_to_ngrams_list(words, n_min = 1, n_max = 2):
    """
    converts word array to array with n_grams
    """

    answer = []
    for n in range(n_min, n_max + 1):
        lst = [' '.join(obs) for obs in list(get_ngrams(words, n))]
        if len(lst) > 0:
            answer += lst
    
    return answer



