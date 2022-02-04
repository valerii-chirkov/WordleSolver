from english_words import english_words_set


words_list = []
approved_letters = []
forbidden_letters = []  # If a letter appears in approved_letters - do not add it here, usually, it is not so important


def get_words_list(word_len=5):
    for word in english_words_set:
        if len(word) == word_len:
            words_list.append(word)


def get_possible_word():
    for possible_word in words_list:
        if all([char in possible_word for char in approved_letters]):
            if any([char in possible_word for char in forbidden_letters]):
                pass
            else:
                if possible_word[0] == 'p' and possible_word[1] == 'l':  # add your possitional letters here
                    print(possible_word)


get_words_list()  # 3210
get_possible_word()
