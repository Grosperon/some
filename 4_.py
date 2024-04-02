from english_words import get_english_words_set
from hashlib import md5

hash_was = 'c0af77cf8294ff93a5cdb2963ca9f038'

for word_now in get_english_words_set(('web2',)):
    if md5(word_now.encode()).hexdigest()==hash_was:
        print(word_now)
        break
