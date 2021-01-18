
# lemma analyzers
from pymystem3 import Mystem
import pymorphy2
from nltk.stem import WordNetLemmatizer
# stemmers 
#import Stemmer
import nltk
from nltk.stem.snowball import RussianStemmer



lemmatizers = {
    'en': {
        'wordnet': WordNetLemmatizer()
        },
    'ru': {
        'pymorphy': pymorphy2.MorphAnalyzer(),
        'mystem': Mystem()
    } 
}

#stemmer_stemmer = Stemmer.Stemmer('russian')

stemmers = {
    'ru': RussianStemmer(False),
    'en': nltk.stem.SnowballStemmer('english')
}



def lemmatize_wordnet(text):
    lemmas = lemmatizers['en']['wordnet'].lemmatize(text)
    return ''.join(lemmas[:-1])   

def lemmatize_mystem(text):
    lemmas = lemmatizers['ru']['mystem'].lemmatize(text)
    return ''.join(lemmas[:-1])

def lemmatize_morphy(text):
    
    return ' '.join([lemmatizers['ru']['pymorphy'].parse(word)[0].normal_form for word in text.split()])


#def stem_stemmer(text):
#
#    return ' '.join(stemmer_stemmer.stemWords(text.split()))

def stem_nltk(text, language = 'ru'):
    return ' '.join([stemmers[language].stem(word) for word in text.split()])




def create_lemmatizer(backend = 'pymorphy', language = 'ru'):
    if language == 'ru':
        if backend == 'pymorphy':
            return lambda text: lemmatize_morphy(text)
        
        if backend == 'mystem':
            return lambda text: lemmatize_mystem(text)
        
        raise Exception(f"unknown lemmatizer backend ({backend})")
    
    elif language == 'en':
        return lambda text: lemmatize_wordnet(text)
    
    else:
        raise Exception(f"Unsupported language {language}")


def create_stemmer(backend = 'snowball', language = 'ru'):
    
    if backend == 'snowball':
        return lambda text: stem_nltk(text, language)
    
    raise Exception(f"unknown stemmer backend ({backend})")

def create_stemmer_lemmer(lemmatizer_backend = 'pymorphy', stemmer_backend = 'snowball', language = 'ru'):

    ln = lemmatizer_backend is None
    sn = stemmer_backend is None

    if ln and sn:
        return lambda text: text
    
    if ln:
        return create_stemmer(stemmer_backend, language)
    if sn:
        return create_lemmatizer(lemmatizer_backend, language)
    
    f_lem = create_lemmatizer(lemmatizer_backend, language)
    f_stem = create_stemmer(stemmer_backend, language)
    
    return lambda text: f_stem(f_lem(text))



if __name__ == '__main__':
    
    text = "стал становился морковь морковного яблока филе"
    
    print(lemmatize_mystem(text))
    
    print(lemmatize_morphy(text))
    
 #   print(stem_stemmer(text))
    
    print(stem_nltk(text))

    lem = create_lemmatizer('pymorphy')
    stem = create_stemmer()
    print(stem(lem(text)))

    pipe = create_stemmer_lemmer()
    print(pipe(text))



