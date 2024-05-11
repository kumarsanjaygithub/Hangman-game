import random

def choose_word():
    words = ["hangman", "python", "computer", "programming", "game", "developer", "code", "challenge"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts_left = 6
    
    print("Welcome to Hangman!")
    print("You have 6 attempts to guess the word.")
    
    while attempts_left > 0:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess not in word:
            attempts_left -= 1
            print("Incorrect guess! Attempts left:", attempts_left)
            if attempts_left == 0:
                print("Sorry, you've run out of attempts. The word was:", word)
                break
        else:
            print("Correct guess!")
            if all(letter in guessed_letters for letter in word):
                print("Congratulations! You've guessed the word:", word)
                break

if __name__ == "__main__":
    hangman()
