import random

word_list = ['bacon', 'pie', 'cake', 'sandwich', 'hamburger', 'chicken', 'egg', 'ham', 'nut', 'avocado',
             'sushi', 'hockey', 'football', 'Rugby', 'baseball', 'volleyball', 'boxing', 'badminton']
hard_list = []
normal_list = []
easy_list = []
guessed_letter = []
limit_guess = 6

print('Welcome to Hangman!')
print()


def choose_level():
    print('Choose the level.\n1: Hard\n2: Normal\n3: Easy')

    for i in word_list:
        if len(i) >= 8:
            hard_list.append(i)
        elif len(i) > 3 and len(i) < 8:
            normal_list.append(i)
        elif len(i) <= 3:
            easy_list.append(i)

    while True:
        level = input("Plese enter the number: ")
        if level == '1':
            return random.choice(hard_list)
            break

        elif level == '2':
            return random.choice(normal_list)
            break

        elif level == '3':
            return random.choice(easy_list)
            break

        else:
            print("Invalid input. Please enter the number 1 ~ 3.")


answer = choose_level()

display = ['_' for i in range(len(answer))]


# Display current state of the word, guessed letters, incorrect guesses remaining
def display_main():
    print()

    print("Current word: ", end=' ')
    print(*display)

    print("Guessed letters: ", end=' ')
    print(*guessed_letter, sep=', ')
    print(f"Incorrect guesses remaining: {limit_guess}")


while True:
    display_main()

    guess = input("Guess a letter: ")

    if guess not in answer:
        print(f"Sorry, '{guess}' is not in the word.")
        limit_guess -= 1

    else:
        print(f"Good job! '{guess}' is in the word.")
        for index, items in enumerate(answer):
            if items == guess:
                display[index] = guess

    guessed_letter.append(guess)

    # Ending the game
    if '_' not in display:
        print()
        print(f"Congratulations! You guessed the word: {answer}")
        break

    if limit_guess == 0:
        print(f"Game over! The word was: {answer}")
        break