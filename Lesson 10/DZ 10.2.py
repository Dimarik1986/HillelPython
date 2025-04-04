import string

def first_word(text):
    text = text.strip()
    while text and not text[0].isalpha() and text[0] != "'":
        text = text[1:]
    res_word = []
    for word in text:
        if word.isalpha() or word == "'":
            res_word.append(word)
        elif word in " .,;!?":
            break
        else:
            continue
    return "".join(res_word)


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
