import random
from collections import Counter

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ')

word = random.choice(someWords)

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a fruit')

    for i in word:
        print('_', " ")
    print()

    playing = True
    letterGuessed = ""
    chances = len(word) + 2
    correct = 0
    flag = 0
    try:
        while (chances != 0) and flag == 0:
            print()
            chances -= 1

            try:
                guess = str(input("Enter a letter to guess: "))
            except:
                print("Enter only a letter.")
                continue

            # Validation of the guess
            if not guess.isalpha():
                print('Enter only a Letter')
                continue
            elif len(guess) > 1:
                print('Enter only one number')
                continue
            elif guess in letterGuessed:
                print("you've already guessed this letter")
                continue

            # If letter is guessed correctly
            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess

            # Print the word
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end=' ')
                    correct += 1
                    # If user has guessed all the letters
                    # Once the correct word is guessed fully,
                elif Counter(letterGuessed) == Counter(word):
                    # the game ends, even if chances remain
                    print("The word is: ", end=' ')
                    print(word)
                    flag = 1
                    print('Congratulations, You won!')
                    break  # To break out of the for loop
                else:
                    print('_', end=' ')

                    # If user has used all of his chances
                if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
                    print()
                    print('You lost! Try again..')
                    print('The word was {}'.format(word))

    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()


