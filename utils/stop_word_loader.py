def load_stop_words():
    with open('utils/stop_words.txt') as f:
        word_plain = f.read()

    return word_plain.split()
