from scripts import func_class
import time
import os


class Gallows:
    def __init__(self, mistakes: int = 5):  # module initial
        self.health = mistakes
        self.random_word: str = func_class.take_random_word()
        self.len_word = len(self.random_word)
        self.word: str = '*' * self.len_word
        self.last_letter = []
        self.counter: int = 0

    def get_status(self):  # module return status
        print(f'Кол-во попыток: {self.health}')
        print(f'Кол-во букв загаданном слове: {self.len_word}')
        print(f'Ваше слово: {self.word}')
        print(f'Введённая буква: {self.last_letter}\n')

    def choice(self):  # module choice letter
        letter = None
        while not letter:
            letter = input('Введите предполагаемый символ: ')
        self.last_letter.append(letter.lower())

    def check_letter(self) -> bool:  # module check letter
        if self.last_letter[-1] in self.random_word:
            index = self.check_index_letter()
            self.counter += len(index)
            self.word = self.change_word(index)
            return True
        else:
            self.health -= 1
            return False

    def check_index_letter(self) -> list:
        index = []
        for count, item in enumerate(self.random_word):
            if item == self.last_letter[-1]:
                index.append(count)
        return index

    def check_health(self) -> bool:  # module check health
        if self.health != 0:
            return True
        return False

    def change_word(self, index: list) -> str:  # model change word
        word = []
        for i in range(self.len_word):
            if i in index:
                word.append(self.last_letter[-1])
            else:
                word.append(self.word[i])
        return ''.join(word)

    def game_start(self):  # start game xD
        while self.len_word != self.counter and self.check_health():
            self.get_status()
            self.choice()
            if self.check_letter():
                print(f'Вы угадали букву xD')
            else:
                print('Вы не угадали букву x0')
            time.sleep(3)  # SLEEP 3 seconds
            os.system('cls')

        time.sleep(3)
        if self.check_health():
            print(f'Вы выйграли, загаданное слово: {self.random_word} = {self.word}')
        else:
            print(f'Вы проиграли, загаданное слово: {self.random_word}')
        # close game
