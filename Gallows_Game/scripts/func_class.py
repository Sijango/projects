import random


def make_generator():
    with open('./files/WordsStockRus.txt', 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            yield line.split()


def take_random_word() -> str:
    random_count = random.randint(1, 11650)
    counter = 0
    words = make_generator()
    for word in words:
        counter += 1
        if counter == random_count:
            return word[0]
