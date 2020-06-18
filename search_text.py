def searching(text):
    censored_word=["jebać","nie"]
    list_words=text.split()
    for word in list_words:
        for word in censored_word:
            if word in list_words:
                leng_cens=len(word)
                index_word=list_words.index(word)
                list_words[index_word]=leng_cens*"*"
    print(*list_words)
