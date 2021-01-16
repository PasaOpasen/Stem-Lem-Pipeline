
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
    if len(arr) == n:
        yield arr
    
    for k in range(n,len(arr)+1):
        yield arr[(k-n):k]




