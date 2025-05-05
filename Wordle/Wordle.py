import random

word_bank = [
    "apple", "grape", "charm", "flame", "quiet",
    "brave", "storm", "crane", "light", "snack",
    "blush", "craft", "dream", "frost", "glide",
    "honey", "jelly", "knife", "lunar", "magic"
]
word = random.choice(word_bank)
guessedWord = ['_'] * len(word)
attempts = 10
while attemps > 0:
    print('\nCurrent word: '+' '.join(guessedWord))
    guess = input('Guess a letter: ')
    if guess in word:
        for i in range(len(word)):
            if word[i]==guess:
                guessedWord[i] == guess
        print('Great Guess!')
    else:
        attempts -=1
        print(f"Wrong gess! Attempts left: {attempts}")
    if '_' not in guessedWord:
        print('\nCongratulations!! You guessed the word: ', word)
        break
    else:
        print('\nYou\'ve run out of attempts! The word was: ',word)
