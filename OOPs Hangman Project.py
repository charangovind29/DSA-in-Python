import random

HANGMAN = [
    '________',
    '|       |',
    '|       O',
    '|       |',
    '|      /|\ ',
    '|       |',
    '|      / \ '
]

words = [
    'CASA', 'CARRO', 'MONO', 'ESTERNOCLEIDOMASTOIDEO', 'PYTHON', 'DJANGO',
    'MILTON', 'LENIS', 'SWAPPS', 'LOGIA', 'UNITTESTING', 'CHARAN'
]

class Hangman:
    def __init__(self,word_to_guess):
        self.failed_attempts = 0
        self.word_to_guess = word_to_guess
        self.game_progress = list('_'*len(self.word_to_guess))

    def find_indexes(self,letter):
        return [i for i,char in enumerate(self.word_to_guess) if letter == char]
    
    def is_invalid_letter(self,letter):
        return letter.isdigit() or (letter.isalpha() and len(letter)>1)
    
    def print_game_status(self):
        print('\n')
        print('\n'.join(HANGMAN[:self.failed_attempts]))
        print('\n')
        print(' '.join(self.game_progress))

    def update_progress(self,letter,indexes):
        for index in indexes:
            self.game_progress[index] = letter

    def get_user_input(self):
        user_input = input('\nPlease type a letter: ')
        return user_input
    
    def play(self):
        while self.failed_attempts < len(HANGMAN):
            self.print_game_status()
            user_input = self.get_user_input()

            if self.is_invalid_letter(user_input):
                print('The input is not a letter')
                continue

            if user_input in self.game_progress:
                print('You already have guessed this letter')
                continue

            if user_input in self.word_to_guess:
                indexes = self.find_indexes(user_input)
                self.update_progress(user_input,indexes)

                if self.game_progress.count('_') == 0:
                    print('\nYay you won!')
                    print(f'The word is : {self.word_to_guess}')
                    quit()
            else:
                self.failed_attempts += 1
        print('OMG! You lost!, Try again')
        print('\n')
        print(f'The word to guess was {self.word_to_guess}')
            

if __name__ == '__main__':
    word_to_guess = random.choice(words)
    hangman = Hangman(word_to_guess)
    hangman.play()

