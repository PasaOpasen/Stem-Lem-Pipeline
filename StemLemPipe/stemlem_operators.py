
# lemma analyzers
from pymystem3 import Mystem
import pymorphy2
# stemmers 
#import Stemmer
from nltk.stem.snowball import RussianStemmer

m = Mystem()
morph = pymorphy2.MorphAnalyzer()

#stemmer_stemmer = Stemmer.Stemmer('russian')

stemmer_nltk = RussianStemmer(False)



def lemmatize_mystem(text):
    lemmas = m.lemmatize(text)
    return ''.join(lemmas[:-1])

def lemmatize_morphy(text):
    
    return ' '.join([morph.parse(word)[0].normal_form for word in text.split()])


#def stem_stemmer(text):
#
#    return ' '.join(stemmer_stemmer.stemWords(text.split()))

def stem_nltk(text):
    return ' '.join([stemmer_nltk.stem(word) for word in text.split()])




def create_lemmatizer(backend = 'pymorphy'):

    if backend == 'pymorphy':
        return lambda text: lemmatize_morphy(text)
    
    if backend == 'mystem':
        return lambda text: lemmatize_mystem(text)
    
    raise Exception(f"unknown lemmatizer backend ({backend})")

def create_stemmer(backend = 'snowball'):
    
    if backend == 'snowball':
        return lambda text: stem_nltk(text)
    
    raise Exception(f"unknown stemmer backend ({backend})")

def create_stemmer_lemmer(lemmatizer_backend = 'pymorphy', stemmer_backend = 'snowball'):

    ln = lemmatizer_backend is None
    sn = stemmer_backend is None

    if ln and sn:
        return lambda text: text
    
    if ln:
        return create_stemmer(stemmer_backend)
    if sn:
        return create_lemmatizer(lemmatizer_backend)
    
    f_lem = create_lemmatizer(lemmatizer_backend)
    f_stem = create_stemmer(stemmer_backend)
    
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



