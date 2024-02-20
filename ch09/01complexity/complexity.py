def has_long_words(sentence):
    if isinstance(sentence, str):
        sentence = sentence.split(' ')

    for word in sentence:
        if len(word) > 10:
            return True
    return False


print(has_long_words("This is a nice program."))
print(has_long_words("I love hippopotamuses very much."))
print(has_long_words(["I", "love", "hippopotamuses", "very", "much", "."]))
print(has_long_words(["I", "love", "cats", "very", "much", "."]))
