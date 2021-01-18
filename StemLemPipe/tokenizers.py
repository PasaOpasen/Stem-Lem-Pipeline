
import re
from itertools import zip_longest


def text2sentences(txt, equal_to_space = ["\n"]):
    """
    Разбивает текст на предложения, учитывая, что фразы типа "мат. алгоритмы", "и т. д.", ".NET" --- это всё одно предложение 
    """
    
    inds = []
    
    for i in range(len(txt)):
        if txt[i] == '.':
            if i+1 == len(txt):
                inds.append(i+1)
            elif txt[i+1].isspace():
                if i+2 < len(txt) and (not txt[i+2].islower() or txt[i+2]=='.'):
                    inds.append(i+1)

    if len(inds) > 0:
        answer = [txt[i:j-1] for i,j in zip_longest([0]+inds[:-1], inds)]
        if inds[-1] != len(txt):
            answer += [txt[inds[-1]+1:]]
    else:
        answer = [txt]
    #raise Exception()
    r_template = '\s*[' + "".join(equal_to_space + ["\s"]) + '\s*]'
    answer = [" ".join([v for v in re.split(r_template, t) if len(v)>0]) for t in answer]

    return answer  



def split_by_words(sentence, words):
    """
    Делает split предложения по stopwords
    """
    result = []
    tmp=[]
    for w in sentence.split():
        if w in words:
            if len(tmp)>0:
                result.append(' '.join(tmp))
                tmp=[]
        else: 
            tmp.append(w)
    
    if len(tmp) > 0:
        result.append(' '.join(tmp))
    
    return result


def sentence_split(sentence, separators = ",;!?", stop_words = None):
    """
    Делает split предложения по указанным стоп-словам и сепараторам
    """
    
    r_template = fr"[{separators}]\s*"
    phrases = re.split(r_template, sentence)

    if not (stop_words is None):
        phrases = sum([split_by_words(phrase, stop_words) for phrase in phrases], [])

    return phrases






