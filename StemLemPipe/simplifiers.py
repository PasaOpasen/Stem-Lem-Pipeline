
import itertools



def sum_phrases(phrases):
    """
    converts nested list of phrases to simple total sum list
    """
    
    answer = list(itertools.chain.from_iterable(phrases))

    while type(answer[0]) == list:
        answer = list(itertools.chain.from_iterable(answer))
    
    return answer


def wordlist2set(input_list, save_order = False):
    """
    converts list of phrases to set

    if save_order == False, n-grams like 'word1 word2' and 'word2 word1' will be equal in result set
    """

    if save_order:
        return set(input_list)

    return set([' '.join(sorted(words.split())) for words in input_list])


