"""
PL wyszukiwanie słów i zmiana na wielkie litery
ENG looking for words and changing them to bigger ones
"""
def search_words(text, words):
    list_words=words.split()
    list_text=text.split()
    for word in list_text:
        if word in  list_words:
            index_word=list_text.index(word)
            list_text[index_word]=word.upper()
    print(*list_text)
