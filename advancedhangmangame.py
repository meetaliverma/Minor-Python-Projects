import random

def get_word(difficulty):
    if difficulty == "easy":
        word_list = ["cat", "dog", "cow", "pig", "bird"]
    elif difficulty == "medium":
        word_list = ["elephant", "giraffe", "rhinoceros", "hippopotamus", "crocodile"]
    else:
        word_list = ["chimpanzee", "orangutan", "gorilla", "lemur", "sloth"]
    return random.choice(word_list)

def play_hangman():
    name = input("What is your name? ")
    print("Welcome to Hangman, " + name + "!")
    difficulty = input("Please choose a difficulty level (easy, medium, hard): ")
    word = get_word(difficulty)
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print("You have", lives, "lives left and you have used these letters: ", " ".join(used_letters))

        # display the current word with underscores for unguessed letters
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").lower()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("Letter is not in word.")
        elif user_letter in used_letters:
            print("You have already used that letter. Please try again.")
        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        print("Sorry, you died. The word was", word)
    else:
        print("Congratulations, you guessed the word", word, "!!")

play_hangman()
