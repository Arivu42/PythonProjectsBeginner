import random

chances = 7
print('''Hi!!! Are you ready to guess the number?
You have 7 chances to guess between 1 to 50''')

num_to_guess = random.randrange(50)

guess_count = 0

while guess_count < chances:
    guess_count = guess_count + 1
    user_guess = int(input("Enter you guessing: "))

    if user_guess == num_to_guess:
        print(f'Excellent!!! you guess it correctly!!! the number is {num_to_guess}.')
        break
    elif guess_count >= chances and user_guess != num_to_guess:
        print(f'Oops sorry, The number is {num_to_guess} better luck next time')
    elif user_guess > num_to_guess:
        print("It's higher")
    elif user_guess < num_to_guess:
        print("It's lower")
