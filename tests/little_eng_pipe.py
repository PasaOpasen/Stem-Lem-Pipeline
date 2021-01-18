
import sys
sys.path.append('..')


from StemLemPipe import phrases2lower, phrases_without_excess_symbols, phrases_transform, text2sentences, split_by_words, sentence_split, create_stemmer_lemmer, words_to_ngrams_list, sum_phrases, wordlist2set, stopwords, StemLemPipeline


text_example = """Lemmatization is the process of grouping together the different inflected forms of a word so they can be analysed as a single item. Lemmatization is similar to stemming but it brings context to the words. So it links words with similar meaning to one word."""

#text_example = "This is some example # @ noised text. It shows all transformations, but it's small because of consequences"

def print2(obj):
    print(obj)
    print()


# create stemmer-lemmatizer pipeline function
stem_lem = create_stemmer_lemmer(lemmatizer_backend='wordnet', stemmer_backend='snowball', language = 'en')


# convert all text to list of sentences
sentences = text2sentences(text_example)
print2(sentences)

# ['Lemmatization is the process of grouping together the different inflected forms of a word so they can be analysed as a single item', 'Lemmatization is similar to stemming but it brings context to the words', 'So it links words with similar meaning to one word']


# transform each phrase to lower case
clean_sentences = phrases2lower(sentences)
print2(clean_sentences)
# ['lemmatization is the process of grouping together the different inflected forms of a word so they can be analysed as a single item', 'lemmatization is similar to stemming but it brings context to the words', 'so it links words with similar meaning to one word']

# split each sentence to list of phrases between separators and stop words
phrases = [sentence_split(sentence , separators=',;', stop_words = stopwords('en')) for sentence in clean_sentences]
print2(phrases)
# [['lemmatization', 'process', 'grouping together', 'different inflected forms', 'word', 'can', 'analysed', 'single item'], ['lemmatization', 'similar', 'stemming', 'brings context', 'words'], ['links words', 'similar meaning', 'one word']]


# remove excess symbols from phrases
char_phrases = phrases_without_excess_symbols(phrases, include_alpha= True, include_numbers= True)
print2(char_phrases)
# [['lemmatization', 'process', 'grouping together', 'different inflected forms', 'word', 'can', 'analysed', 'single item'], ['lemmatization', 'similar', 'stemming', 'brings context', 'words'], ['links words', 'similar meaning', 'one word']]

# stem and lemmatize all words in all phrases
stemmed_phrases = phrases_transform(char_phrases, func = stem_lem)
print2(stemmed_phrases)
# [['lemmatizatio', 'proce', 'group togeth', 'differ inflect form', 'wor', 'ca', 'analys', 'singl ite'], ['lemmatizatio', 'simila', 'stemmin', 'bring contex', 'wor'], ['link word', 'similar meanin', 'one wor']]

# convert each phrase to list of n-grams
n_grams = phrases_transform(stemmed_phrases, func = lambda w: words_to_ngrams_list(w.split(), n_min = 1, n_max = 2))
print2(n_grams)
# [[['lemmatizatio'], ['proce'], ['group', 'togeth', 'group togeth'], ['differ', 'inflect', 'form', 'differ inflect', 'inflect form'], ['wor'], ['ca'], ['analys'], ['singl', 'ite', 'singl ite']], [['lemmatizatio'], ['simila'], ['stemmin'], ['bring', 'contex', 'bring contex'], ['wor']], [['link', 'word', 'link word'], ['similar', 'meanin', 'similar meanin'], ['one', 'wor', 'one wor']]]

# convert list of list of list to just list
total = sum_phrases(n_grams)
print2(total)
# ['lemmatizatio', 'proce', 'group', 'togeth', 'group togeth', 'differ', 'inflect', 'form', 'differ inflect', 'inflect form', 'wor', 'ca', 'analys', 'singl', 'ite', 'singl ite', 'lemmatizatio', 'simila', 'stemmin', 'bring', 'contex', 'bring contex', 'wor', 'link', 'word', 'link word', 'similar', 'meanin', 'similar meanin', 'one', 'wor', 'one wor']

# convert all objects to set
total_set = wordlist2set(total, save_order=False)
print2(total_set)
# {'wor', 'ite singl', 'group', 'stemmin', 'meanin similar', 'form inflect', 'differ inflect', 'lemmatizatio', 'analys', 'one', 'ite', 'group togeth', 'ca', 'word', 'meanin', 'singl', 'inflect', 'similar', 'form', 'bring', 'contex', 'link', 'bring contex', 'link word', 'togeth', 'one wor', 'differ', 'proce', 'simila'}


# all these steps are equal to pipeline

pipe = StemLemPipeline([

    text2sentences,phrases2lower,
    lambda sentences: list(map(lambda s: sentence_split(s , separators=',;', stop_words = stopwords('en')), sentences)),
    
    lambda p: phrases_without_excess_symbols(p, include_alpha= True, include_numbers= True),
    lambda p: phrases_transform(p, stem_lem),
    lambda p: phrases_transform(p, func = lambda w: words_to_ngrams_list(w.split(), n_min = 1, n_max = 2)),
    sum_phrases,
    lambda p: wordlist2set(p, save_order=False)
])

pipe(text_example)
# {'wor', 'ite singl', 'group', 'stemmin', 'meanin similar', 'form inflect', 'differ inflect', 'lemmatizatio', 'analys', 'one', 'ite', 'group togeth', 'ca', 'word', 'meanin', 'singl', 'inflect', 'similar', 'form', 'bring', 'contex', 'link', 'bring contex', 'link word', 'togeth', 'one wor', 'differ', 'proce', 'simila'}

print(total_set == pipe(text_example)) # true


