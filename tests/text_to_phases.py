
import sys
sys.path.append('..')


from StemLemPipe import phrases2lower, phrases_without_excess_symbols, phrases_transform, text2sentences, split_by_words, sentence_split, create_stemmer_lemmer, words_to_ngrams_list, sum_phrases, wordlist2set, stopwords


text_example = """Если в жопе шило, я могу достать.
Я имею опыт, лучше "да" сказать.
Влагалище твое в тонус приведу.
Пиши адрес, я приду.

Мой член, словно банан, кривой
И в матку вплоть до дна зайдет,
И полчаса стоять смогет,
Как на границе часовой.

Ты будешь просто разрываться,
Когда начнем с тобой ебаться,
И в счастье будешь же казниться,
Что раньше не решилась соблазниться.

Я медленно сниму штаны с тебя,
И поцелуями сломлю твое сомненье,
От похоти войдешь ты в опьяненье,
Пока не кончишь от меня.

Я смазку принесу с собой,
Сначала ты почувствуешь прохладу,
Но буду жарить я своей большой трубой,
Пока не получу усладу.

Ты напиши, и я приду,
Если не буду очень занят,
Пощекочу твою пизду
Снутри и долго, ибо не устанет.

Я покусаю твою попу
И буду долго трахать в жопу,
Пока ментов не вызовут на вой
Той девки, что кайфует подо мной.

Потом сниму презерватив,
Мирамистином всё полью,
Минут пятнадцать перерыв —
И снова я на час в бою.

И шея будет вся в укусах и засосах,
И будет всё болеть, включая твою грудь,
Но через пару дней, тоскуя без вопросов,
Захочешь эту ночь вернуть."""


sentences = text2sentences(text_example)


phrases = [sentence_split(sentence , separators=',;', stop_words = stopwords('ru')) for sentence in sentences]


clean_phrases = phrases2lower(phrases)


char_phrases = phrases_without_excess_symbols(clean_phrases, include_alpha= True, include_numbers= True)


stem_lem = create_stemmer_lemmer(lemmatizer_backend='pymorphy', stemmer_backend='snowball')


stemmed_phrases = phrases_transform(char_phrases, func = stem_lem)


n_grams = phrases_transform(stemmed_phrases, func = lambda w: words_to_ngrams_list(w.split(), n_min = 1, n_max = 2))

total = sum_phrases(n_grams)

total_set = wordlist2set(total, save_order=False)


