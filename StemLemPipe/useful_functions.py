
import re

def remove_urls(vTEXT):
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
    if len(arr) < n:
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
        lst = [' '.join(obs) if len(obs) > 1 else obs[0] for obs in list(get_ngrams(words, n)) if len(obs) > 0]
        if len(lst) > 0:
            answer += lst
    
    return answer





def remove_hook_words(text, hook_words):
    """
    removes hook words from text with one next word

    for text = "a b c d e f"
    and hook_words = ['b', 'e']
    returns "a d" (without b, e and next words)
    """

    words = text.split()
    answer = []

    k = 0
    while k < len(words):
        if words[k] in hook_words:
            k += 2
        else:
            answer.append(words[k])
            k += 1
    
    return ' '.join(answer)

def remove_words(text, words):
    """
    removes next words from text without splitting to phrases (unlike 'sentence_split')
    """
    return ' '.join([w for w in text.split() if w not in words])


