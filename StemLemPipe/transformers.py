

def phrases_transform(phrases, func):
    """
    Converts phrases to using func for each phrase

    phrases must be list of phares (like it's got from sentence: ['Like', 'this phrases', 'array of words array'])
    or list of list of phrases (like list of phrases from sentences from text) 
    """
    answer = [p for p in phrases if len(p) > 0]
    result = []

    if type(answer[0]) == list:
        for i in range(len(answer)):
            sub_answer = [func(a) for a in answer[i] if len(a) > 0]
            if len(sub_answer) > 0:
                result.append(sub_answer)
    else:
        result = [func(a) for a in answer if len(a) > 0]

    return result     



def phrases2lower(phrases):
    """
    Converts phrases to lower case and removes empty observations

    phrases must be list of phares (like it's got from sentence: ['Like', 'this phrases', 'array of words array'])
    or list of list of phrases (like list of phrases from sentences from text) 
    """

    return phrases_transform(phrases, lambda phrase: phrase.lower()) 


def phrases_without_excess_symbols(phrases, include_alpha = True, include_numbers = False, include_also = None):
    """
    Converts phrases to phrases without excess symbols like "'"|" and so on

    phrases must be list of phares (like it's got from sentence: ['Like', 'this phrases', 'array of words array'])
    or list of list of phrases (like list of phrases from sentences from text) 
    """
    false_check = lambda symbol: False

    check1 = (lambda symbol: symbol.isalpha()) if include_alpha else false_check
    check2 = (lambda symbol: symbol.isnumeric()) if include_numbers else false_check
    check3 = (lambda symbol: symbol in include_also) if  not (include_also is None) else false_check

    remover = lambda phrase: ' '.join((''.join([a for a in phrase if a == ' ' or check1(a) or check2(a) or check3(a)])).split())

    return phrases_transform(phrases, remover)






